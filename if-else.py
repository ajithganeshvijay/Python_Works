#if-else statement\
#print the number whether is possitive or negative
num=int(input('enter a number'))
if num>0:
    print(num,'is a positive number')
else:
    print(num,'is a negative number')
#print the number whether it is odd or even
if num>0 and num%2==0:
    print(num,'is an even number')
    if num>0 and num%2!=0:
        print(num,'is an odd number')
else:
    print(num,'is neither an even nor an odd possitivenumber')