def foo_a(*args):
    print('args: ',type(args),args)
    print('*args: ',*args)

def foo_b(num = None,**kwargs):
    print('num = ',num,'kwargs: ',kwargs)
    if(num is not None):
        return kwargs
    print('**kwargs: ',foo_b(num = 1,**kwargs))
    print('kwargs: ',foo_b(num = 1,**kwargs))

def foo_c(**kwargs):
    print(**kwargs)

foo_a(1,2,3,[4,5,6,7,8])
#foo_b(10,11,12,[13,14,15,16])
print()
foo_b(a = 20,b = 21, c = 22 , d = [23,24,25])
print()
#var = foo_c(a = 20,b = 21, c = 22 , d = [23,24,25])
foo_c(a = 20,b = 21, c = 22 , d = [23,24,25])
#print('var: ',type(var),var)