ad=input("Adinizi daxil edin: ")
soyad=input("Soyadinizi daxil edin: ")

print(f"Salam {soyad} {ad}!") # ad soyadi ekrana cap etmek 
"""

Bu programda men calismisam ki besit kalkulyator yazim.



"""

def hesablama_masini():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"

    print(f"The result is: {result}")

hesablama_masini()