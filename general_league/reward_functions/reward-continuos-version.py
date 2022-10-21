'''
- Model name: reward-4th-version
- Date: 2022-10-21
- Training time: 3h
- Technical features: 
    track alignment, 
    more than half-speed, 
    limited steering angle, 
    drive near to track center
- Track: Jennens Family Speedway
- Race type: Time trial
- Training algorithm: PPO
- Hyperparameters: standard
- Space set: continuous
- Speed: range from 0.5 to 4.0
- Steering angle: range from -30 to 30
'''

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are increasingly further away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return reward