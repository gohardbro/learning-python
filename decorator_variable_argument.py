def trace(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
        
        return r
    return wrapper

@trace
def getMax(*args):
    return max(args)

@trace
def getMin(**kwargs):
    return min(kwargs.values())

print(getMax(10, 20))
print(getMin(x=10, y=20, z=30))
