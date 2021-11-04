def c(func):
    print('c', func)
    def inner_c():
        print('cc')
        print(func)
        func()
        print('ccc')
    return inner_c

def b(func):
    print('b', func)
    def inner_b():
        print('bb')
        print(func)
        func()
        print('bbb')
    return inner_b

@c
@b  
def a():  # a=c(b(a))
    print('a')

a = a() = c(c(a))()


reversed()