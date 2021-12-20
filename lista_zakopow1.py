# Zadanie 1
moje_zakupy = {"piekarnia": ["chleb", "bułki", "pączek"],
               "warzywniak": ["marchew", "pomidory", "seler"]}

ilosc = (len(moje_zakupy.get("piekarnia")) + len(moje_zakupy.get("warzywniak")))
print("Wchdzę do warzywniaka i kupuję: ", moje_zakupy["warzywniak"], "\na potem wchodzę do piekarni i kupuję: ",
      moje_zakupy["piekarnia"],
      "\nW sumie kupuję", ilosc, " produktów")

# Zadanie 2
podzielne_5 = []
for i in range(0, 100):
    if i % 5 == 0:
        podzielne_5.append(i)
print(podzielne_5)
# kwadrat_prosciej = [number * number for number in liczby if number > 10]
potegi_3 = [liczba ** 3 for liczba in podzielne_5]
print(potegi_3)