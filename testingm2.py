
def decorator(func):
    def wrapper(a, b):
        print("Func is working:")
        result = func(a, b)
        print("Func stopped!\nSee result:")
        return result
    return wrapper



@decorator
# func:
def sum(a, b):
    return a + b

print(sum(1, 2))

