# p3.py
# Author 3
from p1 import calculate_total
from p2 import calculate_grade
name = input("Student Name : ")
m1 = int(input("Marks 1 : "))
m2 = int(input("Marks 2 : "))
m3 = int(input("Marks 3 : "))
total = calculate_total(m1, m2, m3)
grade = calculate_grade(total)
print("\n------ Result ------")
print("Student :", name)
print("Total :", total)
print("Grade :", grade)