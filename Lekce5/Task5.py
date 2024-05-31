def soucet_v_rozsahu(pocatek, konec):
 

  if pocatek > konec:
    raise ValueError("Počáteční číslo nesmí být větší než koncové číslo.")

  soucet = 0
  for cislo in range(pocatek, konec + 1):
    soucet += cislo
    
  return soucet


a = int(input("Zadej počáteční číslo rozsahu:"))
b = int(input("Zadej konecové číslo rozsahu:"))
print(soucet_v_rozsahu(a,b))



"""
def task5(start, end):
    output = 0
    for i in range(start, end):
        output += i

    return output


def task5_version2(start, end):
    return sum(range(start, end))

print(task5(1,5))
print(task5_version2(1,5)) 

"""