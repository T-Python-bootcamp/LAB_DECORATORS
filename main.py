
def my_decorators(param):
    print("check validation")
    return param



@my_decorators
def check(x):
    if type(x) == str and len(x) > 5:
        print(f"the argument {x} checks the requirements")
    else:
        raise ValueError("the argument should be str and it should have more than 5 characters.")


check("hello")
