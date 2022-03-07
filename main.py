
def my_decorators(param):
    def wrapper(*args):
        if type(*args) == str and len(*args) > 5:
            print(f"the argument checks the requirements")
        else:
            raise ValueError("the argument should be str and it should have more than 5 characters.")
        return param(*args)
    return wrapper


@my_decorators
def check(x):
    print("check validation")


check("hello there")
# decorated_func = my_decorators(check("helloo"))
# decorated_func()
