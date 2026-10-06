#1.given list
l=[12,4.5,6.8,30,'arun','hello']

#print floating point numbers
for i in l:
    if(type(i)==float):
        print(i)
#print string values
for i in l:
    if(type(i)==str):
        print(i)
#print numbers
for i in l:
    if(type(i)==int):
        print(i)

#2.Gives a dictionary
d={'a':23,'b':25,'c':28,'d':30,'e':22}
#print only even values
for i in d.values():
    if(i%2==0):
        print(i)

#3.Given a list of
colors=['red','green','blue','orange','black']
#print starting letter of each color
for u in colors:
    print(list(u[0]))
#print last letter of each color
for u in colors:
    print(list(u[-1]))
#print reverse of each color
for u in colors:
    print(u[::-1])
#print all colors containing letter 'b'
for u in colors:
    if('b' in u):
        print(u)

