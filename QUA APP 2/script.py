import csv
import function as fn

while True: #program loop
    program = str(input("Start? Y/any: "))
    if program == "y" or program == "Y":
        pass
    else:
        break
    
    plant_point_list = {} #output list(dict)
    
    print("\n\nดินร่วน = 1, ดินทราย = 2, ดินเหนียว = 3, ดินร่วนปนดินทราย = 4, ดินร่วนปนดินเหนียว = 5, ดินทรายปนดินเหนียว = 6, ดินตะกอน = 7, ดินร่วนซุย = 8, ดินรุกรัง = 9, ดินตกตะกอนริมแม่น้ำ = 0")
    ip_soil = str(input("ชนิดของดิน: "))
    ip_moi = int(input("ค่าความชื้น (0-100): "))
    ip_pH = float(input("ค่า pH (0-14): "))
    ip_nut = int(input("ปริมาณสารอาหาร (0-infinite): "))
    ip_temp = float(input("อุณหภูมิ (ส่วนใหญ่จะเป็น 20-40): "))
    ip_sal = int(input("ค่าความเค็ม: "))
    
    with open('Soil.csv', 'r', encoding="UTF-8") as db:
        pdb = csv.reader(db)
        next(pdb) #skip ID
        
        for row in pdb: #วนทีละแถว
            count = 0
            for cell in row: #วนคอลัมน์
                count += 1 #เพิ่มจำนวน count ขึ้นเรื่อยๆจนถึง 15
                match count:
                    case 1:
                        ID = cell
                    case 2:
                        name = str(cell)
                    case 3:
                        soil = list(cell)
                    case 4:
                        moi_min = float(cell)
                    case 5:
                        moi_max = float(cell)
                    case 6:
                        pH_min = float(cell)
                    case 7:
                        pH_max = float(cell)
                    case 8:
                        nut_min = float(cell)
                    case 9:
                        nut_max = float(cell)
                    case 10:
                        temp_min = float(cell)
                    case 11:
                        temp_max = float(cell)
                    case 12:
                        sal_min = float(cell)
                    case 13:
                        sal_max = float(cell)
                    case 14:
                        local = str(cell)
                    case 15:
                        break

            point_moi = fn.Moi_point(moi_min, moi_max, ip_moi)
            point_pH = fn.pH_point(pH_min, pH_max, ip_pH)
            point_nut = fn.Nut_point(nut_min, nut_max, ip_nut)
            point_temp = fn.Temp_point(temp_min, temp_max, ip_temp)
            point_sal = fn.Sal_point(sal_min, sal_max, ip_sal)
            point_soil = fn.Soil_type(ip_soil,soil)
            point_all = fn.calculate_final_score(point_moi, point_pH, point_nut, point_temp, point_sal, point_soil)
            plant_point_list.update({name:point_all})
        
        sorted_plant_list = dict(sorted(plant_point_list.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_plant_list)
        
        lenght_list = (input("How many plant do you want to show?: "))
        
        count = 1
        prefnum = 1
        
        for key, value in sorted_plant_list.items():
            print(f"{prefnum}. {key} ความใกล้เคียง {value}")
            if value == 0 or count >= int(lenght_list):
                break
            count += 1
            prefnum += 1
        
        plantNameFromList = list(sorted_plant_list.keys())
        
        while True:
            while True:
                exit = input("\nอยากจะดูข้อมูลการปลูกพืชไหน (หากต้องการจะออก พิมพ์ back):\n")
                if exit == "back":
                    break
                else:
                    name = plantNameFromList[int(exit)-1]
                    print(name)
                    try:
                        file1 = open(f"information/{name}.txt", "r+", encoding="utf-8")
                    except:
                        print("ยังไม่มีข้อมูล ณ ตอนนี้ ขออภัย")
                        break
                    print(f"----------information of {name}----------")
                    file1 = open(f"information/{name}.txt", "r+", encoding="utf-8")
                    print(file1.read())
            if exit == "back":
                break
            
print("End")