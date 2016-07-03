import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi,voronoi_plot_2d

points = np.random.rand(15,2)
vor = Voronoi(points)
voronoi_plot_2d(vor)

for region in vor.regions:
    if not -1 in region:
        polygon = [vor.vertices[i] for i in region]
        plt.fill(*zip(*polygon))

plt.show()
