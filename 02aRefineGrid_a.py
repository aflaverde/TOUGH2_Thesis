from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

print ('2-a Refine Grid')
#read model grid
geo=mulgrid('01_grid.dat')

#refine the grid where given a list of co-ordinates:
#columns to refine:
columns_refine=np.loadtxt('02apolygon_refine_a.dat',delimiter=',')
#need to find cols in polygon
skinny_columns=geo.columns_in_polygon(columns_refine)
print(skinny_columns)
geo.refine(skinny_columns)
#write geometry file
geo.write('02a_grid.dat')
#geo.export_surfer('g_.bna')