# - Model name: Ronnenberg-Fumiaki-StableHyperparams-Discrete-clone02
# - Date: Mon, 06 Feb 2023 18:33:09 GMT
# - Training time: 24h
# - Technical features: 
#     track alignment,
#     more than half-speed, 
#     limited steering angle, 
#     drive near to track center
# - Track: Fumiaki Loop
# - Race type: Time trial

# Gradient descent batch size	256
# Entropy	0
# Discount factor	0.9999
# Loss type	Huber
# Learning rate	0.00003
# Number of experience episodes between each policy-updating iteration	100
# Number of epochs	10

# - Training algorithm: PPO
# - Space set: continuous
# - Speed: range from 1.5 to 2.5
# - Steering angle: range from -20 to 20
# - Total time: 02:16.797
def reward_function(params):
    reward = 0.01
    if params['all_wheels_on_track'] and params['steps'] > 0:
        reward = float((params['progress'])/params['steps']*100)+(params['speed']**2)
    return reward