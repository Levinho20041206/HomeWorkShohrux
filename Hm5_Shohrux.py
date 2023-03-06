def phone(function):
    def wrapper(*args):
        function(*args)
        num = f"+998 {function(*args)}"
        return num
    return wrapper

@phone
def add(args):
    return args
print(add("33 074 1204"))