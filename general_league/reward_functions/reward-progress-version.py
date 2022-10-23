'''
- Model name: reward-progress-version
- Date: 2022-10-22 23:59:59
- Training time: 10h
- Technical features: steps and progress
- Track: Jennens Family Speedway
- Race type: Time trial
- Training algorithm: PPO
- Hyperparameters: 
    Number of experience episodes between each policy-updating iteration: 20
- Space set: continuous
- Speed: range from 0.5 to 4.0
- Steering angle: range from -30 to 30
'''

def reward_function(params):

    # Read input variable
    steps = params['steps']
    progress = params['progress']
    is_offtrack = params['is_offtrack']
    is_crashed = params['is_crashed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with typical value
    reward = 1e-3

    if ((track_width*0.5)-distance_from_center) >= 0.05:
        reward = 1.0 # reward for staying in the center of the track
    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward = 30.0
    if is_offtrack or is_crashed:
        reward = -30.0

    return float(reward)
