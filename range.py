#range

for i in range(1,6):
    print(i,end='')
print()
#
for i in range(1,12,2):
    print(i,end='')
print()
#
for i in range(2,11,2):
    print(i,end='')
print('')
#
for i in range(100,501,100):
    print(i,end='')
#
for i in range(5,0,-1):
    print(i,end='')
#
for i in range(3,22,3):
    print(i,end='')

for i in range(1,7):
    print(i**2,end='')
#
for i in range(100,999):
    if("3" in str(i)):
        print(i,end='')

for i in range(102,200,3):
    if(i%3==0):
        print(i)

for i in range(1,6):
    print(i**3,end='')


#sum of digits in a number
l=1234
sum=0
s=str(l)
for i in s:
    sum=sum+int(i)
print(sum)

t='hello'
rev=''
for i in s:
    rev=i+rev
print(rev)

s=1234
u=str(s)
rev=''
for i in u:
    rev=i+rev
print(rev)
#

#given a list
l=[1,2,3,4]
# #create a new list for showing square
new=[]
for i in l:
    new.append(i**2)
print(new)

#create a dict where keys are numbers and values are square of each number
#d={1:2,2:4,3:9,4:16}
new={}
for i in l:
    new[i]=i**2
print(new)
