dictionary={
    "Bug":"An Error in the Program",
    "Function":"Piece of code that can be call over and over again.",
    "Loop":"Repeatable code",
}
# print(dictionary["Bug" ])
studentsScore={
    "Qasim":98,
    "Umar":78,
    "Talha":85,
    "Zahoor":75
}
studentsGrade={}
for student in studentsScore:
    score=studentsScore[student]
    if score>=91 and score <=100:
        studentsGrade[student]="Outstanding"
    elif score >=80 and score <=90:
        studentsGrade[student]="Exceeds Exceptions"
    elif score >=71 and score <=80:
        studentsGrade[student]="Acceptable"
    else:
        studentsGrade[student]="Fail"
# print(studentsScore)
# print(studentsGrade)
travelLog={
    "Punjab":['Faisalabad','Narowal','Lahore','Sialkot','Shakargarh','Shekhupura'],
    "Sindh":{'Karachi':['Korangi','Malir','Liyari','Kharadar','chamra chorangi','tin talwar'],'Haiderabad':'Saylani Office'}
}
dictInList=[
    {
        'Name':'Zahoor Ahmad',
        'AG':'2021-ag-7754',
        'Section':'B'
    },
    {
        'Name':'Muhammad Talha',
        'AG':'2021-ag-7784',
        'Section':'B'
    },
]
print(dictInList)
# print(travelLog)
n=int(input('How many entities you want to add: '))
def addingEntities(name,ag,sec):
    newEntity={
        'Name':name,
        'AG':ag,
        'Section':sec
    }
    dictInList.append(newEntity)
for _ in range(n):
    name=input('Enter Your Name: ')
    ag=input('Enter your AG like "2021-ag-0000" :')
    sec=input('Your Section name please: ')
    addingEntities(name,ag,sec)
print(dictInList)