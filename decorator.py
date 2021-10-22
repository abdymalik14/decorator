# def multiple(func):
#     print('$'*30)
#     def dec(a,b):
#         func(a,b)
#     return dec

# @multiple
# def mult(a,b):
#     print(a*b)

# mult(4,5)

def log(func):
    def inner(*args,**kwargs):
        print(f'Function <{func.__name__}> is called')
        result = func(*args,**kwargs)
        # print(result)
        return result
    return inner

@log
def add(a,b):
    return a+b
@log
def minus(a,b):
    return a-b

add(4,5)
minus(9,3)