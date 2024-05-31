# TUPLE -> imutable list

t = (2, 4, 3)
t2 = tuple([1, 3, 4])
    
print(t)
print(t[0])
print(t[1])
print(t[2])
print(t2)

t = (t[0], t[1]) # není ideální použití, lepší je použít místo tuple klasický list
print(t)
print(t[0])
