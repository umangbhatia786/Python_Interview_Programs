from functools import wraps

def only_ints(fn):
    """Decorator to ensure that only integer values are passed as arguments."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Wrapper function to check if all arguments are integers before calling the original function."""
        if all(type(val) == int for val in args):
            return fn(*args, **kwargs)
        raise ValueError('Non-integer values are not allowed as arguments!')
    return wrapper

@only_ints
def add(x,y):
    return x + y

print(add('Hi', 'Hello'))