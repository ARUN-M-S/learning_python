from unittest import result


def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        raise ValueError("cannot divide by zero")

    return x/y

def displayMenu():
     print("\n Simple calculator")
     print("1.Add")
     print("2.Substract")
     print("3.Multiply")
     print("4.Divide")
     print("5.Exist")

     choise = input("Enter your choise: ")
     return choise

def getValues():
    x=float(input('Input first value: '))
    y=float(input('Input first value: '))
    return x,y


def main():
    while True:
     choise=displayMenu()
     if choise=='1':
        x,y=getValues()
        result = add(x,y)
        print(result)
     elif choise=='2':
        x,y=getValues()
        result = minus(x,y)
        print(result)
     elif choise=='3':
        x,y=getValues()
        result = multiply(x,y)
        print(result)
     elif choise=='4':
        x,y=getValues()
        
        try:
             result = divide(x, y)
             print(f"The result is: {result}")
        except ValueError as e:
            print(e)
     elif choise=='5':
        print("Exiting the calculator. Goodbye!")
        break
     else:
        print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()