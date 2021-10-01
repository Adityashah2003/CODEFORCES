n = int(input())
distances = input().split( )
start,stop = input().split()
start = int(start)
stop = int(stop)
buffer=0
if start < stop : 
  for i in range(start-1,stop-1):
    buffer=buffer+int(distances[i])
else :
  for i in range(stop-1 , start-1):
    buffer=buffer+int(distances[i])      
total_distance=0
for i in distances:
  total_distance=total_distance+int(i)
anti = total_distance - buffer
print(min(buffer,anti))
