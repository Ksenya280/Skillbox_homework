import time

def slow_down(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@slow_down(2)
def some_function():
    print('Эта функция замедляется на 2 секунды')

some_function()
