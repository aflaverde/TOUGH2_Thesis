from t2data import *

geo=mulgrid('04_rock_grid_geometry.dat')
#import input file##############################################################
#this can be input after you have put the rock types in Leapfrog & exported
dat=t2data('04_rock_grid.dat')
dat.clear_generators
#go to bottom layer:
layer=geo.layerlist[-1]
#generation rate in W/m2. Recommend 0.10 or if that is too much 0.05, get it 
#warmed up, and then make a new input with 0.10 that should be enough background
#heat.  Add the convective upflow yourself.  Refer to Page 156 onwards of TOUGH2
#manual.This is Appendix which deals with the format of the entire input file.  
q=0.03
for col in geo.columnlist:
   blockname=geo.block_name(layer.name,col.name)
   gen=t2generator(name=col.name+' 1',block=blockname,type='HEAT',gx=q*col.area)
   dat.add_generator(gen)
#write input file###############################################################   
dat.write('001.dat')