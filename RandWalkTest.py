import matplotlib.pyplot as plt
from RandWalkDemo import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
point = range(rw.num_points)
ax.scatter(0,0,c='green',edgecolor='none',s=100)
ax.scatter(rw.x_values, rw.y_values, c=point, cmap=plt.cm.Reds,
           edgecolor='none', s=10)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
