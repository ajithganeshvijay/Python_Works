#
# num=int(input('enter a number'))
#
# if(num>0):
#
#     if(num%2==0):
#         print('num is possitive even')
#     else:
#         print('num is possitive odd num')
#
# else:
#
#     if(num%2==0):
#         print('num is negative even')
#     else:
#         print('num is negative odd')

# #
# num=int(input('enter a number'))
# if(num%2==0):
#     if(num%3==0):
#         print('is divisible by 2 and 3')
#     else:
#         print('is divisible by 2 and not by 3')
# elif(num%3==0):
#     print('number is divisible by 3 and not by 2')
# else:
#     print('not divisible by 2 and 3')

# 1
# 2 3
# 4 5 6
# 7 8 9 10
k=1
for i in range(1,5):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()

