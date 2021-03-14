"""
    This test is trying to build a Y-shape pipe system in anuga-swmm
    It has two inlet nodes in the same altitude and connect to one outlet node which is in lower altitude
    and see how water flows in the simple system.
    Using the same domain structure like previous testing "test_volume_inlet_op.py"
"""
# ------------------------------------------------------------------------------
# Import necessary modules
# ------------------------------------------------------------------------------
from anuga import Dirichlet_boundary
from anuga import Domain
from anuga import Reflective_boundary
from anuga import Rate_operator
from anuga import Inlet_operator
from anuga import Region
from anuga import rectangular_cross

import anuga
import numpy as num

# ------------------------------------------------------------------------------
# Setup computational domain
# ------------------------------------------------------------------------------

length = 20.
width = 6.
dx = dy = 0.2  # .1           # Resolution: Length of subdivisions on both axes

points, vertices, boundary = rectangular_cross(int(length / dx), int(width / dy),
                                               len1=length, len2=width)
domain = Domain(points, vertices, boundary)
domain.set_name('anuga_swmm')  # Output name based on script name. You can add timestamp=True
print(domain.statistics())


# ------------------------------------------------------------------------------
# Setup initial conditions
# ------------------------------------------------------------------------------
def topography(x, y):
    """Complex topography defined by a function of vectors x and y."""

    z = 0 * x - 5

    # higher pools
    id = x < 10
    z[id] = -3

    # wall
    id = (10 < x) & (x < 15)
    z[id] = 0

    # wall, spilt two inlet areas
    id = (10 > x) & (2.5 < y) & (y < 3.5)
    z[id] = 0

    '''
    not consider the pit's physical depth, just note the physical location
    to setup the depth, just need to modify z[id] = <x>, x represent x meters depth
    '''

    # first pit, locate at (7, 1) radius=1
    id = (x - 7) ** 2 + (y - 1) ** 2 < 1. ** 2
    z[id] -= 0.0

    # second pit, locate at (7, 5) radius=1
    id = (x - 7) ** 2 + (y - 5) ** 2 < 1. ** 2
    z[id] -= 0.0

    # out pit, locate at (17, 3) radius=1
    id = (x - 17) ** 2 + (y - 3) ** 2 < 1 ** 2
    z[id] -= 0.0

    return z


# ------------------------------------------------------------------------------
# Setup initial quantity
# ------------------------------------------------------------------------------

domain.set_quantity('elevation', topography, location='centroids')  # elevation is a function
domain.set_quantity('friction', 0.01)  # Constant friction
domain.set_quantity('stage', expression='elevation', location='centroids')  # Dry initial condition

# ------------------------------------------------------------------------------
# Setup boundaries
# ------------------------------------------------------------------------------
Bi = Dirichlet_boundary([-2.75, 0, 0])  # Inflow
Br = Reflective_boundary(domain)  # Solid reflective wall
Bo = Dirichlet_boundary([-5, 0, 0])  # Outflow
domain.set_boundary({'left': Br, 'right': Br, 'top': Br, 'bottom': Br})

# ------------------------------------------------------------------------------
# Setup inject water
# ------------------------------------------------------------------------------

region_inlet1 = Region(domain, radius=1.0, center=(7., 1.))
region_inlet2 = Region(domain, radius=1.0, center=(7., 5.))
region_outlet = Region(domain, radius=1.0, center=(17., 3.))

region_input1 = Region(domain, radius=1.0, center=(2., 1.))
region_input2 = Region(domain, radius=1.0, center=(2., 5.))

op_inlet1 = Inlet_operator(domain, region_inlet1, Q=0.0, zero_velocity=True)
op_inlet2 = Inlet_operator(domain, region_inlet2, Q=0.0, zero_velocity=True)
op_outlet = Inlet_operator(domain, region_outlet, Q=0.0, zero_velocity=False)

op_input1 = Inlet_operator(domain, region_input1, Q=0.25)
op_input2 = Inlet_operator(domain, region_input2, Q=0.25)

x = domain.centroid_coordinates[:, 0]
indices = num.where(x < 10)
anuga.Set_stage(domain, stage=-2.75, indices=indices)()

# ------------------------------------------------------------------------------
# couple SWMM
# ------------------------------------------------------------------------------
# TODO: couple SWMM




for t in domain.evolve(yieldstep=1.0, finaltime=20.0):
    print('\n')
    domain.print_timestepping_statistics()


















