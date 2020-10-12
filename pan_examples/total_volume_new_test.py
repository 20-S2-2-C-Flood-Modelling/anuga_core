"""
This is the first prototype (testing) for the ANUGA & SWMM coupling project

In this testing, we are expecting to create a one-pipe testing. Flowing water out from ANUGA to SWMM, and using the SWMM
calculate the water flow activities in the pipe, and flows back to ANUGA.

we can validate this testing by monitor the change of the water total volume. It should remains the same between flowing
to SWMM and flowing back to ANUGA.
"""


# ------------------------------------------------------------------------------
# Import necessary modules
# ------------------------------------------------------------------------------
from anuga import Dirichlet_boundary
from anuga import Domain
from anuga import Reflective_boundary
from anuga.operators.rate_operators import Rate_operator
from anuga import Region
from anuga import rectangular_cross
import numpy as num

# ------------------------------------------------------------------------------
# Setup computational domain
# ------------------------------------------------------------------------------

length = 15.
width = 5.
dx = dy = 0.2  # .1           # Resolution: Length of subdivisions on both axes

points, vertices, boundary = rectangular_cross(int(length / dx), int(width / dy),
                                               len1=length, len2=width)
domain = Domain(points, vertices, boundary)
domain.set_name('total_volume_testing')  # Output name based on script name. You can add timestamp=True
print(domain.statistics())


# ------------------------------------------------------------------------------
# Setup initial conditions
# ------------------------------------------------------------------------------
def topography(x, y):
    """Complex topography defined by a function of vectors x and y."""

    z = 0 * x - 5

    # higher pools
    id = x < 5
    z[id] = -3

    # wall
    id = (5 < x) & (x < 10)
    z[id] = 0

    # inflow pipe hole, located at (2, 2), r = 0.5, depth 0.1
    id = (x - 2) ** 2 + (y - 2) ** 2 < 0.3 ** 2
    z[id] -= 0.2

    # inflow pipe hole, located at (12, 2), r = 0.5, depth 0.1
    id = (x - 12) ** 2 + (y - 2) ** 2 < 0.3 ** 2
    z[id] -= 0.2

    return z


# ------------------------------------------------------------------------------
# Setup initial quantity
# ------------------------------------------------------------------------------
domain.set_quantity('elevation', topography)  # elevation is a function
domain.set_quantity('friction', 0.01)  # Constant friction
domain.set_quantity('stage', expression='elevation')  # Dry initial condition
# --------------------------

"""
We would use this method to gain the boundary indices
"""


# polygon1 = [ [10.0, 0.0], [11.0, 0.0], [11.0, 5.0], [10.0, 5.0] ]
# polygon2 = [ [10.0, 0.2], [11.0, 0.2], [11.0, 4.8], [10.0, 4.8] ]

def get_cir(radius=None, center=None, domain=None, size=None, polygons=None):
    if polygons is not None:
        polygon1 = polygons[0]  # the larger one
        polygon2 = polygons[1]
        opp1 = Rate_operator(domain, polygon=polygon1)
        opp2 = Rate_operator(domain, polygon=polygon2)
        if isinstance(polygon1, Region):
            opp1.region = polygon1
        else:
            opp1.region = Region(domain, poly=polygon1, expand_polygon=True)
        if isinstance(polygon2, Region):
            opp2.region = polygon2
        else:
            opp2.region = Region(domain, poly=polygon2, expand_polygon=True)

    if radius is not None and center is not None:
        region1 = Region(domain, radius=radius, center=center)
        if size < 0.03:
            #if the size of triangle is too small then this method cannot get the boundary indices.
            region2 = Region(domain, radius=radius - size * 4, center=center)
        else:
            region2 = Region(domain, radius=radius - size, center=center)

    if radius is None and center is None:
        indices = [x for x in opp1.region.indices if x not in opp2.region.indices]
    else:
        indices = [x for x in region1.indices if x not in region2.indices]

    return indices


def get_depth(operator):

    # need check each triangle's area should be dx*dy/4
    # here is the inlet depth
    len_boud_pipe = len(operator.stage_c[:].take([get_cir(radius=0.5, center=(2.0, 2.0), domain=domain, size=0.01)])[0])
    overland_depth = sum(operator.stage_c[:].take([get_cir(radius=0.5, center=(2.0, 2.0), domain=domain, size=0.01)])
                         [0]-operator.elev_c[:].take([get_cir(radius=0.5, center=(2.0, 2.0), domain=domain, size=0.01)])
                         [0]) / len_boud_pipe
    # the overland_depth should be got from ANUGA directly

    return overland_depth

# ------------------------------------------------------------------------------
# Setup boundaries
# ------------------------------------------------------------------------------
Bi = Dirichlet_boundary([0.1, 0, 0])  # Inflow
Br = Reflective_boundary(domain)  # Solid reflective wall
Bo = Dirichlet_boundary([-5, 0, 0])  # Outflow

domain.set_boundary({'left': Br, 'right': Br, 'top': Br, 'bottom': Br})

# ------------------------------------------------------------------------------
# Setup inject water
# ------------------------------------------------------------------------------
op_inlet = Rate_operator(domain, radius=0.5, center=(2., 2.))
op_outlet = Rate_operator(domain, radius=0.5, center=(12., 2.))  #


from pyswmm import Simulation, Nodes, Links

sim = Simulation('./pipe_test.inp')
sim.start()
node_names = ['Inlet', 'Outlet']

link_names = ['Culvert']

nodes = [Nodes(sim)[names] for names in node_names]
links = [Links(sim)[names] for names in link_names]

# type, area, length, orifice_coeff, free_weir_coeff, submerged_weir_coeff
nodes[0].create_opening(4, 0.785, 1.0, 0.6, 1.6, 1.0)
nodes[0].coupling_area = 0.785


nodes[1].create_opening(4, 0.785, 1.0, 0.6, 1.6, 1.0)
nodes[1].coupling_area = 0.785


print("node1_is_open?:",nodes[1].is_coupled)

def total_vol_evovle(stop_release_water_time,release_water):
    """
    stop_release_water: double
                        It should be able to divide by 1.0 and less than 55.0.
    release_water: double
                    It should be greater than 0.0.
    """
    op_release_inlet = Rate_operator(domain, radius=0.5, center=(1., 4.))
    # set a new inlet location to avoid the wave over the swmm pipe's inlet.
    domain.set_name("anuga_swmm")

    for t in domain.evolve(yieldstep=1.0, finaltime=55.0 + stop_release_water_time + 10):
        """
        The coupling step is 1.0 second and the finaltime is 55 seconds for the coupling model to evolve,
        10 seconds for the waiting time in order to make the initial water calm down. 
        """
        if t < stop_release_water_time:
            # assume we need to release the water into the domain for first "stop_release_water_time" seconds
            op_release_inlet.set_rate(release_water)

        else:
            #After release the water into the left domain part, we would closed the inlet for calming down the waves.
            op_release_inlet.set_rate(0)
            op_outlet.set_rate(0)

            if t >= stop_release_water_time + 10:
                # start couple
                nodes[0].overland_depth = get_depth(op_inlet)
                volumes = sim.coupling_step(1.0)
                volumes_in_out = volumes[-1][-1]
                if t == stop_release_water_time + 10:
                    """
                    The first return of the pyswmm is different. I choose the larger answer to represent as the 
                    first second's volume.
                    """
                    inlet_volume = volumes[0][-1]["Inlet"]
                    fid = op_inlet.full_indices
                    op_inlet.set_rate(-1 * inlet_volume / num.sum(op_inlet.areas[fid]))
                    op_outlet.set_rate(nodes[1].total_inflow / nodes[1].coupling_area)

                else:
                    op_inlet.set_rate(-1 * volumes_in_out['Inlet'] / nodes[0].coupling_area)
                    Q = nodes[1].total_inflow
                    fid = op_outlet.full_indices
                    rate = Q / num.sum(op_outlet.areas[fid])
                    op_outlet.set_rate(rate)

        if t == 65+stop_release_water_time:
            print("\n")
            print(f"coupling step: {t}")
            print("total volume: ", domain.get_water_volume())
            print("stop time",stop_release_water_time)
            print("release water:",release_water*stop_release_water_time)



total_vol_evovle(4,3)
#Here is used for changing argument conveniently.

















