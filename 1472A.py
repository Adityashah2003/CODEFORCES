test = int(input())
while test !=0:
  w,h,n = input().split()
  w = int(w)
  h = int(h)
  n = int(n)
  countw = 1
  counth = 1
  if w%2 == 0 :
    a = w
    while a%2 ==0:
      countw *=2 
      a = a/2
  else:
    countw =1
  if h%2 == 0 :
    b = h
    while b%2 ==0:
      counth *=2 
      b= b/2
  else:
    counth = 1
  total = countw*counth
  if total >= n :
    print("YES")       
  else :
    print("NO")  
  test=test-1 