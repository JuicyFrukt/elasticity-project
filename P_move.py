from Runge_Kutt import R_K



def move_point(start_points: tuple, time):
    points = R_K(time_limits=time, points0=start_points, h=0.01)
    return points