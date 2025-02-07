#In the code we achieving Polymorphism
#using Method Overriding
class Calculator:
    def calculate(self,a,b):
      pass

class Add(Calculator):
    def calculate(self, a, b):
        print('Addition:',a+b)

class sub(Calculator):
    def calculate(self, a, b):
        print('Subtraction:',a-b)

class Mul(Calculator):
    pass

ref = Add()
ref.calculate(10,20)

ref = Sub()
ref.calculate(20,10)

ref = Mul()
ref.calculate(10,20)

def permit(ref,a,b):
    if type(ref)._name_ == 'Mul':
        print('Mul class does not have calculation()')
    else:
        ref.calculate(a,b)
permit(Add(),10,20)
permit(Sub(),20,10)
permit(Mul(),10,20)
