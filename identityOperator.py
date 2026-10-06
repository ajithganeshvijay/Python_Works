x=23
print(id(x))

y=25
print(id(y))

print(id(x) is (y))
# returns true : both the variables x&y addresses are same

print(type(x))
# returns the type of x