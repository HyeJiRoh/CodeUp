num = int(input())
arr =[]

for i in range(20) :
  arr.append([])
  for k in range(20) :
    arr[i].append(0)

for i in range(num):
  x, y = map(int, input().split())
  arr[x][y] = 1

for i in range(1,20) :
  for k in range(1,20) :
    print(arr[i][k], end = " ")
  print()
