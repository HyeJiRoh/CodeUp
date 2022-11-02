num = int(input())
start = 1
sum =0

while True:
  sum += start
  start += 1
  if sum>=num :
    break
print(sum)
