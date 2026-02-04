import time

def timer(function):
    def warapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__} run in {int(end - start)} second time")
        return result
    return warapper

@timer
def example_function(n):
    time.sleep(n)

example_function(5)    

