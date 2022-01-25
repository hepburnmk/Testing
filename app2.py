'''course = "Python for beginners"
print(course.upper())
print(course.lower())
print(course.find("P"))
print(course.find("n"))
print(course.replace("for", "4"))
print(course)
print("for" in course)
print("end" in course)

print(10 ** 3)

temperature = int(input("What is the temperature? "))

if temperature < 20:
    print ("Put on a jacket")
elif temperature < 15:
    print("It's ok")
elif temperature > 20:
    print("yummy mummy")'''

weight = float(input("Weight: "))
unit = input("Lbs or Kgs?: ")
if unit.upper() == "k":
    converted = (weight / 0.45)
    print("Your weight in Lbs is" + str(converted))
else:
    converted = (weight * 0.45)
    print("Weight in Kgs: " + str(converted))

