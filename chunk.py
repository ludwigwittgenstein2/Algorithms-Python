import timeit

def costly_func():
        return map(lambda x: x^2, range(10))

l = timeit.timeit(costly_func)
