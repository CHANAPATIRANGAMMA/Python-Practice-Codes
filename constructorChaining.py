'''
1.Constructor Chaining is the process of calling one Constructor
from another constrctor.'''
class GrandParent:
    def _init_(self):
        self.x = 100
class Parent(GrandParent):
    def _init_(self):
        self.y = 200
        super()._init_()
class Child(Parent):
    def _init_(self):
        self.z = 300
        super()._init_()

c = Child()
print(c.z)
print(c.y)
print(c.x)