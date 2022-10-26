
def outer():
    x = 1
    def inner():
        print(x)
    return inner

foo = outer()

print(foo.__closure__)
