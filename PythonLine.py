# Question: Create an algorithm to draw
# right triangle in a rectange
#

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

someX, someY = 0.5, 0.5
fig, ax = plt.subplots()
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX-0.1, someY - 0.1), 0.2,0.2, alpha=1,fill=None, facecolor='none'))
plt.show()



