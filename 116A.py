n=int(input())
buffer=0
maxm=0
while n !=0:
  str=input()
  a,b = str.split( )
  a=int(a)
  b=int(b)
  buffer = buffer - a + b
  if buffer > maxm:
    maxm = buffer
  n=n-1
print(maxm)
