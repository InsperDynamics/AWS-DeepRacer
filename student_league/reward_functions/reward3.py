import math

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    is_reversed = params['is_reversed']
    
    # Dfine the constant values for comparison
    ABS_STEERING_THRESHOLD = 20.0
    DIRECTION_THRESHOLD = 10.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Give a very low reward by default
    reward = 1e-3

    # Give a small but relevant reward if no wheels go off the track and the car is not reversed
    if all_wheels_on_track and not(is_reversed):
        reward = 1.0
        if ((track_width*0.5)-distance_from_center) >= 0.05:
            reward *= 4.0 # reward for staying in the center of the track
            if steering_angle <= ABS_STEERING_THRESHOLD:
                reward *= 4.0 # reward commonly if steering angle is in acceptable range
            if speed >= 0.5:
                reward *= 10.0*speed # reward heavily if speed is higher than half of max speed
            if speed < 0.5:
                reward *= speed/5.0 # penalize if speed is less than half of its max
        if direction_diff > DIRECTION_THRESHOLD:
            reward *= 0.1 # penalize if the car is not alligned with the track direction

    # Always return a float value
    return float(reward)
