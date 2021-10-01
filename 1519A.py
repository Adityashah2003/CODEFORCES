n = int(input())
while n != 0:
  r, b, d = input().split()
  r = int(r)
  b = int(b)
  d = int(d)
  chota = min(r, b)
  bada = max(r, b)
  if (d+1)*chota>=bada:
    print("Yes")
  else:
    print("NO")
  n = n - 1
