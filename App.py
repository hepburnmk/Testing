print("Hello World")
# variables temporarily stores a value in memory
# age is a label, 35 is the value
age = 35
price = 19.95
# Boolean Values have a capital first letter
is_online = False
print(age)
first_name = "Megan"

# Practice
patient_name = "John Smith"
age1 = 20
new_patient = True

# Receiving input, Concatenation

name3 = input("What is your name? ")
print("Hello " + name3)
print("Hello", name3)

birth_year = int(input("What year were you born? "))
age = 2021 - birth_year
print("you are", age, "years old")

first = input("First number: ")
second = input("Second number: ")

#Covert first and second to int for sum. They stay as strings re: above

sum = int(first) + int(second)
print("the sum is " + str(sum))

#Convert variable to float at input point.

third = float(input("Third number: "))
fourth = float(input("fourth number: "))
new_sum = sum + third + fourth

print("the new sum is: " + str(new_sum))
