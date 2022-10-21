def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    
    ABS_STEERING_THRESHOLD = 20

    # Give a very low reward by default
    reward = 1e-3
    if all_wheels_on_track:
        reward += 1
        if ((track_width*0.5)-distance_from_center) >= 0.05:
            reward += 4
            if steering_angle <= ABS_STEERING_THRESHOLD:
                reward *= speed

    # Always return a float value
    return float(reward)