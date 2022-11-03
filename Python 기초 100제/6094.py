num = int(input())
a = list(map(int, input().split()))
min = 24

for i in range(num):
  if min>a[i] :
    min = a[i]

print(min)
