n = 5

for i in range(n):
  for j in range(n-i,0,-1):
    print(' ', end='')
  for k in range(2*i+1):
    print('*', end='')
  print()
for i in range(n-1):
  for j in range(i+2):
    print(' ', end='')
  for k in range(7-2*i,0,-1):
    print('*', end='')
  print()

for i in range(0,n+1,1):
  print(' '*(n-i), end='')
  print('*'*i, end='')
  print('*'*(i-1))
for j in range(0,n,1):
  print(' '*(j+1), end='')
  print('*'*(2*(n-j)-3), end='')
  print()
  
  
  
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))