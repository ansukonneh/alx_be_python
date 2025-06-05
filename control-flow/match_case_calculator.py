num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = str(input("Choose the operation (+, -, *, /):"))

match operator:
    case  "+":
        result = num1 + num2
        print(f"The result is {result}.")

match operator:
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")

match operator:
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")

match operator:
    case "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            result = num1 / num2
            print(f"The result is {result}.")

    case _:
        print("Invalid Operation Selected")
            
 
  


