class Student(object):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
class Student_manager(object):
    def __init__(self):
        self.los=[]
    def add_student(self,new_student):
        self.los.append(new_student)
        print("The new student is added")
    def view_students(self):
        if not self.los:
            print('''There is no student listed''')
        else:
            print("The list of student:\n")
            for id, student in enumerate(self.los, start=1):
                print(f"{id} - {student.name} - {student.grade}")
    def average_grade(self):
        if not self.los:
            print("No record of the students")
        else:
            number = 0
            grade= 0
            for id, student in enumerate(self.los, start=1):
                number = number + 1
                grade= grade + student.grade
            print(f'''The average is: {grade/number}''')

manager=Student_manager()

def menu():
    print('''Select from the menu:\n
    1. Add a new student
    2. View students info and grades
    3. Calculate average 
    4. Exit''')
    try:
        menu_=int(input())
        if menu_ in [1,2,3]:
            return menu_
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid input")
menu_input=menu()
def continue_menu():
    print("Do you want to continue?[Y/N]")
    try:
        answer=input().upper()
        if answer in ["Y","N"]:
            if answer == "N":
                menu_input=menu()
                return menu_input
        else:
            print("Invalid input")
    except ValueError:
        print("Invalid Input")
        
        


while menu_input in [1,2,3]:
    if menu_input == 1:
        try:
            new_name= input("Enter the name of the student")
            new_grade= float(input("Enter the grade of the student"))
            new_student1=Student(new_name, new_grade)
            manager.add_student(new_student1)
            menu_input=menu()
        except ValueError:
            print("Invalid input")
    if menu_input == 2:
        manager.view_students()
        menu_input=menu()
    if menu_input == 3:
        manager.average_grade()
        menu_input=menu()
if menu_input == 4:
    print("END OF THE PROGRAM")
