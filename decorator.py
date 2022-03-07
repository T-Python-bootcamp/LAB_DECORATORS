
def check_str(func):
    def wrapper(param):
        
        return func(param)
    return wrapper

@check_str
def check_length(param):
    if isinstance(param,str):
        if len(param) > 5:
            print("The argument is more than 5 characters.")
        else:
            raise ValueError("the argument should have more than 5 characters.")
    else:
        raise ValueError("the argument should be str")
    

check_length("hello!")