from mulgrids import *
geo = mulgrid('gpestmesh.dat')
nodenames = np.load('pestmesh_nodes.npy')
nnodes = len(nodenames)
dat = np.loadtxt('pestmesh.in').reshape((nnodes,2))
for pos,nodename in zip(dat,nodenames):
    geo.node[nodename].pos = pos
colnames = np.load('pestmesh_columns.npy')
for colname in colnames:
    geo.column[colname].centre = geo.column[colname].centroid
result = []
connames = np.load('pestmesh_connections.npy')
result += [geo.connection[tuple(conname)].angle_cosine for conname in connames]
result += [geo.column[colname].side_ratio for colname in colnames]
f = open('pestmesh.out', 'w')
for r in result: f.write('%20.5f\n'%r)
f.close()