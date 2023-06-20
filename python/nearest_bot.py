import math

def nearest_bot(mec,robots):
    # Coordinates of the center of the circle
    center_x = mec[0][0]
    center_y = mec[0][1]



    # Initialize variables to hold minimum distance and corresponding bot
    min_distance = math.inf
    nearest_bot = [0,0]
    #print(min_distance)

    # Loop through each bot and calculate its distance to the center of the circle
    for bot in robots:
        bot_x, bot_y = bot
        distance = math.sqrt((bot_x - center_x)**2 + (bot_y - center_y)**2)
        
        # If this bot is closer than the previous closest bot, update the variables
        if distance < min_distance:
            min_distance = distance
            nearest_bot = bot
            
    # Print the nearest bot's coordinates
    
    return nearest_bot


