name = "vishu"
letter = [n for n in name]

new = [number*2 for number in range(1,5)]

print(letter)
print(new)

list = [num for num in range(1, 10) if num%2 == 0]
print(list)

import random

students = ['alex', 'bravo', 'enzo', 'redo']
student_marks = {student: random.randint(80,100) for student in students}
print(student_marks)

passed_students = {student:marks for (student, marks) in student_marks.items() if marks >85}
print(passed_students)

import pandas as pd
df = pd.DataFrame({
    "Name": (student_marks.keys()),
    "Marks": (student_marks.values())
})
print(df)

for (index, row) in df.iterrows():
    print(row.Name)




