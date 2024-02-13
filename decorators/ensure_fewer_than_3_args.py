from functools import wraps

class ArgsCountError(Exception):
    pass

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        else:
            raise ArgsCountError('More than 2 arguments are not allowed!')
    return wrapper
    

@ensure_fewer_than_three_args
def greet(first, last):
    return f'Hello {first} {last}'

@ensure_fewer_than_three_args
def intro(first, last, age):
    return f'Name is {first} {last} with age as {age}'

print(intro('Umang', 'Bhatia', 29))