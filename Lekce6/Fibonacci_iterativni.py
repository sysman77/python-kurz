def fibonacci_iterativni(n):
    num1 = 1
    num2 = 1
    for i in range(2, n):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num3)
    
    return num2


krok = 9
print(fibonacci_iterativni(krok))


# iterativní řešení je lepší než rekurzivní


