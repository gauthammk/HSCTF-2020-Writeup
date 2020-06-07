from math import sqrt

level = 25
# iterative method
for i in range(1, level + 1):
    if i == 1:
        side = sqrt(70368744177664)
        area = 70368744177664
        print('level 1 area : ', area, side)
    else:
        side = sqrt(1/2) * side
        area = pow(2, i - 1) * pow(side, 2) + area
        print('level', i, ' area : ', area, side)
