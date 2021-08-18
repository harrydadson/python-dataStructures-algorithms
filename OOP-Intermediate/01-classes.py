class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def speak(self):
        print(f"Hi! I am {self.name} and I'm {self.age}")

    def change_age(self, age):
        self.age = age

    

h = Dog("frisky", 32)
f = Dog("Fred", 55)

h.speak()
f.speak()
f.change_age(50)
f.speak()