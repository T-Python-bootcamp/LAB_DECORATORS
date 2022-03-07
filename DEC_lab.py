
def decorator1 (any):
  def wrapped(decor):
       print("Your opretions is Done !")
       return any(decor)

  return wrapped 

@decorator1
def decorator2 (param):
    if type(param) == str and len(param) > 5:
        return param
    raise ValueError("please add value more than 5")

decorator2("Great") 