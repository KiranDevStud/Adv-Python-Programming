def div(a,b):
    try:
        k=a//b
    except ZeroDivisionError:
        print("Cannot divide by zero!!")
    else: 
        print("Division done the result is:",k)

num1=int(input("Enter a number"))
num2=int(input("Enter another number"))
div(num1,num2)
