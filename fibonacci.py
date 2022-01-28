from datetime import datetime


def timeit(n_of_calls):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            for i in range(n_of_calls):
                result = func(*args, **kwargs)
            end = datetime.now()
            delta = (end - start)/n_of_calls
            print(f'Duration: {delta.microseconds}')
            return result
        return wrapper
    return inner


def cache(func):
    _cache = {}
    def wrapper(n):
        if n not in _cache.keys():
            print(f'Adding {n} to _cache')
            _cache[n] = func(n)
        return _cache[n]
    return wrapper


@timeit(n_of_calls=1000)
@cache
def fibonacciDynamic(n):
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


# print(fibonacciDynamic(n = 1100))
# print(fibonacciDynamic(n = 1100))
# print(fibonacciDynamic(n = 1100))

