def decorator(func):
    def wrapper_sum(*args,**kwargs):
        print("The sum of",*args,"is:")
        value=func(*args,**kwargs)
        print("The sum is printed")
        return value
    return wrapper_sum

@decorator
def sumNumbers(*args):
    s=0
    for i in args:
        s+=i
    print(s)
    return s

sumNumbers(3,7,9,4)
