def my_decorator(param):
    def wrapped(string):
        print("check the string")
        return param(string)
    return wrapped
    


@my_decorator
def checkstring(string):
    if type(string)==str and len(string)>5:
        print(f"the string is{string}")
        return string
    raise Exception("the argument should be str and it should have more than 5 characters")

checkstring("saraaaa")

        

