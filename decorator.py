
def check_str(func):
    def wrapper(param):
        if isinstance(param,str):
            if len(param) > 5:
                return func(param)
            else:
                raise ValueError("the argument should have more than 5 characters.")
        else:
            raise ValueError("the argument should be str.")
        
    return wrapper

@check_str
def check_length(param):
    print(f"[{param}] is validated!")
    

check_length("Hello!")