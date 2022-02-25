from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

print ('2-b Refine Grid - Second refinement')
#read coarse model grid
geo=mulgrid('02a_grid.dat')

#ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt

#refine the grid where given a list of co-ordinates:
#columns to refine:
columns_refine=np.loadtxt('02bpolygon_refine_b.dat',delimiter=',')
print (columns_refine)
#need to find cols in polygon
skinny_columns=geo.columns_in_polygon(columns_refine)
print (skinny_columns)
geo.refine(skinny_columns)

##############################################################################

#write geometry file
geo.write('02b_grid.dat')
#geo.export_surfer('g_.bna')
