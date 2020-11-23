import numpy as np
import math

walk_seed = 2025678

num_steps = 500 + 10 * (walk_seed % 11) - 50

np.random.seed(walk_seed)

journeys = 20000

max_distance = np.zeros(journeys)

for j in range(journeys):
    x_c = 0
    y_c = 0
    max_x = 9
    max_y = 6
    current_max_distance = math.sqrt(max_x**2+max_y**2)
    
    for i in range(num_steps):
        
        direction = np.random.randint(0,3)
        
        if direction == 0:
            x_c += 1
        if direction == 1:
            x_c -= 1
        if direction == 2:
            y_c += 1
        if direction == 3:
            y_c -= 1
            
        current_distance = math.sqrt(x_c * x_c + y_c * y_c)
        current_distance_round = math.trunc(current_distance)
        # print(current_distance_round)
        
        if current_distance_round > current_max_distance:
            current_max_distance = current_distance_round 
            
            
    max_distance[j] = current_distance_round 