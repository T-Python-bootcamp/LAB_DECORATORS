def myFunc(func):
    def wrapped(parm1):
        print("string")
        return func(parm1)  
    return wrapped


@myFunc
def string(parm:str):
   if len(parm) >5:
      print(" string is more than 5 characters")
   else:
      print("string should have more than 5 characters ")


string("jamela") 
