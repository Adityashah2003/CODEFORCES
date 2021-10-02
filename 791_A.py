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
if h%2 == 0 :
  b = h
  while b%2 ==0:
     counth *=2 
total = countw*counth
if total >= n :
  print("YES")       
else :
  print("NO")  