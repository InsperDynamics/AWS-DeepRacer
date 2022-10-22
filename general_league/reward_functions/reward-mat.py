def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    is_offtrack = params["is_offtrack"]
    crashed = params["is_crashed"]
    
    
    ABS_STEERING_THRESHOLD = 20
    
    r = speed
    k = distance_from_center
    n = steering_angle
    
    reward = r*((1e-3)**((-k)*n))
    
    if not is_offtrack and not crashed:
        reward+=1
    else:
        reward-=10

    # Always return a float value
    return float(reward)