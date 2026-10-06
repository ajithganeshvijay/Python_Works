#check whether the maximum of three numbers:

a=int(input('enter a number'))
b=int(input('enter a number'))
c=int(input('enter a number'))
d=int(input('enter a number'))

if(a>b and a>c and a>d):
    print('First number is the largest')
elif(b>a and b>c and b>d):
    print('Second number is the largest')
elif(c>a and c>b and c>d):
    print('Third number is the largest')
else:
    print('Fourth number is the largest')


