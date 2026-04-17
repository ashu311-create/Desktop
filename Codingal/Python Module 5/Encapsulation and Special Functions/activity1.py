class MyClass:
    __privateVar=27
    def __privMeth(self):
        print("I am inside my class")
    def hello(self):
        print("Private Variable Value:", MyClass.__privateVar)
foo=MyClass()
foo.hello()
foo.__privMeth