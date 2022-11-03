num = int(input())
a = list(map(int, input().split()))
arr = []

for i in range(24) :
  arr.append(0)

for i in range(num) :
  arr[a[i]] += 1

for i in range(1, 24) :
  print(arr[i], end=" ")
