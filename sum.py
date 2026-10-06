# # #sum of series 1,2,3,4,5
# sum=0
# i=1
# while(i<=5):
#     sum+=i #0+1,1+2,1+3
#     i+=1 #1,3,5,
# print(sum)
# #
# # #print the sum of numbers that are divisible by 3 in the range of (1,50)
# sum=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         sum+=i
#     i+=1
# print(sum)
# #
# # #print the sum of three digit numbers
# sum=0
# i=100
# while(i<=999):
#     sum+=i
#     i+=1
# print(sum)
# #
# #print the sum of first 10digit number(2,4,6,8,10,12,14,16,18,20)
# sum=0
# i=2
# while(i<=20):
#     sum+=i
#     i+=2
# print(sum)
# #
# #print the product of first five numbers (1,2,3,4,5)
# product=1
# i=1
# while(i<=5):
#     product*=i
#     i+=1
# print(product)
#
# #print the product of first 10 odd numbers(1,3,5,7,9,11,13,15,17,19)
# i=1
# product=1
# while(i<=19):
#     if(i%2!=0):
#         product*=i
#     i+=2
# print(product)
#
# #product of numbers that contains 3 in the range (1,50)
# product=1
# i=1
# while(i<=50):
#     if('3'in str(i)):
#         product*=i
#     i+=1
# print(product)
#
# #Factorial of a number
# num=int(input('Enter a number'))
#
# i=1
# fact=1
# while(i<=num):
#     fact*=i
#     i+=1
# print(fact)

#multiplication table of a number
num=int(input('Enter a number'))
i=1

while(i<=10):
    print(num,'*',i,'=',num*i)
    i+=1


