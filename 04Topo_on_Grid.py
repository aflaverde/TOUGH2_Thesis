from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

print ('Adding topography to optimized grid')
#read model grid
geo=mulgrid('03_grid.dat')

##############################################################################

#this fits the surface to xyz, note can fit specific cols if req'd
topo_data=np.loadtxt('Topography_Cupiagua.dat',delimiter=',')
geo.fit_surface(topo_data,1.0,1.0)
#write geometry file
geo.write('04_grid.dat')

#geo.export_surfer('g_.bna')
