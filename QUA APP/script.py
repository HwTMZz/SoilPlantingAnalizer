import csv
import point as pt

while True: #program loop
    program = str(input("Start? y/any: "))
    if program == "y":
        pass
    else:
        break
    
    plant_point_list = {} #output list(dict)
    
    print("\n\nดินร่วน = 1, ดินทราย = 2, ดินเหนียว = 3, ดินร่วนปนดินทราย = 4, ดินร่วนปนดินเหนียว = 5, ดินทรายปนดินเหนียว = 6, ดินตะกอน = 7, ดินร่วนซุย = 8, ดินรุกรัง = 9, ดินตกตะกอนริมแม่น้ำ = 0")
    ip_soil = str(input("type soil input (only one type) : "))
    ip_moi = int(input("type Moisture input (0-100): "))
    ip_pH = float(input("type pH input (0-14): "))
    ip_nut = int(input("type nutrients input (0-infinite): "))
    ip_temp = float(input("type temperature input (mostly around 20-40): "))
    ip_sal = int(input("type salinity input (0-infinite): "))
    with open('random_plant_data.csv', 'r', encoding="UTF-8") as db:
        pdb = csv.reader(db)
        next(pdb) #skip ID
        
        for row in pdb: #วนทีละแถว
            count = 0
            for cell in row: #วนคอลัมน์
                count += 1 #เพิ่มจำนวน count ขึ้นเรื่อยๆจนถึง 15
                if count == 1:
                    ID = cell
                if count == 2:
                    name = str(cell)
                if count == 3:
                    soil = list(cell)
                if count == 4:
                    moi_min = float(cell)
                if count == 5:
                    moi_max = float(cell)
                if count == 6:
                    pH_min = float(cell)
                if count == 7:
                    pH_max = float(cell)
                if count == 8:
                    nut_min = float(cell)
                if count == 9:
                    nut_max = float(cell)
                if count == 10:
                    temp_min = float(cell)
                if count == 11:
                    temp_max = float(cell)
                if count == 12:
                    sal_min = float(cell)
                if count == 13:
                    sal_max = float(cell)
                if count == 14:
                    local = str(cell)
                if count == 15: #วนสุดตาราง (count = 15)
                    break
            point_moi = pt.Moi_point(moi_min, moi_max, ip_moi)
            point_pH = pt.pH_point(pH_min, pH_max, ip_pH)
            point_nut = pt.Nut_point(nut_min, nut_max, ip_nut)
            point_temp = pt.Temp_point(temp_min, temp_max, ip_temp)
            point_sal = pt.Sal_point(sal_min, sal_max, ip_sal)
            point_soil = pt.Soil_type(ip_soil,soil)
            point_all = pt.calculate_final_score(point_moi, point_pH, point_nut, point_temp, point_sal, point_soil)
            plant_point_list.update({name:point_all})
        
        sorted_plant_list = dict(sorted(plant_point_list.items(), key=lambda item: item[1], reverse=True))
        print(sorted_plant_list)
        for key, value in sorted_plant_list.items():
            print(f"{key} = {value}")
        
print("End")