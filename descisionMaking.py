#if statement
#write a prgrm to display a number if it is even
num=int(input('enter a number'))
if num>0 and num%2==0:
    print(num,'is an even enumber')
else:
    print(num,'is an odd nmumber')

#write a program to display a name if the name contains letter 'n'
name=input('enter your name')
if 'n' in name:
    print(name)
else:
    print('enter according to the given instruction')
#print the location which contains the word 'land'
location=input('Enter your location')
if('land' in location):
    print(location)
else:
    print('enter according to the given instruction')
