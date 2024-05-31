from random import randint

seznam = [randint(-10, 10) for _ in range(10)]

# vypiš seznam
print(seznam)

# obrátit seznam a vypiš ho
seznam.reverse()
obraceny = []
for num in seznam:
    obraceny.append(num)
print()    
print(obraceny)