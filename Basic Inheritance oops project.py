class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.name} is an {self.species} and can speak.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")

    def bark(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")

    def meow(self):
        print(f"{self.name} meows!")
