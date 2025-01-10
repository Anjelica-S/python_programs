#anjelica S 11/19/24
#calculator thingy


#functions

def add(num1, num2):
    print(num1+num2)
def subtract(num1, num2):
    print(num1 - num2)
def multiply(num1,num2):
    print(num1 * num2)
def divide(num1, num2):
    print(num1/num2)
def exponent(num1, num2):
    print(num1**num2)
def calculator():
    print("hello! welcome to the simple calculator!")
    print("please choose an operation: ")
    print ("""1 = add
    2 = subtract
    3 = multiply
    4 = divide
    5 = exponentation
    6 = quit""")
    operation = int(input("(1-6):"))

    while operation != int(6):
        
        if operation == 1:
            add1 = int(input("enter first number:"))
            add2 = int(input("enter second number:"))
            add(add1, add2)
        elif operation == 2:
            sub1 = int(input("enter first number:"))
            sub2 = int(input("enter second number:"))
            subtract(sub1, sub2)
        if operation == 3:
            mult1 = int(input("enter first number:"))
            mult2 = int(input("enter second number:"))
            multiply(mult1, mult2)
        if operation == 4:
            div1 = int(input("enter first number:"))
            div2 = int(input("enter second number:"))
            divide(div1, div2)
        if operation == 5:
            ex1 = int(input("enter first number:"))
            ex2 = int(input("enter second number:"))
            exponent(ex1, ex2)
            
        print("please choose an operation: ")
        print ("""1 = add
    2 = subtract
    3 = multiply
    4 = divide
    5 = exponentation
    6 = quit""")
        operation = int(input("(1-6):"))
        
    if operation == 6:
            print ("thanks for using the simple calculator!")
        
    
#main

calculator()

