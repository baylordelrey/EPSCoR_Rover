import matplotlib.pyplot as plot
import numpy as np
ra_hours = 2
ra_minutes = 41
ra_seconds = 39

dec_degrees = 89
dec_minutes = 15
dec_seconds = 51

ra = (ra_hours * 0.26) + (ra_minutes * 0.000290888) + (ra_seconds * .0000048481)
dec = (dec_degrees * 0.0174532925) + (dec_minutes * 0.000290882) + (dec_seconds * 0.0000048481) + np.pi

r = 3;

fig = plot.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("auto")

coord_polar = [ra,dec]

coord_cart = np.array([1,0,0])

#R_X = np.array( [[1,0,0], [0, np.cos(dec), -np.sin(dec)], [0,np.sin(dec),np.cos(dec)]])
R_Y = np.array( [[np.cos(dec), 0, np.sin(dec)], [0,1,0], [-np.sin(dec), 0, np.cos(dec)]])
R_Z = np.array( [[np.cos(ra), -np.sin(ra), 0], [np.sin(ra), np.cos(ra), 0], [0,0,1]])

#print (R_Y)
#print (R_Z)

coord_cart = R_Y.dot(coord_cart)
coord_cart = R_Z.dot(coord_cart)
coord_cart = r * coord_cart

# draw earth
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="g")

#draw celestial sphere r* earth
u2, v2 = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x2 = r*np.cos(u2)*np.sin(v2)
y2 = r*np.sin(u2)*np.sin(v2)
z2 = r*np.cos(v2)
ax.plot_wireframe(x2, y2, z2, color="b")


from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


#
p = Arrow3D([0,coord_cart[0]],[0,coord_cart[1]],[0,coord_cart[2]],mutation_scale=20,
            lw=2, arrowstyle="-|>", color="r")
#ax = plot.gca()
ax.add_artist(p)

#plot.plot(p)
plot.show()
