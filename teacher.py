# def lastChangeTeacher(listOfNames, listOfAssign, listOfGrades):
#     names = listOfNamese
#
#     message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
#     submit before you can graduate. You're current grade is {} and can increase \
#     to {} if you submit all assignments before the due date.\n\n"
#
#     for idx in len(listOfNames):
#         name = listOfNames[idx].capitalize()
#         print(message.format(name, listOfAssign[idx], listOfGrades[idx]))
#     # write a for loop that iterates through each set of names, assignments, and grades to print each student's message
#
# testNames = ["chandler bing", "phoebe buffay", "monica geller", "ross geller"]
# testAssign = [3, 6, 0, 2]
# testGrades = [81, 77, 92, 88]
# lastChangeTeacher(testNames, testAssign, testGrades)

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
