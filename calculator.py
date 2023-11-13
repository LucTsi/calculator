def subtract(x, y):#function för minus
    return x - y

def add(x, y):#function för plus
    return x + y

def multiply(x, y):#function för multiplication
    return x * y

def divide(x, y):#function för dividion
    return x / y

#calculator programmet
while True:
    #vad du vill göra
    choice = input("Enter multiply/divide,add,subtract: ")
    #forsätt med koden om du är smart och kan stava
    if choice in("add", "sub", "divide", "multiply"):
        try:
            #dina 2 nummer som du vill använda
            num1 = float(input("enter first number"))
            num2 = float(input("enter second number"))
        #bruh
        except ValueError:
            print("idiot")
            continue
        #om du har valt plus
        if choice == "add":
            print(num1, "+", num2, "=", add(num1, num2))
        #om du har valt multiplication
        elif choice == "multiply":
            print(num1, "*", num2, "=", multiply(num1, num2))
        #om du har valt divition
        elif choice == "divide":
            print(num1, "/", num2, "=", divide(num1, num2))
        #om du har valt minus
        elif choice == "subtract":
            print(num1, "-", num2, "=", subtract(num1, num2))
        #en till calculation?
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        #bruh moment varför du kan inte skriva
        print("Invalid Input")