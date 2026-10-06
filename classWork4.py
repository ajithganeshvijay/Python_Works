# #1.Write a program to check whether two entered numbers are equal or not
# num1=int(input('Enter a number'))
# num2=int(input('enter another number'))
# if num1==num2:
#     print(num1,num2,'are equal')
# else:
#     print(num1,num2,'are not equal')

#2.Write a program to check whether two entered words are equal or not
# a=input('enter the words')
# b=input('enter another word')
# if(a==b):
#     print('a and b are equal')
# else:
#     print('a and b are not equal')

#3.Write a program to find the maximum of two numbers
# num1=int(input('enter a number'))
# num2=int(input('enter another number'))
# if num1>num2:
#     print(num1,"is greater than",num2)
# else:
#     print(num2,'is greater than',num1)

#4.write a program to check whether the entered character is vowel or not
# w=input('enter a character')
# vowels='aeiouAEIOU'
# if(w in vowels):
#     print('character is a vowel')
# else:
#     print('character didn't have vowel')

#5.Write a program to check whether the entered country name contains word 'land'
# country=input('enter the name of country')
# if('land' in country):
#     print('having word land')
# else:
#     print('not having land')

#6.write a program to check whether the entered number is 3 digit or not
# num=int(input('enter a number'))
# if(num>99 and num<=999):
#     print('this is three digit number')
# else:
#     print('this is not a three digit number')

#7.write a program to check whether the entered string is  palindrome or not
# p=input('enter any words')
# if(p==p[::-1]):
#     print('this is a palindrome')
# else:
#     print('is not a palindrome')

#8.Write a program to check whether a number is present in given list
# l=[23,67,12,90]
# num=int(input('enter a number'))
# if num in l:
#     print(num,'is in the list')
# else:
#     print(num,'is not in the list')
#9.Write a program to check whether a key is present in a dictionary or not
# d={101:'Arun',102:'Amal',103:'Anu'}
# num=int(input('enter a key in number'))
# if num in d.keys():
#     print(num,'is in the dictionary')
# else:
#     print(num,'is not in the dictionary')
#10.Write a program to check whether the given password is strong/weak(if length less than 8 weak)
password=input('enter your password')
if len(password)>8:
    print('is a strong password')
    if len(password)<8:
        print('is a weak password')
else:
    print('is an invalid password')