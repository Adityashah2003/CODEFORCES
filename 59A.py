import math 
a = int(input())
b = a//5
d = a%5
c = math.floor(b)
if d == 0:
  print(c)
else:
  print(c+1)

