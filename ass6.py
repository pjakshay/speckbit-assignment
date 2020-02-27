n = int(input("Please enter number of students:"))

all_students = []

for i in range(0, n):
    stud_name = input('Enter the name of student: ')
    print(stud_name)

    stud_rollno = input('Enter the roll number of student: ')
    print (stud_rollno)

    

    all_students.append({
                            'Name': stud_name,
                            'Rollno': stud_rollno,
                            
                            })

for student in all_students:
    print('\n')
    for key, value in student.items():
        print('{0}: {1}'.format(key, value))
