from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

#open geometry file  BEN check the name!
geo=mulgrid('04_grid.dat')
#open input data file
 
dat=t2data('05_1D_21_eos1.dat')

dat.grid=t2grid().fromgeo(geo)

#plot horiz layer for checking
#geo.layer_plot(1525.5)

#write input file
dat.write('001.dat')
#probably best to now import this to Leapfrog and create flow model with rock
#types on it, and export that to get heat generators