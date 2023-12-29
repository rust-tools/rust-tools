def func(x):
    for y in range(x):
        yield y

for i in func(10): print(i, end = " ")
print(len(func(10)))