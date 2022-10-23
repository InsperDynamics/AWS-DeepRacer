'''
- Model name: reward-rainbow-road-version
- Date: 2022-10-23 13:24:25
- Training time: 10h
- Technical features: 
    all_wheels_on_track, 
    steering_angle, 
    speed
- Track: Jennens Family Speedway
- Race type: Time trial
- Training algorithm: PPO
- Hyperparameters: 
    batch_size: 128
- Space set: continuous
- Speed: range from 0.5 to 4.0
- Steering angle: range from -30 to 30
'''

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = params['steering_angle']
    speed = params['speed']

    reward = 1e-3

    if all_wheels_on_track:
        reward += 1
    if abs(steering_angle) < 5:
        reward += 1
   
    reward += (speed/8)
   
    return float(reward)
