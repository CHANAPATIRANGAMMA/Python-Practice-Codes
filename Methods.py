class Student:
    def cook(self):
        print('Student is cooking')
    def play(self):
        print('playing cricket')

class Employee(Student):
    def work(self):
        print('Employee is working')
    def cook(self):
        print('Employee is cooking')
e = Employee()
e.play()
