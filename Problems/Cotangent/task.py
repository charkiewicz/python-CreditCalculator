import math

degree = int(input())
degree = math.radians(degree)
cot = math.cos(degree) / math.sin(degree)

print(round(cot, 10))
