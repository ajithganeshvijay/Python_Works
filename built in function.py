# #built in function
# print(abs(-100))
# print(pow(2,4))
# print(max(1,2,3,4,))
# print(min(12,3,4,5,65))
# print(sum((10,23,4,5)))
# print(divmod(10,2))
#
# #math module function
# import math
# print(math.sqrt(25))
# print(math.isqrt(25))
# print(math.lcm(1,2,3))
# print(math.pow(8,2))
#
# #random module function
# import random
# print(random.random())
# print(random.randint(1,50))
# print(random.randrange(1,10,2))
# print(random.choice([1,2,3,4,54,65]))
#
# #built in function for string
# s='hello world'
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.index('l'))
# print(s.find('e'))
# print(s.count('e'))
# print('-'.join(s))
#
# a='1234h'
# print(a.isalpha())
# b='1234'
# print(b.isdigit())
# print(a.isalnum())
#
# h='hello world'
# print(h.replace('world','python'))
# print(h.isspace())
#
# #list type built in function
#
# l=[12,4,56,73,3]
# l.extend([13,5])
# print(l)
#
# l.pop(2)
# print(l)
#
# l.remove(12)
# print(l)
#
# l.insert(1,13)
# print(l)
#
# l.reverse()
# print(l)
#
# l.sort()
# print(l)
#
# l.sort(reverse=True)
# print(l)

#set type-built in function
c={1,2,3,4}
c.add(6)
print(c)
c.update((7,8,9))
print(c)
c.remove(6)
print(c)
c.discard(9)
print(c)
c.pop()
print(c)

s1={1,2,3,4}
s2=(4,5,6)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

#dictionary type built in functions
d={'a':10,'b':20}
print(d.get('b'))
d.update({'c':12,'d':56})
print(d)
print(d.pop('c'))
print(d)
print(d.popitem())
print(d)
for i,j in d.items():
    print(i,'=',j)