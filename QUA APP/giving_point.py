import point as pt
import csv

with open(''):
    pass

db = "Soil.csv"
plant_point_list = {}
while True:
    with open(db, 'r') as db:
        pass
    #import csv
    #forloop untill the end of database
    plant_name = input("plant name: ") #form Database
    Moi_min = 50
    Moi_max = 70
    pH_min = 6
    pH_max = 7.5
    Nut_min = 2
    Nut_max = 4
    Temp_min = 25
    Temp_max = 30
    Sal_min = 2
    Sal_max = 4
    soil = [1,3,5]


    print("##### ",soil," , ",Moi_min,Moi_max," , ",pH_min,pH_max," , ",Nut_min,Nut_max," , ",Temp_min,Temp_max," , ",Sal_min,Sal_max)

    print("\n\nดินร่วน = 1,ดินทราย = 2,ดินเหนียว = 3,ดินร่วนปนดินทราย = 4,ดินเหนียวปนดินร่วน = 5,ดินทรายปนดินเหนียว = 6")
    print("type number of your soil",end="")
    ip_soil = int(input(": "))

    ip_moi = int(input("type Moi tnput: "))
    ip_pH = float(input("type pH tnput: "))
    ip_nut = int(input("type nut tnput: "))
    ip_temp = float(input("type temp tnput: "))
    ip_sal = int(input("type sal tnput: "))

    point_moi = pt.Moi_point(Moi_min, Moi_max, ip_moi)
    point_pH = pt.pH_point(pH_min, pH_max, ip_pH)
    point_nut = pt.Nut_point(Nut_min, Nut_max, ip_nut)
    point_temp = pt.Temp_point(Temp_min, Temp_max, ip_temp)
    point_sal = pt.Sal_point(Sal_min, Sal_max, ip_sal)
    point_soil = pt.Soil_type(ip_soil,soil)

    point_all = (point_moi+point_pH+point_nut+point_temp+point_sal)*point_soil

    print("point_soil ",point_soil)
    print("point_moi ",point_moi)
    print("point_pH ",point_pH)
    print("point_nut ",point_nut)
    print("point_temp ",point_temp)
    print("point_sal ",point_sal)

    print(plant_name ,"point is:",point_all)

    plant_point_list.update({plant_name:point_all})

    print(plant_point_list)

    print("Recommand plant for this soil")
    sorted_plant_list = dict(sorted(plant_point_list.items(), key=lambda item: item[1], reverse=True))
    print(sorted_plant_list)
