#Dictionary type:data will store as a key values pair

d={'name':'ajith','age':27,'place':'KTM'} #name,age,palce are keys and ajith,KTM,27 are values
print(d)
print(d['name'])
print(d['place'])
d['age']=26 #age updated
d['course']='Python django' #a new course added
print(d)

print(d.values()) # finding out he values from dictionary
print(d.keys())# finding out he keys from dictionary
print(d.items())# finding out both the key and values as tuple from dictionary
#to read a value from the dictionary we can use
#dictName[key]
#to update / add a new value
#dictname[key]=value


#1 given list
l1=[12,45,23,67]
print(l1[1])

#2 given list
l=[['arun',30],['amal',24],['anu',12]]
#print second element
print(l[1])
#print the second name
print(l[1][0])

#3 given list
l2={101:['arun',23,'ekm'],102:['amal',25,'tvm']}
#print the second element
print(l2[102])
#print the second name
print(l2[102][0])
