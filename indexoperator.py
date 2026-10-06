#index operator
s='hello'
print(s)
print(s[-1])
print(len(s))

#slice operator
#[start index:stop index:step index]   default step index=1(increment 1)
#[0:n]  means starting from nth index to (n-1)th index

a='hello world'
print(s[0:5]) # or print(s[:5])  hello

#given a string

s='python coding is easy and fun'

#find the len of the string
print(len(s))
#find the reverse of string
print(s[::-1])
#print the first chara
print(s[0])
#print the last chara
print(s[-1])
#print the chara from the 2nd index to the 10th chara
print(s[2:9])
#print 13th chara
print(s[12])
#print 5th index chara
print(s[5])
