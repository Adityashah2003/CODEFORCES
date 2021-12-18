n=int(input())
list = []
while n!=0:
  number = int(input())
  buffer= number/2050
  if number%2050 !=0:
    print("-1")
  else:
    sum=0
    while buffer!=0:
      sum = sum +int(buffer%10)
      buffer = int(buffer/10)
    print(sum)
  n=n-1
#yo