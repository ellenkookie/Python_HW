#Площадь квадрата

import math

def square(side):
    area = side * side

    if not isinstance(side, int):
        area = math.ceil(area)

    return area

print(f"Площадь квадрата со стороной 3: {square(3)}")
print(f"Площадь квадрата со стороной 2.3: {square(2.3)}")