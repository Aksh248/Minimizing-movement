from MEC import minimum_enclosing_circle
from nearest_bot import nearest_bot
from math import sin, cos, pi
import numpy as np

import random
import matplotlib.pyplot as plt
# Generate n random robots
#n = 100
#robots = []
#for i in range(n):
#    x = 50 * (0.5 - random.random())
 #   y = 50 * (0.5 - random.random())
  #  robots.append([x, y])


def star_connect(robots,n):
    mec = minimum_enclosing_circle(robots)

    center = mec

    print("Center = { ",mec[0][0],",",mec[0][1],"} Radius = ",round(mec[1],6))



    #fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    #axs[0].scatter([x[0] for x in robots], [x[1] for x in robots])
    #axs[0].scatter( mec[0][0], mec [0][1], color = 'red' )
    #axs[0].set_title('Initial Positions')
    #axs[0].set_xlim(-30, 30)
    #axs[0].set_ylim(-30, 30)


    final=[]
    for i in range(1000):
        theta = random.random() * 2 * pi
        x = mec[0][0] + 5*cos(theta)
        y = mec[0][1] + 5*sin(theta)
        final.append([x, y])

    near = nearest_bot(mec, robots)



    print("The nearest bot to the center of the circle is:", near)
    near_x,near_y = near
    robots2= np.array(robots)
    robots2[robots2 == near_x] = mec[0][0]
    robots2[robots2 == near_y] = mec[0][1]
    print(robots)

    robots.remove(near)
    i=0
    j=0
    x=0
    for x in range(n-1):
        nearest_to_center= nearest_bot(mec,robots)
        near1 =[[[0]*1]*2]
        near1[0][0], near1[0][1]= nearest_to_center
        i,j = nearest_to_center
        nearest_point_on_circle = nearest_bot(near1, final)
        near2 =[[[0]*1]*2]
        near2[0][0], near2[0][1]= nearest_point_on_circle
        #axs[1].scatter( near2[0][0],  near2[0][1], color = 'orange' )

        #for bot2 in robots2:
                #if robots2[i][0] == near1[0][0] and robots2[i][1]== near1 [0][1]:
                    #robots2[i][0] = near2[0][0]
                    #robots2[i][1] = near2[0][1]
                    #i=0
        robots2[robots2 == i] = near2[0][0]
        robots2[robots2 == j] = near2[0][1]
        robots.remove(nearest_to_center)            

    robots2[robots2 == i] = near2[0][0]
    robots2[robots2 == j] = near2[0][1]   
    print(robots2)
    return robots2 
                
                
                

                
                
                            
    #axs[1].scatter([x[0] for x in robots2], [x[1] for x in robots2])

    #axs[1].scatter( center[0][0],  center[0][1], color = 'red' )
    #axs[1].set_title('Final Positions')
    #axs[1].set_xlim(-30, 30)
    #axs[1].set_ylim(-30, 30)


    #plt.show() 

    



