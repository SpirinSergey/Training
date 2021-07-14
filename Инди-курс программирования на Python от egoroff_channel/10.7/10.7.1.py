"""
Напишите программу, которая отсортирует список subject_marks по возрастаю оценок.
Затем распечатайте предметы и оценки, каждый пару на новой строчке через пробел
"""

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]

for el in sorted(subject_marks, key= lambda x: x[1]):
    print(*el)
