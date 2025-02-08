import csv

with open('Soil.csv', 'r', encoding="UTF-8") as db:
    pdb = csv.reader(db)
    next(pdb)
    for row in pdb: #วนทีละแถว
        count = 0
        for cell in row: #วนคอลัมน์
            count += 1
            
IT = "14"
TPIT = list(IT)
print(TPIT)
if "1" in TPIT:
    print("YESSSS")