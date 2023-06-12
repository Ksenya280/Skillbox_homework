def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'Функция {func.__name__} была вызвана {wrapper.count} раз.')
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@counter
def foo():
    print('Вызов функции foo')


foo()
foo()
foo()

