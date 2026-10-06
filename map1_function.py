#creat a new list of having square of the given list
l=[1,2,3,4]

print(map(lambda x:x**2,l))
print(list(map(lambda x:x**2,l)))

#create a new list of cubes of same list given above

print(list(map(lambda y:y**3,l)))

#create a new list of square root of given list
l2=[25,36,81,100]
print(list(map(lambda y:y**0.5,l2)))

#create a new list of length
colors=['red','green','blue','yellow','black']
print(list(map(lambda x:len(x),colors)))

#create a new list of first chara
print(list(map(lambda x:x[0],colors)))

#create a new list of last chara
print(list(map(lambda x:x[-1],colors)))

#create a new list of reverese of the elements
print(list(map(lambda x:x[::-1],colors)))

#given a list=[23,78,12,,56]
l=[23,78,12,56]
print(list(map(lambda x:x+10,l)))

##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
{'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
{'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# # create a new list of emails
print(list(map(lambda x:x['email'],l)))