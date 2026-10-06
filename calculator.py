
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mlt(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input('enter a number'))
b=int(input('enter another number'))
while(1):
    print('Choose the operation')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Exit')

    choice=int(input('enter your choice'))
    if choice==1:
        print(add(a,b))
        break
    elif choice==2:
        print(sub(a,b))
        break
    elif choice==3:
        print(mlt(a,b))
        break
    elif choice==4:
        print(div(a,b))
        break
    else:
        exit()