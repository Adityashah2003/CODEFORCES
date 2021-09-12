n = int(input())
x= input()
list=[]
for i in range(0,n-1):
  if x[i] == x[i + 1]:
    list.append(i)
print(len(list))








