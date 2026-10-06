# # # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# for i in range(1,101):
#     if(i%3==0 or i%5==0):
#         print(i)
#
# # # 2.Print the cumulative sum of a list.
# # # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
# sum=0
# for i in range(1,5):
#     print(i)
#     sum+=i
from unittest import skip

# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
# sum=0
# for i in range(3,8):
#     sum+=i
# print(sum)

## 4.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90
# 5.Given a list, sum the elements until a 0 is encountered (stop at 0).
# l=[4,9,1,0,6,7]
# sum=0
# for i in l:
#     if(i==0):
#         break
#     else:
#             i+=1
#     print(i)

# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# for i in range(1,1001):
#     if(i%7==0 and i%11==0):
#         print(i)
#         break

# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.

# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]
# l=[1,2,3]
# new=[]
# for i in range(1,4):
#     new.append(i**2)
# print(l,'=',new)

# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
# s='hello world'
# new=''
# for i in s:
#     if(i in 'aeiouAIOU'):
#             continue
#     else:
#         print(i,end='')
#         continue

# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# l=[5,2,8,6,2]
# new=[]
# for i in l
#     if(i**2>50):
#         break
# else:
#     print(new.append(i**2))

# 11.From a string containing mixed characters, create a new string containing only digits.
# i: "abc123x7z" → Output: "1237"

s="abc123x7z"
new=""
for i in s:
    if("1237" in i):
        print(new)





