import math
import random
import matplotlib.pyplot as plt

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def Connect(Pi, Pj, d):
    # Finding the closest point in Pj for each point in Pi
    closest_points = []
    for u in Pi:
        min_dist = float('inf')
        for v in Pj:
            dist = distance(u, v)
            if dist < min_dist:
                min_dist = dist
                v_star = v
        closest_points.append(v_star)
    # Computing the displacement vector for all points in Pi and Pj
    new_positions = []
    for i, u in enumerate(Pi + Pj):
        neighbors = Pi + Pj
        neighbors.remove(u)
        disp = [0, 0]
        for v in neighbors:
            if distance(u, v) <= d:
                disp[0] += v[0] - u[0]
                disp[1] += v[1] - u[1]
        new_positions.append([u[0] + disp[0], u[1] + disp[1]])

    return [tuple(pos) for pos in new_positions]


def cluster_connect(X, r, d):

    clusters = []
    visited = set()
    for i in range(len(X)):
        if i not in visited:
            cluster = [X[i]]
            visited.add(i)
            queue = [i]
            while queue:
                u = queue.pop(0)
                for v in range(len(X)):
                    if v not in visited and distance(X[u], X[v]) <= r:
                        cluster.append(X[v])
                        visited.add(v)
                        queue.append(v)
            clusters.append(cluster)

    # Connect all clusters to each other
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            Pi, Pj = clusters[i], clusters[j]
            if distance(Pi[0], Pj[0]) <= r:
                Pi_new, Pj_new = Connect(Pi, Pj, d)
                clusters[i] = Pi_new
                clusters[j] = Pj_new

    # Create a list of edges connecting pairs of robots
    edges = []
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            if distance(X[i], X[j]) <= r:
                edges.append((i, j))

    # Add edges iteratively until all robots are connected
    while len(edges) > 0:
        # Find the closest pair of unconnected robots
        min_dist = float('inf')
        min_edge = None
        for edge in edges:
            if distance(X[edge[0]], X[edge[1]]) < min_dist:
                min_dist = distance(X[edge[0]], X[edge[1]])
                min_edge = edge
        # Adding the edge to the list of connected edges
        edges.remove(min_edge)
        # Updating the position of the robots
        u, v = min_edge
        X[u], X[v] = Connect([X[u]], [X[v]], d)

    return X

# Generating robots and storing their location in the list robots
#n = 40                                         #number of bots
#robots = []
#for i in range(n):
    #x = 50 * (0.5 - random.random())           #max x value = 25 for workspace formation
    #y = 50 * (0.5 - random.random())           #max y value = 25 for workspace formation
    #robots.append([x, y])

# Run the Cluster Connect algorithm
#r = 5
#positions = cluster_connect(robots, r, 0)

# Ploting the initial and final positions of the robots

#fig, axs = plt.subplots(1, 2, figsize=(10, 5))
#axs[0].scatter([x[0] for x in robots], [x[1] for x in robots])
#axs[0].set_title('Initial Positions')
#axs[0].set_xlim(-30, 30)
#axs[0].set_ylim(-30, 30)

#axs[1].scatter([x[0] for x in positions], [x[1] for x in positions])
#axs[1].set_title('Final Positions')
#axs[1].set_xlim(-30, 30)
#axs[1].set_ylim(-30, 30)

# Plot the connections between the robots
#fig.suptitle(f"Number of bots spawned = {n}")

#for i in range(len(positions)):
    #for j in range(i+1, len(positions)):
        #d = distance(positions[i], positions[j])
        #if d <= r:
            #axs[1].plot([positions[i][0], positions[j][0]], [positions[i][1], positions[j][1]], 'k-', alpha=0.3)

#plt.show()