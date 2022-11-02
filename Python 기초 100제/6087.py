num = int(input())
start = 0

while True :
  start += 1
  
  if start%3 != 0 :
    print(start, end = " ")
    
  if start >= num :
    break
