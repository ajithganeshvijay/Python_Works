#positional(normally)
def fun(n,a):
    print('name',n)
    print('age',a)

fun('ajith',26)

#keyword
def function(n,a):
    print('name',n)
    print('age',a)

function(a=12,n='ajith')

#default
def default(n,a=23):

    print('name',n)
    print('age',a)
default(n='ajith')

#arbitary arguments

#1. possition type(non keyword)
def fun(*args):
    print(args)
fun(1,2,3,'Ajith',5)

#2. Keyword type(**kwargs)
def function(**kwargs):
    print(kwargs)

function(name='ajith',age=24,place='ktm',course='python')

#define a funtion that accepts any numbers  of numbers and return their sum

def sum(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum(1,2,3,4))