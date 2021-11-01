k, n, m = map(int, input().split())
coin = (k*n)-m

if coin > 0:
  print(coin)
else:
  print(0)