import math
def deg2rad(deg):
    return math.radians(deg)
def rad2deg(rad):
    return math.degrees(rad)
def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))
