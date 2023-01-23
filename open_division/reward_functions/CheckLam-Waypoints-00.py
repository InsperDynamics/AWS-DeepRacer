def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]

    left_lane = [21,22,23,24,25,26,27,28,29,55,56,57,58,59,60,84,85,86,87,88,89,90,101,102,103,104,105,106,107,108,109]

    center_lane = [0,1,2,3,4,5,6,18,19,20,30,31,32,33,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,61,62,63,64,65,67,68,78,79,80,81,82,83,91,98,99,100,110,111,112,113,114,115,116,117,118,119,120,121]

    right_lane = [7,8,9,10,11,12,13,14,15,16,17,34,35,36,37,38,69,70,71,72,73,74,75,76,77,92,93,94,95,96,97]

    fast = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,26,27,28,29,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,61,62,63,64,65,66,67,68,78,79,80,81,82,83,89,90,98,99,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121]
    slow = [18,19,20,21,22,23,24,25,30,31,32,33,34,35,36,37,38,55,56,57,58,59,60,69,70,71,72,73,74,75,76,77,84,85,86,87,88,91,92,93,94,95,96,97,101,102,103,104,105,106]

    reward = 21

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] == 2 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1 :
            reward += 10
        else:
            reward -= 10
        
    
    return float(reward)
