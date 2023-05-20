# for loop
# for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# fruits = ['Apple','orange','banana', 'grapes', 'papaya']
# for fruit in fruits:
#     print(fruit)

# let's calculate the average of a series
studentsMarks=[12,23,34,45,34,24,55,23,23,27]
totalMarks=0
totalStudents=0
for student in studentsMarks:
    totalMarks+=student
    totalStudents+=1
print('Average marks are: ',(totalMarks/totalStudents))


# Now let's calculate the Maximum and minimum value
minMarks=0
maxMarks=0
for marks in studentsMarks:
    if marks > maxMarks:
        maxMarks=marks
    # minMarks=marks
print(maxMarks)