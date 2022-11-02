h, b, c, s = map(int, input().split())
store = h*b*c*s
result = store/8/1024/1024
print(format(result, ".1f"), 'MB')
