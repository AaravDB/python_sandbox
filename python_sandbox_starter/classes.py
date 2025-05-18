# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class user:
    def __init__(self,name,age,hometown):
        self.name=name
        self.age=age
        self.hometown=hometown
    def greeting(self):
        return f'Hello!My name is {self.name}, I am {self.age} years old and I belong to {self.hometown} .Where are you from?'

brad=user('aarav',20,'chandigarh')
print(brad.greeting())

