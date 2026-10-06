#sum of list
l=[1,2,3,4]
import functools
print(functools.reduce(lambda a,b:a+b,l,0))

#product of the given list
print(functools.reduce(lambda a,b:a*b,l,1))
