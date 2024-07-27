def time_wrapper(function):
    import time

    def wrapper(*args, **kwargs):
        start = round(time.time() * 1000)
        result = function(*args, **kwargs)
        end = round(time.time() * 1000)
        print(f'Running time: {end-start} ms')
        return result
    return wrapper
