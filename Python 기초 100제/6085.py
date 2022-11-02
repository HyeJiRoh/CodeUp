w, h, b = map(int, input().split())
store = w*h*b
result = store/8/1024/1024
print(format(result, ".2f"), "MB")
