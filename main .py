# age = int(input("Enter your age: "))
#
# if age <= 0 or age > 120:
#     print("You entered wrong number!")
# elif age <= 18:
#     print("You should study.")
# elif age <= 50:
#     print("You should work.")
# elif age <= 59:
#     print("You will retire soon")
# elif age < 90:
#     print("You are pensioner")
# else:
#     print("You have been living long!")

# month_num = int(input("Enter month: "))
# months = {
#     1: ["Janaury", 31],
#     2: ["February", 28],
#     3: ["March", 31],
#     4: ["Aprel", 30],
#     5: ["May", 31],
#     6: ["June", 30],
#     7: ["July", 31],
#     8: ["August", 31],
#     9: ["Septemer", 30],
#     10: ["October", 31],
#     11: ["Novamber", 30],
#     12: ["December", 31]
# }
#
# if 1 <= month_num <= 12:
#     month_info = months[month_num]
#     print(f"Month: {month_info[0]}. Days: {month_info[1]}.")
# else:
#     print("Error!")


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# count = 0
# if num1 == num2 == num3:
#     count = 3
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     count = 2
#
# print(f"Same number: {count}")


# num1 = int(input("Enter first name: "))
# num2 = int(input("Enter second name: "))
#
# if num1 * num2 <= 1000:
#     print(f"Multipication: {num1 * num2}")
# else:
#     print(f"Sum: {num1 + num2}")



# num = int(input("Enter number: "))
# print("Hello" if num % 5 == 0 else "Bye")


# year = int(input("Enter year: "))
#
# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print(f"{year} - leap year")
# else:
#     print(f"{year} - not leap year")


width = int(input("Chocolate width: "))
length = int(input("Chocolate lengh: "))
pieces = int(input("The number of bars we need: "))

if (pieces % width == 0 or pieces % length == 0) and pieces <= width * length:
    print("YES")
else:
    print("NO")
