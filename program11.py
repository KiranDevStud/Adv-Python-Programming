def increase_by_two_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 2
    return wrapper

@increase_by_two_decorator
def get_number():
    return 5

print(get_number())
