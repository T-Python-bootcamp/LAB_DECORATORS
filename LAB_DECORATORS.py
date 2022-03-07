def my_decorator(param):
    print("string")
    return param

def my_func(x:str):
    if len(x) >=5:
      print(" is more than 5 ")
    else:
        print("should have more than 5 characters ")

decorated_func = my_decorator(my_func)
decorated_func("jj")

