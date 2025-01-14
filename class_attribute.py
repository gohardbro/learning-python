class Person:
    def __init__(self):
        self.hello = 'Hello!'
        
    def greeting(self):
        print(self.hello)
        
john = Person()
john.greeting()