from utils import deg2rad, rad2deg, clamp
from vector2d import Vector2D
print(deg2rad(90))
print(rad2deg(1.57))
a = range(10)
clamped =  [clamp(x, 2, 7) for x in a]
print(clamped)


v1 = Vector2D(1, 2)
v2 = Vector2D(2, 3)
print(v1)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1.norm())

