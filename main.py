def my_decorator(*args):
    def wrapped(param):
        print("some operation is done")
        if type(param) == str and len(param) > 5:
            return param
        raise ValueError('argument should be a string with more than 5 charaters')
    
    return wrapped
@my_decorator
def check(x):
    return x

print(check("hello0"))