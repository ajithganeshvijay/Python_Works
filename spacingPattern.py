#print the given pattern
#       *
#     * *
#   * * *
# * * * *
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1): #loop for extra spacing in each line
#         print("",end=' ')
#
#     k=k-2
#
#     for j in range(1,i+1):#loop for printing * in each line
#         print('*',end=' ')
#     print()
#
# # #print a pyramid pattern
# #       *
# #     *   *
# #   *   *   *
# # *   *   *   *
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1): #loop for extra spacing in each line
#         print("",end=' ')
#
#     k=k-2
#
#     for j in range(1,i+1):#loop for printing * in each line
#         print('*',end='   ')#leave a double space in between the empty string
#     print()
#
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print("",end=" ")
#
#     k=k-2
#
#     for j in range(1,i+1):
#         print('*',end="   ")
#     print()
# #print the given pattern
# # *   *   *   *
# #   *   *   *
# #     *   *
# #       *
# k=0
# for i in range(5,1,-1):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k+=2
#     for j in range(1,i):
#         print('*',end="   ")
#     print()


#home_work
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
k=0
for i in range(1,5):
    for p in range(1,k+1):
        print("",end=" ")
    k=k-2
    for j in range(1,i+1):
        print("*",end=" ")
    print()
k=0
for i in range(3,0,-1):
    for p in range(k-1):
        print("",end=" ")
    k=k-2
    for j in range(1,i+1):
        print('*',end=" ")
    print()
#       *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print("",end=" ")

    k=k-2

    for j in range(1,i+1):
        print('*',end="   ")
    print()
k=0
for i in range(4,1,-1):
    for p in range(k+2):
        print("",end=" ")
    k+=2
    for j in range(1,i):
        print('*',end="   ")
    print()

#    **
#    **
#   ****
#   ****
#  ******
#  ******
# ********
# ********

k=6
for i in range(2,9,2):
    for j in range(2):
        for p in range(1,k+1):
            print(' ',end='')
        for q in range(1,i+1):
            print('* ',end='')
        print()
    k-=2
