# Üres lista létrehozása
szervek = []
print(szervek) # []
# Az üres listát LECSERÉLTÜK az alábbi 3 elemű listára
# Listát lecserélni és feltölteni nem ugyanaz!
szervek = ["agy", "gyomor", "máj"]
print(szervek) # ['agy', 'gyomor', 'máj']

# Új elem hozzáadása a listához:
szervek.append("vese") # A lista végére kerül
print(szervek) # ['agy', 'gyomor', 'máj', 'vese']

# Hozzáférés a lista egy eleméhez:
# Az indexével tudunk utalni rá
szerv = szervek[2]
print(szerv) # máj

# Hozzáférés a lista több eleméhez:
# Tartomány az indexek felhasználásával
# A tartomány felső határa MÁR NEM lesz benne!
print(szervek[1:3]) # ['gyomor', 'máj']


# Lista egy elemének módosítása:
szervek[0] = "szív"
print(szervek) # ['szív', 'gyomor', 'máj', 'vese']

# Lista több elemének módosítása, ha az új elemek többen vannak:
szervek[1:2] = ["vékonybél", "vastagbél"]
print(szervek) # ['szív', 'vékonybél', 'vastagbél', 'máj', 'vese']

# Lista több elemének módosítása, ha az új elemek kevesebben vannak
# Ha több elemet jelöltem ki módosításra a tartomány által, mint
# ahány új elem rendelkezésre áll, akkor a Python lecseréli addig
# az újakra, ameddig csak tudja, amikor pedig elfogynak az új elemek
# a maradék TÖRLŐDIK
szervek[1:3] = ["bélrendszer"]
print(szervek) # ['szív', 'bélrendszer', 'máj', 'vese']