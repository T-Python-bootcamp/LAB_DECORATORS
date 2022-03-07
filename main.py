
error_message1 = 'VALUE MUST BE OF TYPE STRING';
error_message2 = 'STRING MUST BE LONGER THAN FIVE LETTERS'

def myDecorator(params):
    def wrapper(arg):
        if type(arg) is not str:
            raise TypeError(error_message1)
        if len(arg)<6:
            raise ValueError(error_message2)
        return params(arg)
    return wrapper

@myDecorator
def main_func(param):
    print('Param:',param)
    
main_func('python is fu')
main_func('Hi')
main_func(1)
