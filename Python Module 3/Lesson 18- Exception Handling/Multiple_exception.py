try:
    num1, num2=eval(input("Enter 2 numbers seperated by commas:"))
    result=num1/num2
    print ("Result is",result)
except ZeroDivisionError:
    print("Division by 0 is an error!")
except SyntaxError:
    print ("Comma is missing. Put the numbers like this -> 1,2")
except:
    print("Wrong Input")
else:
    print ("No exceptions")
finally:
    print("This will execute")