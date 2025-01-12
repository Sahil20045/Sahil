
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
class Cow(Animal):
    def make_sound(self):
        return "Moo!"
def animal_sound(animal):
    print(animal.make_sound())

# Create objects
dog = Dog()
cat = Cat()
cow = Cow()
animal_sound(dog)  
animal_sound(cat)  
animal_sound(cow)  