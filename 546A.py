first_banana,dollars,no_of_bananas = input().split()
first_banana = int(first_banana)
dollars = int(dollars)
no_of_bananas = int(no_of_bananas)
total_cost=0
for i in range (1 , no_of_bananas+1):
  x = first_banana*i
  total_cost = x+ total_cost
y = total_cost - dollars
if y<=0:
  print("0")
else:
  print(y)