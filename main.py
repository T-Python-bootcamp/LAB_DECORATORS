

def first_fuc(param):
    print("the param is paramiter")
    return param


@first_fuc
def my_decorator2(param):
    def wrapped(*args):
        # do some operations
        print("some operation is done")
        return param(*args,)

    return wrapped


@my_decorator2
def calculate(*args):
    for x in args:
        if type(x) == str and len(x) >= 5:
            print(" the conditon is done!")
            return x
        else:
            print("not!")


calculate(234578)


# def my_decorator2(param):
#     def wrapped(*args,):
#         for args in args:
#             if type *args== str and len>=5:
#                 print(" conditon is done")
#         return param(*args)
#         raise "conditon is nit done"

#     return wrapped
# def func(*args):
#     for arg in args:
#         if type * args[arg] == str and (len(args) >= 5):
#             print("done")
#             return args
#         else:
#             raise
#             print("Condition not met")


# func(22):
