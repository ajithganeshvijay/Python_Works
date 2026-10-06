#
# # # # Q1.Define a function that takes 2 numbers and returns their product
# # def product(a,b):
# #     p=a*b
# #     return(p)
# # result=product(3,4)
# # print(result)
# from function import result
#
# # Q2.Define a function that takes a string and returns number of vowels
# # def word(s,v):
# #     count=0
# #     for i in s:
# #         if i in v:
# #             count+=1
# #     return(count)
# # result=word('ajith','aeiouAEIOU')
# # print(result)
#
# #Q3.Define a function that takes length and breadth and returns area of
# #rectangle
#
# # def area(l,b):
# #     p=l*b
# #     return(p)
# # result=area(5,2)
# # # print('Area=',result)
# #
# # # # Q4.Define a function that takes a list of numbers and creates a new list
# # # # with even numbers and returns the new list
# # # l=[45,78,90,12,35]
# # # def list(e):
# # #     new_list=[i for i in l if i%2==0]
# # #     return(new_list)
# # # result=list(l)
# # # print(result)
# #
# # # #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # # # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]
# def list(l):
#     new=[]
#     for i in l:
#         sum=0
#         for j in str(i):
#             sum += int(j)
#         new.append(sum)
#     return new
# result=list(l)
# print(result)
#
# #
# #new=[6,12,3,21,8,17]
#
# def palindrome(s):
#     if(s[::-1]==s):
#        return s
# result=palindrome('ajith')
# print(result)
# 153 =1^3+5^3+3^3
# def amstrong(f):
#     sum = 0
#     n=str(f)
#     l=len(n)
#     for i in range(1,l):
#         sum+=int(f**l)
#         if(sum==f):
#             return f
# result=amstrong(f=153)
# print(result)

#define a function that takes a list as arguments and returns a new list containing unique elements form the list.
# l=[23,34,78,78,12,90,23]
#
# def list(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
#
# result=list(l)
# print(result)

#define a function that takes two list as arguments adn print common elements.
l1=[12,34,56,78,90]
l2=[90.34,11,57,45]

def l(a,b):
    for i in l1:
        if i in l2:
            print(i)
    return

l(l1,l2)