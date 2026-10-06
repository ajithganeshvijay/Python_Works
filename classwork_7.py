# # # #create a new list with square root of each element
# l=[25,16,9,36]
# new_list=[i**0.5 for i in l ]
# print(new_list)
#
# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # new_dict=[i for i in d]
# # print(new_dict)
# # # create a list of names
# # # create a list of marks
# new_dict=[i for i in d.values()]
# print(new_dict)
#
# #Given a list
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# # #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)
# # #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)
# #create a list of positive numbers
# # new=[i for i in l if(type(i)==int or type(i)==float) and i>0]
# # print(new)
#
# #
# # #Given a list
fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
new=[i for i in fruits if len(i)>6]
print(new)
# # #create a new list with elements whose value is divisible by 3 in range(1,101)
new=[i for i in range(1,102) if i%3==0]
print(new)
# # Given
s="python coding is easy and fun"
# # create a new list with only vowels
v='aeiou'
# new_list=[i for i in s if i in v]
# print(new_list)
new_set={i for i in s if i in v}
print(new_set)
