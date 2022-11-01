num = int(input())
sum = 0
count = 0

for i in range(1, num) :
  count +=1
  sum += i
  if sum >= num :
    break
print(count)
