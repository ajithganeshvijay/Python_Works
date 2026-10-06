#1.write a program to find BMI(Body Mass Index)

# height=float(input('Enter your height in cm'))
# weight=float(input('Enter your weight in kg'))
# BMI=weight/(height/100)**2
# if BMI <=18.4:
#     print(BMI,'under weight')
# elif BMI>=18.5 and BMI<=24.9:
#     print(BMI,'Normal')
# elif BMI>=25.0 and BMI<=39.9:
#     print(BMI,'Overweight')
# elif BMI>=30.0:
#     print(BMI,'Obse')
# else:
#     print('Enter valid data')
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
# battery_based_amount=int(input('enter the amount of battery_based toys:'))
# key_based_amount=int(input('enter the amount of key based toy:'))
# electrical_based_amount=int(input('enter the amount of electrical charging type:'))
#
# # The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# if battery_based_amount>1000:
#     code=int(input('enter the code:'))
#     print(battery_based_amount*(10/100),'rupees has been discounted for battery based toys and total bill is rupees',battery_based_amount-battery_based_amount*(10/100))
# # On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,
# if key_based_amount>100:
#     code = int(input('enter the code:'))
#     print(key_based_amount*(5/100),'having 5% of discount for battery based toys')
# # and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.
# if electrical_based_amount>500:
#     code = int(input('enter the code:'))
#     print(electrical_based_amount*(10/100),'having 10% of discount for electrical charging toys')
# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

#3 FIZZBUZZ Problem

num=int(input('enter a number'))
# if divisible by 3 only -print fizz
# if num%3==0:
#     if num%5==0:
#         print('fizz buzz')
#     else:
#         print('fizz')
# else:
#     if num%5==0:
#         print('buzz')
#     else:
#         print(num)
# if divisible by 5 only -print buzz

# if a number is divisible by 3 and 5

#     print fizz buzz
#     otherwise -print the number

