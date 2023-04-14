def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}({', '.join([str(i) for i in args])})\n" \
               f"it returned {func(*args)}"
    return wrapper

@logged
def suy_func(*args):
    return 3 + len(args)


print(suy_func(4, 4, 4))