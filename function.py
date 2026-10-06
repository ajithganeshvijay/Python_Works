# # function:is a block of statements used to perform an operation or task.
# #syntax
# #def functionname(parameters):
#     # "function doct
# # ring"
#     # fuction body
#     # return(expression)
#
#
# def addition(): #function definition
#     "addition of two numbers" #function doctring
#     num1=int(input('enter a number')) #function body
#     num2=int(input('enter another number')) #function body
#     sum=num1+num2 #function body
#     print(sum)
#     return
# addition()  #function call
# #1
# def name():
#     "display name"
#     s='hello name'
#     print(s)
#     return
# name()
# #2
# def factorial():
#     'factorial of a number'
#     num=int(input('enter a number'))
#     for i in range(num-1,0,-1):
#         num*=i
#     print(num)
#     return
# factorial()
from itertools import product


#3
# def occurance():
#     'occurance of a number'
# a=input('enter a name')
# cha=input('enter a character')
#        if i==cha:
#                                             count+=1
#      print(count)
#      return
# occurance()

# #define a function to check a whether a number is prime or not
def prime():
    'cecking prime number'
    num=int(input('enter a number'))
    for i in range(2,num):
        if(num%i==0):
            print('is not a prime')
            break
    else:
        print('prime')
        return
prime()

#find the simple interest
# def interest(p,n,r):
#     si=p*n*r/100
#     # print(si)
#     return si
# p=int(input('enter the amount'))
# n=int(input('enter the year'))
# r=int(input('enter the rate'))
#
# result=interest(p,n,r)
# print(result)

#define the funtion that 3 numbers and return the product of 3 numbers
# def num(num1,num2,num3):
#     product=num1*num2*num3
#     return product
# result=num(3,2,3)
# print(result)

#define a function that takes a string and chara and return the numbers of occurance of the chara in thet string
# def word(s,c):
#     count=0
#     for i in s:
#         if i==c:
#             count+=1
#
#     return(count)
# result=word('ajith','j')
# print(result)



l1=[12,34,56,78,90]
l2=[90.34,11,57,45]

def l(a,b):
    for i in l1:
        if i in l2:
            print(i)
    return

l(l1,l2)