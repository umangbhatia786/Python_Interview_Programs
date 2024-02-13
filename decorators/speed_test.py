from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print(f'Time elapsed: {end_time-start_time}')
        return result
    return wrapper


@speed_test
def sum_nums():
    return sum(val for val in range(10000))
    

print(sum_nums())