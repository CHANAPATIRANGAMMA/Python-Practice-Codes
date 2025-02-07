class  Demo1:
    def _init_(self):
        self.x = 100
    def _init_(self):
        self.x = 200
d1 = Demo1()
print(d1.x)

'''
When we create multiple Constructors in same class then 
only last declared constructor will be invoked at the 
time of object creation.
'''