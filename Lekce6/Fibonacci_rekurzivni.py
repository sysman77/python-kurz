def fibonacci_rekurzivni(n, l):
    l[0] += 1
    
    if n <= 2:
        return 1
  
    return fibonacci_rekurzivni(n - 1, l) + fibonacci_rekurzivni(n - 2, l) 

krok = 9
l = [0]
print(fibonacci_rekurzivni(krok, l))
print(l)
