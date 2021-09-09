codes = int(input())
count=0
while codes != 0 :
  code_1 = input()
  x,y,z = code_1.split()
  x=int(x)
  y=int(y)
  z=int(z)
  if x+y+z >1:
    count +=1
  else:
    count+=0
  codes=codes-1
print(count)


