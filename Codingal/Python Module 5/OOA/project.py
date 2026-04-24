class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print("-------------------")
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "German Shepherd")
dog1.display()
dog2.display()