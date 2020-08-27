from PIL import Image
from pylab import *

im = array(Image.open("data/state-empire-building.jpg").convert("L"))

figure()
gray()
contour(im, origin="image")

axis("equal")
axis("off")
show()