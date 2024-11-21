from functools import wraps

def cache(func):
    """
    Декоратор для кэширования результатов вызова функции.
    """
    cache_dict = {}
    
    @wraps(func)
    def wrapper(*args):
        # Преобразуем все аргументы в кортеж для их использования в качестве ключа
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result
            
    return wrapper

@cache
def fibonacci(n):
    """
    Функция для вычисления n-го числа Фибоначчи.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
