#List is mutable
l=[1,2,3]
print(l)
l[2]=10
print(l)
l.append(20)
print(l)

#Tuple is a immutable ie cant be edit after execution
t=(1,2,3)
print(t)

#declare list of 5 colors
color=['red','blue','orange','green','white']
#add a new color yellow to the lsit
color.append('yellow')
#change the second color to black
color[1]='black'
#print the updated list
print(color)
#print the second last color
print(color[-2])
#print the number of colors
print(len(color))
#print the revers of the list
print(color[::-1])