import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi,voronoi_plot_2d

points = np.random.rand(4,2)
print points
vor = Voronoi(points)
voronoi_plot_2d(vor)

# for region in vor.regions:
#     if not -1 in region:
#         polygon = [vor.vertices[i] for i in region]
#         plt.fill(*zip(*polygon))


print "vertives is: "+str(vor.vertices)
print 

# There is a single finite Voronoi region, and four finite Voronoi
# ridges:

print "regions is: " +str(vor.regions)
print 
print "redge_vertices is:" + str(vor.ridge_vertices)


# The ridges are perpendicular between lines drawn between the following
# input points:

print "ridge_points is: " + str(vor.ridge_points)
plt.show()