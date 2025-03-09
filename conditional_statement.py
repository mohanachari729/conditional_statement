#vowel
char = input("Enter a character ")
vowel= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if char in vowel:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")





# Age Group Classification
age = int(input("Enter age"))

if age <= 0:
    print(f"{age} is an invalid input")
elif age <= 13:
    print(f"{age} belongs to Child")
elif age <= 18:
    print(f"{age} belongs to Teenager")
elif age <= 65:
    print(f"{age} belongs to Adult")
else:
    print(f"{age} belongs to Senior")



#Number Classifier:

number = int(input("Enter any number"))

if number < 0:
    print(f"{number} is negative number")
elif number > 0:
    print(f"{number} is positive number")
else:
    print(f"{number} is zero")



# Leap Year Checker

year = int(input("Enter a year"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")


    
# Discount Calculator

price = float(input("Enter the price"))
discount = float(input("Enter the discount"))

discount_amount = (discount / 100) * price

final_price = price - discount

print(f"final price after discount is {final_price}")



# BMI Calculator

weight = float(input("Enter your weight in kg"))
height = float(input("Enter your height in meters"))

bmi = weight / (height ** 2)

print(f'your BMI is {bmi}')