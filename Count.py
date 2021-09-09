n,k = input().split()
n=int(n)
k=int(k)
count= 0
x=0
scores = input().split( )
buffer= int(scores[k-1])
for i in scores:
  x+=int(i)
if x>0:
  for i in scores:
    if int(i) >=buffer:
      if int(i)>0:
        count+=1
  print(count)
else:
  print(0)
