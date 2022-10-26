
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply(func, x, y):
    return func(x, y)

print(apply(add, 2, 1))

print(apply(sub, 2, 1))
