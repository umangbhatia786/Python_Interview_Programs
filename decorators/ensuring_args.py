from functools import wraps

def ensure_no_kwrgs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No kwargs are allowed!')
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_kwrgs
def greet(first, last):
    return f'Hello {first} {last}'

print(greet('Umang', 'Bhatia'))
print(greet(first='Umang',last='Bhatia'))