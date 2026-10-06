# # #find the max and min from the given list
# # l=[23,78,45,70,12,56]
# # max=l[0]
# # for i in l:
# #     if i>max:
# #         max=i
# #         print(max)
# # min=l[0]
# # for i in l:
# #     if i<min:
# #         min=i
# #         print(min)
#
# #fibinocci series
# # n=int(input('enter the value'))
# # a,b=0,1
# # for i in range(n):
# #     print(a,end='')
# #     a,b=b,a+b
#
# #find the number is prime or not (condition for prime is factors are (one and same number)
# # num=11
# # if num==0 or num==1:
# #     print(num,'is not a prime number')
# # elif num>1:
# #     for i in range(2,num):
# #         if num%i==0:
# #             print(num,'is not a prime number')
# #             break
# #     else:
# #         print(num,'is a prime number')
#
# #factorial of a number
# # num=7
# # product=1
# # for i in range(num,0,-1):
# #     product=product*i
# # print('factorial of',num,'=',product)
#
# #capitalize all names in a list
# # names=['alin','arun','anu']
# # print(list(map(lambda x:x.capitalize(),names)))
# #
# # # 2.Append "@gmail.com" to a list of usernames
# # users = ['user1', 'user2']
# # print(list(map(lambda x:x+'@gmail.com',users)))
#
# # 11.
# # p= [{'name':'laptop','price':50000},
# #     {'name':'phone','price':20000},
# #     {'name':'watch','price':3000},
# #     {'name':'Tablet','price':25000}]
#
# #print list of product names in Uppercase
# # print(list(map(lambda x:x['name'].capitalize(),p)))
# # #print products with price greater than 10000
# # print(list(filter(lambda x:x['price']>10000,p)))
# # #Find the total price of all products
# # import functools
# # u=list(map(lambda x:x['price'],p))
# # print(functools.reduce(lambda x,y:x+y,u))
#
# # Q1.Define a function that takes 2 numbers and returns their product
#
# # def product(a,b):
# #     return a*b
# # print(product(100,2))
#
# # # Q4.Define a function that takes a list of numbers and creates a new list
# # # with even numbers and returns the new list
# # l=[45,78,90,12,35]
# #
# # def new(e):
# #     new_list=[i for i in l if i%2==0]
# #     return(new_list)
# # print(new(l))
#
#
# # #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # # each value is the sum of digits of corresponding number in the original list.
# l=[123, 345, 111, 678, 134, 809]
# # new=[6,12,3,21,8,17]
#
# # def new(a):
# sum=0
# for i in l:
#     sum += i
# print(sum)

#
# Given a list of integers num_list containing numbers from 1 to N. The list should contain each number exactly once, but:
#
#
# One number is repeated twice.
#
# One number is missing.
#
#
# Write a Python function to:
#
#
# 1.Identify the repeated number.
#
# 2.Identify the missing number.
#
# 3.Calculate and return the sum of the repeated and missing numbers.
#
#
# Example
#
# num_list = [1, 1, 3, 4]
#
#
# Output:
#
# Repeated number: 1
#
# Missing number: 2
#
# Sum: 3



# def num(numlist):
#     repeated=0
#     missing=0
#     for i in range(1,max(numlist)+1):
#         if numlist.count(i)>1:
#             repeated=i
#         if numlist.counting(i)==0:
#             missing=i
#             break
#     sum=repeated+missing
#     print(sum)
# num([1,1,3,4])

# def strong_num(num):
#     import math
#     s=str(num)
#     sum=0
#     for i in s:
#         u=int(i)
#         f=math.factorial(u)
#         sum+=f
#
#     if sum!=num:
#         return False
#     else:
#         print(num,'is strong number')
#         return True
#
# print(strong_num(40845))

# a=5
# b=2
# c=a+b*3
# print(c)

s=set('Banana')
print(len(s))


