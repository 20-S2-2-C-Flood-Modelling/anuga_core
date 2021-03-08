import anuga
from anuga import Inlet_operator
from anuga.structures.boyd_pipe_operator import Boyd_pipe_operator
import numpy as num
#import numpy as np
#import matplotlib.pyplot as plt
from anuga.structures.inlet import Inlet

"""
bounding_domain = anuga.rectangular_cross_domain(10, 5, len1=10.0, len2=5.0)
base_resolution = 10.0  #m^2
merewether_resolution = 0.5
merewether_domain = anuga.rectangular_cross_domain(5, 2, len1=2.0, len2=1.0)
interior_regions = [[merewether_domain, merewether_resolution]]
domain = anuga.create_domain_from_regions(bounding_domain,boundary_tags={
                                        'bottom':[0],'right':[1],'top':[2],'left':[3]},
                                        maximum_triangle_area=base_resolution,
                                        interior_regions=interior_regions
                                          )
"""
#domain = anuga.rectangular_cross_domain(10,5,len1 = 2.5, len2 = 1.0)
bounding_polygon = [[0.0, 0.0],
                    [20.0, 0.0],
                    [20.0, 10.0],
                    [0.0, 10.0]]

boundary_tags={'bottom': [0],
                'right': [1],
                'top': [2],
                'left': [3]}
domain = anuga.create_domain_from_regions(bounding_polygon,
                               boundary_tags,
                               maximum_triangle_area = 0.5,
                               )
domain.set_name("small_resolution1")
#domain.set_name('merewether1') # Name of sww file
#dplotter = anuga.Domain_plotter(domain)
#plt.triplot(dplotter.triang, linewidth = 0.4);

domain.set_quantity('elevation', 0.5)
domain.set_quantity('friction', 0.01)         # Constant friction
domain.set_quantity('stage',
                    expression='elevation')   # Dry initial condition
Bi = anuga.Dirichlet_boundary([2.0, 0, 0])         # Inflow
Bo = anuga.Dirichlet_boundary([-2, 0, 0])
Br = anuga.Reflective_boundary(domain)             # Solid reflective wall

domain.set_boundary({'left': Bi, 'right': Br, 'top': Br, 'bottom': Br})
end_point0 = num.array([0.35, 2.5])
end_point1 = num.array([17.0, 2.5])
"""
#if I use this method then the surface would have 2 raised water peaks.
Boyd_pipe_operator(domain,
                    #end_point0=[9.0, 2.5],
                    #end_point1=[13.0, 2.5],
                    #exchange_line0=[[9.0, 1.75],[9.0, 3.25]],
                    #exchange_line1=[[13.0, 1.75],[13.0, 3.25]],
                    losses=1.5,
                    end_points=[end_point0, end_point1],
                    diameter=0.375,
                    #apron=0.5,
                    use_momentum_jet=True,
                    use_velocity_head=False,
                    manning=0.013,
                    #logging = True,
                    #label = 'culvert_output',
                    verbose=False)
"""
line = [[3.0, 2.5], [14.0, 2.5],[5.5,4.0]]
Q = -25.0


def dynamic_Q (t,yieldstep):
    t = t+yieldstep
    return Q+t


inlet0 = Inlet_operator(domain, line,Q=0.0)

for t in domain.evolve(yieldstep=0.5, finaltime=20.0):
    Q = dynamic_Q(0,0.5)
    inlet0.set_Q(dynamic_Q(0,0.5))
    domain.print_timestepping_statistics()
    #domain.set_quantity('stage',None,None)
    #print(inlet0.timestepping_statistics())
    #Q = dynamic_Q(0,yieldstep=0.5)

    print(inlet0.get_Q(),"Q")
    print(inlet0.inlet.get_average_speed(),"avsp")
    print(inlet0.inlet.get_depths(),"dp")





