def myfunc(a):
    from Bookie1 import myBookie1
    print('Hi there')
    b = myBookie1(a)
    if b == 'Tipico':
        return 'Tipicoooo'
    else:
        return 'F'
    

# choose correct function
#def chooser(bookie_name, **args):
#    if bookie_name == 'Tipico':
#        return func_tipico(**args)
#    ...



