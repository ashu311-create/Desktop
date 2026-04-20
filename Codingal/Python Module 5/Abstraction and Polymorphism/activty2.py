from abc import ABC , abstractmethod
class Animal(ABC):
    def move (self):
        pass
class Human (Animal):
    def move (self):
        print("I can walk and run")
class snake (Animal):
    def move (self):
        print("I can crawl")
class dog(Animal):
    def move (self):
        print("I can bark")
class Lion(Animal):
    def move (self):
        print ("I can roar")
R=Human()
R.move()
R=snake()
R.move()
R=dog()
R.move()
R=Lion()
R.move()