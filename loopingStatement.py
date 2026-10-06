# #while loop
#
# # #print numbers 1to 100
# # i=1
# # while(i<=100):
# #     print(i)
# #     i=i+1
# #
# # #print numbers 100 to 200
# # u=100
# # while(u<=200):
# #     print(u)
# #     u=u+1
# #
# # #print numbers 1,3,5,7,9,11,13,15
# # i=1
# # while i<=15:
# #     print(i)
# #     i+=2
# #
# # #2,,4,6,8,10
# # e=2
# # while(e<=10):
# #     print(e)
# #     e=e+2
# #
# # #1,4,7,10,13,16
# i=1
# while i<17:
#     print(i)
#     i+=3
# #
# # #10,20,30....,80
# u=10
# while u<81:
#     print(u)
#     u+=10
#
# #3,6,9,12,15,18,21
# o=3
# while(o<=21):
#     print(o)
#     o=o+3
#
# #5,4,3,2,1
# t=5
# while(t>=1):
#     print(t)
#     t-=1
#
# #8,6,4,2,0
# p=8
# while(p>=0):
#     print(p)
#     p-=2
#
# #print all 4 digit numbers(1000-9999)
# m=1000
# while(m<=9999):
#     print(m)
#     m+=1
#
# #print the 3 digit numbers that are divisible by 3
#
# b=100
# while(b<=999):
#     if(b%3==0):
#         print(b)
#     b+=1
#
# #print those 4 digit numbers that contains digit 3
#
# z=1000
#
# while(z<=9999):
#     z=str(z)
#     if('3' in z):
#         print(z)
#     z=int(z)+1
#
# #print those numbers that are divisible by 3 and 5 in the range (1,100)
# e=1
#
# while(e<=100):
#     if(e%3==0 and e%5==0):
#         print(e)
#     e+=1
#
# #print 1,4,9,16,25,36,49,64,81,100
#
# y=1
# while(y<=10):
#         print(y**2)
#         y+=1

# count=0
# x=100
#
# while(x<=999):
#     if('3' in str(x)):
#         print(x)
#         count+=1
#     x+=1
# print(count)

# l=200
# count=0
# while(l<=300):
#     if(l%7==0 or l%3==0):
#         print(l)
#         count+=1
#     l+=1
# print(count)

# n=1
# count=0
#
# while(n<=100):
#     if(n%2!=0 and n%5==0):
#          count+=1
#     n+=1
# print(count)

#count of all palindrome  numbers upto 1 to 1000 (HW)
# i=1
# count=0
# while(i<=1000):
#     if str(i)==str(i)[::-1]:
#         count+=1
#     i+=1
# print(count)

#count of those numbers that are divisible by 3 in the range of (1,50)

# i=1
# count=0
#
# while(i<=50):
#     if(i%3==0):
#
#         count+=1
#     i+=1
# print(count)


i=100
count=0
while i<=200:
    count+=1
    i+=1
print(count)