import random
from math import sqrt
import math
from MEC import minimum_enclosing_circle
from star_final_code import star_connect
from cluster_connect_final import cluster_connect
import matplotlib.pyplot as plt
from moving_the_bot import move_bot
n = 500
robots = []
for i in range(n):
    x = 50 * (0.5 - random.random())
    y = 50 * (0.5 - random.random())
    robots.append([x, y])

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].scatter([x[0] for x in robots], [x[1] for x in robots])
axs[0].set_title('Initial Positions')
axs[0].set_xlim(-30, 30)
axs[0].set_ylim(-30, 30)
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

mec = minimum_enclosing_circle(robots)
#defining connectivity radius to be 3
r = 3
center = mec

print("Center = { ",mec[0][0],",",mec[0][1],"} Radius = ",round(mec[1],6))
L = round(mec[1],6)

test = L/r
if test >= sqrt(n):
    positions = star_connect(robots,n)
else:
    positions = cluster_connect(robots,r,0)



axs[1].scatter([x[0] for x in positions], [x[1] for x in positions])
axs[1].set_title('Final Positions')
axs[1].set_xlim(-30, 30)
axs[1].set_ylim(-30, 30)

    # Plot the connections between the robots

for i in range(len(positions)):
    for j in range(i+1, len(positions)):
        d = distance(positions[i], positions[j])
        if d <= r:
            axs[1].plot([positions[i][0], positions[j][0]], [positions[i][1], positions[j][1]], 'k-', alpha=0.3)
i=0
while i in range(length(positions)):
    move_bot(positions[i], positions[j])

plt.show()