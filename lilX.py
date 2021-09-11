n= int(input())
x = [int(x) for x in input().split()]
y = [int(x) for x in input().split()]
x.remove(x[0])
y.remove(y[0])
z=x+y
final_list = []
for x in z:
	if x not in final_list:
		final_list.append(x)

if len(final_list)==n:
	print("I become the guy.")
else :
    print("Oh, my keyboard!")