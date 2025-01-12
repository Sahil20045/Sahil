
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."

animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Kitty")

print(animal.speak())  
print(dog.speak())     
print(cat.speak())     