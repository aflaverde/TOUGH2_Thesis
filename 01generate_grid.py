from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

################################################################################
#IMPORTANT! check PyTOUGH manual for what all these things mean
################################################################################
# number in [] is block width or thickness, number after * is how many 
### Cupiagua GM:
#       x(min): 752465.4798456935      x(max): 779721.4683902061
#       y(min): 565560.7777123338      y(max): 595812.0249052932
#       z(min): -6500.0                z(max): 2800.0

cupiagua_x_min = 752465
cupiagua_x_max = 779465
cupiagua_y_min = 565560
cupiagua_y_max = 595560
cupiagua_z_min = -6500.0
cupiagua_z_max = 2800.0

gm_x_extents = cupiagua_x_max - cupiagua_x_min
gm_y_extents = cupiagua_y_max - cupiagua_y_min
gm_z_extents = cupiagua_z_max - cupiagua_z_min

print('x:', gm_x_extents, 'y:', gm_y_extents, 'z:', gm_z_extents)

x=[1000]*24
y=[1000]*38
z=[400]*3+[300]*10+[150]*5+[80]*12+[100]*5+[150]*10+[200]*5
origin=[750500.6014, 561000.5238, 2300.0]
################################################################################
atmos_type=0
#block naming convention
convention=0
#permeability_dir=-45

#PUT IN YOUR OWN CO-ORDS & shift if you need to
angle=41
# centre = [(cupiagua_x_max+cupiagua_x_min)/2, (cupiagua_y_max+cupiagua_y_min)/2]
centre = [765379.2381, 577152.5589]
#shift=[-4500.0,-1400.0,0.0]
geo=mulgrid().rectangular(x,y,z,convention,atmos_type,origin)
#rotate grid if necessary - need value for angle & centre
geo.rotate(angle,centre)
#geo.permeability_angle=permeability_dir

#translate grid
#geo.translate(shift)
#ADD WELLS - FILE REQ'D#########################################################
#open file & loop thru lines, read &:::::::::::::::::::::::::::::::::::::::::::: 
#
#f=open('well-coords.dat')
#for line in f.readlines():
#  values=line.split(',')
#  print values
#  name=values[0]
#  top=[float(values[1]),float(values[2]),float(values[3])]
#  bot=[float(values[4]),float(values[5]),float(values[6])]
#  w=well(name,[top,bot])
#  geo.add_well(w)
#f.close()
################################################################################
#WRITE GEOMETRY FILE
geo.write('01_grid.dat')
#geo.export_surfer('mulgraph_gridfilename.bna')


