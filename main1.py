rok = 2025
text = "Veselé Velikonoce"
cislo = 51054601

#fstring
print(f"Ahoj, {text}  {rok}")

 #oddělovačtisíců
print (f"{cislo:, }")

#vypsat počet písmen

#Úkol 1
jmeno = input("Zadejte své jméno: ")
vek = input("Zadejte svůj věk: ")

print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let. ")

#ÚKOL2

cislo1 = float(input("Zadejte první desetinné číslo: "))
cislo2 = float(input("Zadejte druhé desetiné číslo: "))
soucet = cislo1 + cislo2
rozdíl= cislo1 - cislo2
soucin = cislo1 * cislo2
podíl = cislo1 / cislo2 if cislo2 != 0 else "Nedefinováno (dělení nulou )"
print(f"Součet: {soucet: .2f}")
print
print
print