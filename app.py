# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Create an instance of the Dog class
dog = Dog("Buddy")
print(f"{dog.name} says {dog.speak()}")  # Output: Buddy says Woof!