def func(x):
    for i in range(1,x+1):
        yield i

result = list(func(5))
print(result)
for i in range(len(result)):
    print(result[i])
