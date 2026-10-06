# #
# s='hello'
# for i in s:
#     if(i=='l'):
#         break
#     print(i)
# # #given a list
colors=['red','green','blue','yellow','black','orange']
# #print each color
for i in colors:
    print(i)
#print the first color starting with 'b'
for i in colors:
    if(i[0]=='b'):
        print(i)
        break
# #print all colors except color starting with 'b'
for i in colors:
    if(i[0]!='b'):
        print(i)
        continue
#print the first color contains letter 'n'
for i in colors:
    if('n' in i):
        print(i)
        break

#print all colors except color contains letter 'n'
for i in colors:
    if('n'not in i):
        print(i)
        continue

#

