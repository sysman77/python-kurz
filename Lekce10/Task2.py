"""
Vytvořte třídu pro výpočet plochy geometrických tvarů. Třída by měla poskytovat funkcionalitu pro výpočet plochy
 trojúhelníku pomocí různých vzorců, plochy obdélníku, plochy čtverce, plochy kosočtverce.
 Třídové metody pro výpočet plochy by měly být implementovány se statickými metodami. Třída by také měla počítat počet
výpočtů a vracet tuto hodnotu pomocí statické metody.
"""
class GeometrickéTvary:
    # Atribut třídy pro sledování počtu provedených výpočtů
    _count = 0

    @staticmethod
    def vypocitej_plochu_trojuhelniku_zakladna_vyska(zakladna, vyska):
        GeometrickéTvary._count += 1
        return 0.5 * zakladna * vyska

    @staticmethod
    def vypocitej_plochu_trojuhelniku_heron(a, b, c):
        GeometrickéTvary._count += 1
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @staticmethod
    def vypocitej_plochu_obdelniku(sirka, vyska):
        GeometrickéTvary._count += 1
        return sirka * vyska

    @staticmethod
    def vypocitej_plochu_ctverce(strana):
        GeometrickéTvary._count += 1
        return strana ** 2

    @staticmethod
    def vypocitej_plochu_kosotverce(d1, d2):
        GeometrickéTvary._count += 1
        return 0.5 * d1 * d2

    @staticmethod
    def get_count():
        return GeometrickéTvary._count

# Příklady použití:
plocha_trojuhelnik1 = GeometrickéTvary.vypocitej_plochu_trojuhelniku_zakladna_vyska(10, 5)
plocha_trojuhelnik2 = GeometrickéTvary.vypocitej_plochu_trojuhelniku_heron(3, 4, 5)
plocha_obdelnik = GeometrickéTvary.vypocitej_plochu_obdelniku(7, 8)
plocha_ctverec = GeometrickéTvary.vypocitej_plochu_ctverce(4)
plocha_kosotverec = GeometrickéTvary.vypocitej_plochu_kosotverce(6, 8)

# Výpis výsledků
print(f"Plocha trojúhelníku (základna a výška): {plocha_trojuhelnik1}")
print(f"Plocha trojúhelníku (Heronův vzorec): {plocha_trojuhelnik2}")
print(f"Plocha obdélníku: {plocha_obdelnik}")
print(f"Plocha čtverce: {plocha_ctverec}")
print(f"Plocha kosočtverce: {plocha_kosotverec}")

# Počet provedených výpočtů
print(f"Počet provedených výpočtů: {GeometrickéTvary.get_count()}")
