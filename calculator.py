def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def modulus(x,y):
    return x%y
print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.modulus")

while True:
    choice=input("enter choice 1/2/3/4/5: ")
    if choice in ('1','2','3','4','5'):
        try:
            num1=float(input("enter first number: "))
            num2=float(input("enter second number: "))
            expect ValueError:
                print("invalid input. enter a number")
                continue
            if choice == '1'
