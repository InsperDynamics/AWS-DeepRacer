'''
- Model name: reward-the-holy-version
- Date: 2022-10-25 21:05:00
- Training time: ?h
- Technical features: chooses best steering angle and gives reward based on error
- Track: Jennens Family Speedway
- Race type: Time trial
- Training algorithm: PPO
- Hyperparameters: 
    discount_factor: 0.5
- Space set: continuous
- Speed: range from 1.0 to 4.0
- Steering angle: range from -30 to 30
'''
import math


def dist(p1, p2): # distance between two points
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def to_polar(x, y): # convert to polar coordinates
    coordinate_r = (x ** 2 + y ** 2) ** 0.5
    coordinate_theta = math.degrees(math.atan2(y,x))
    return coordinate_r, coordinate_theta

def angle_between_minus180_and_plus180(angle): # change the angle to be in the range of [-180, 180]
    n = math.floor(angle/360.0)
    angle = angle - n*360.0
    if angle <= 180.0:
        return angle
    return angle - 360.0

def multiply_waypoints(waypoints, many_times): # make multiply the amount of waypoints, with less distance between them
    n = len(waypoints)
    return [[i / many_times * waypoints[(j+1) % n][0] + (1 - i / many_times) * waypoints[j][0], i / many_times * waypoints[(j+1) % n][1] + (1 - i / many_times) * waypoints[j][1]] for j in range(n) for i in range(many_times)]

def get_target_point(params):
    # waypoints provided in counter clock wise order
    waypoints = params['waypoints'] # car in counter clock wise
    if params['is_reversed']: # car in clock wise
        waypoints = list(reversed(params['waypoints']))
    waypoints = multiply_waypoints(waypoints, 20)

    coordinates = [params['x'], params['y']]
    distance_list = [dist(p, coordinates) for p in waypoints]
    i_closest = distance_list.index(min(distance_list))

    n = len(waypoints)
    waypoints_starting_with_closest = [waypoints[(i+i_closest) % n] for i in range(n)]
    coordinate_r = params['track_width'] * 0.9
    is_inside = [dist(p, coordinates) < coordinate_r for p in waypoints_starting_with_closest]
    i_first_outside = is_inside.index(False)
    
    if i_first_outside < 0:  # only happens if coordinate_r is as big as the entire track
        return waypoints[i_closest]
    return waypoints_starting_with_closest[i_first_outside]

def reward_function(params):
    tx, ty = get_target_point(params)
    dx = tx-params['x']
    dy = ty-params['y']
    _, target_angle = to_polar(dx, dy)
    best_steering_angle = angle_between_minus180_and_plus180(target_angle - params['heading'])
    error = (params['steering_angle'] - best_steering_angle) / 60.0
    reward = 1.0 - abs(error)
    return float(max(reward, 0.01)) # optimizer struggle with negative numbers and numbers too close to zero
