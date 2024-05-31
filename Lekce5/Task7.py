def je_stastne_cislo(cislo):
  """
  Tato funkce kontroluje, zda je zadané šestimístné číslo šťastné.

  Argumenty:
    cislo: Řetězec nebo celé číslo obsahující šestimístné číslo.

  Vrací:
    True, pokud je číslo šťastné. False, pokud není.

  Příklad použití:
    je_stastne_cislo("123432") == True  # Číslo 123432 je šťastné
    je_stastne_cislo("789012") == False  # Číslo 789012 není šťastné
  """

  # Kontrola délky čísla
  if len(str(cislo)) != 6:
    raise ValueError("Zadané číslo musí mít 6 číslic.")

  # Převedení čísla na řetězec a rozdělení na dvě části
  cislo_str = str(cislo)
  prvni_tri = cislo_str[:3]
  druha_tri = cislo_str[3:]

  # Sečtení číslic v první a druhé části
  soucet_prvni_tri = sum(int(cislice) for cislice in prvni_tri)
  soucet_druha_tri = sum(int(cislice) for cislice in druha_tri)

  # Kontrola, zda se součty rovnají
  if soucet_prvni_tri == soucet_druha_tri:
    return True
  else:
    return False

# Příklad použití
print(je_stastne_cislo("123420"))  # Vypíše True
print(je_stastne_cislo("789012"))  # Vypíše False





"""
def is_lucky_number(n):
    if n > 999999:
        return False
    
    s = str(n)

    return (int(s[0]) + int(s[1]) + int(s[2]) == 
            int(s[3]) + int(s[4]) + int(s[5]))

#print(is_lucky_number(123420))
#print(is_lucky_number(123421))


def is_lucky_number_version2(n):
    if n > 999999:
        return False
    
    finish_number = 0
    for _ in range(3):
        finish_number += n % 10
        n //= 10 # n = n // 10

    #begin_number = 0
    for _ in range(3):
        finish_number -= n % 10
        n //= 10

    #return finish_number == begin_number
    return finish_number == 0 # not finish_number



def get_three_sum(n):
  number = 0
  for _ in range(3):
    number += n % 10
    n //= 10

  return number, n


def is_lucky_number_version3(n):
    if n > 999999:
        return False

    finish_number, new_n = get_three_sum(n)
    begin_number, _ = get_three_sum(new_n)

    return finish_number == begin_number
    #return finish_number - begin_number == 0

print(is_lucky_number_version3(123321)) 

"""