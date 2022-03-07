
def check_str(func):
    def wrapper(param):
        if isinstance(param,str):
            print("The argument is string.")
        else:
            raise ValueError("the argument should be str")
        return func(param)
    return wrapper

@check_str
def check_length(param):
    if len(param) > 5:
        print("The argument is more than 5 characters.")
    else:
        raise ValueError("the argument should have more than 5 characters.")

check_length("85klwdm")