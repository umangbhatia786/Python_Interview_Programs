from functools import wraps

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0]!=val:
                raise ValueError(f'First argument needs to be {val}')
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is(10)
def add(x,y):
    return x + y

print(add(5,6))