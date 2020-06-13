# def hello(name='jose'):
#     print('The hello() function has been executed!')

#     def greet():
#         return '\t this is the greet() func inside hello!'

#     def welcome():
#         return '\t This is welcome inside hello'

#     # print(greet())
#     # print(welcome())
#     # print('This is the end of the hello func!')
#     print('I am going to return a function')

#     if name=='Jose':
#         return greet
#     else:
#        return welcome

# my_new_func = hello('jose')
# def hello():
# 	return 'Hi jose'

# def other(some_def_func):
# 	print('other code runs here!')
# 	print(some_def_func())

# other(hello)


def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')

        original_func()

        print('some extra code ,after the original function')

    return wrap_func


# def func_needs_decorator():
# 	print('I want to be decorated!!')

# decorated_func=new_decorator(func_needs_decorator)

# decorated_func()

@new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()
