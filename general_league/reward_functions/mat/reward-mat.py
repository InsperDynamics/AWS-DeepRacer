# - Model name: Hello-World-De-Carrinho-Versao-Matematica-Avancada
# - Date: 10/21/2022, 9:51:12 PM GMT-3
# - Training time: 2h
# - Technical features: 
#     track alignment,
#     more than half-speed, 
#     limited steering angle, 
#     drive near to track center
# - Track: 2022 re:Invent Championship
# - Race type: Time trial
# - Training algorithm: PPO
# - Hyperparameters: standard
# - Space set: continuous
# - Speed: range from 0.5 to 4.0
# - Steering angle: range from -20 to 20
# - Best time: mais de 3 minutos


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
    
    # reward = r*((1e-3)**((-k)*n)) --------> antiga
    reward = r*((n)**(-k))
    
    if not is_offtrack and not crashed:
        reward+=1
    else:
        reward-=10

    # Always return a float value
    return float(reward)