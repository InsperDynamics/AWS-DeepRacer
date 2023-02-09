# - Model name: matmatmat3
# - Date: 10/22/2022
# - Training time: 2h
# - Technical features: 
#     track alignment,
#     more than half-speed, 
#     limited steering angle, 
#     drive near to track center
# - Track: Jennens Family Speedway
# - Race type: Time trial
# - Training algorithm: PPO
# - Hyperparameters: {Entropy : 0,01 ; Learning Rate: 0,001 ; Discount Factor: 0,3  }
# - Space set: continuous
# - Speed: range from 0.5 to 4.0
# - Steering angle: range from -30 to 30
# - Best time: 


def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    is_offtrack = params["is_offtrack"]
    progress = params['progress']
    crashed = params['is_crashed']
    is_reversed = params['is_reversed']
    steering_angle = params["steering_angle"]
    
    r = speed
    k = distance_from_center
    m = progress
    n = steering_angle
    
    # reward = r*((1e-3)**((-k)*n)) --------> antiga
    reward = m*r*((1e-3)**(-k))*(n/20)

    if not is_offtrack and not crashed and not is_reversed:
        reward+=1
    else:
        reward/=10

    # Always return a float value
    return float(reward)