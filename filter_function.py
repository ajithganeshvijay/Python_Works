#filter the even elements from the given list
l=[1,2,3,4,5,6,7,8,9,10]
print(filter(lambda x:x%2==0,l))
print(list(filter(lambda x:x%2==0,l)))
#given a list
l1=[23,67,90,12,45,52]
#number greater than 50
print(list(filter(lambda x:x>50,l1)))
#given a list of fruits
f=['apple','orange','grapes','pineapple']
#fruit name whose length is >5
print(list(filter(lambda x:len(x)>5,f)))
#number divisble by 3&5
l2=[34,78,96,23,12,15]
print(list(filter(lambda x:x%3==0 and x%5==0,l2)))
