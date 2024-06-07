from random import randint

def drunkman_simulator(size, steps):
  """
  https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html

  """
  
  position = size // 2  # Opilec začíná na půli cesty
  direction = 1  # 1 = směr k hospodě, -1 = směr domů

  for _ in range(steps):
    # Náhodný krok
    step = randint(-1, 1)
    
    # Aktualizace pozice
    position += step * direction
    
    # Kontrola konce simulace
    if position == 0:
      # Došel domů
      return "Opilec se dobelhal domů!"
    elif position == size:
      # Došel do hospody
      return "Opilec se opět dopotácel do hospody!"

    # Zobrazení simulace
    print("home","." * (size - abs(position)) + "*" + "." * abs(position,),"pub")

  # Došel maximální počet kroků
  return "Simulace skončila po maximálním počtu kroků."

# Ukázkový výstup
print(drunkman_simulator(10, 100))
