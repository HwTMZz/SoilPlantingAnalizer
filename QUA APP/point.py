def Moi_point (Moi_min, Moi_max, ip_moi):
    point = 0
    if (ip_moi >= Moi_min) and (ip_moi <= Moi_max):
        point = 2
    elif (ip_moi > Moi_max and ip_moi <= Moi_max+10) or (ip_moi >= Moi_min-10 and ip_moi < Moi_min):
        point = 1
    else:
        point = 0
    return point

def pH_point (pH_min, pH_max, ip_pH):
    point = 0
    if (ip_pH >= pH_min) and (ip_pH <= pH_max):
        point = 2
    elif (ip_pH > pH_max and ip_pH <= pH_max+1) or (ip_pH >= pH_min-1 and ip_pH < pH_min):
        point = 1
    else:
        point = 0
    return point

def Nut_point (Nut_min, Nut_max, ip_nut):
    point = 0
    if Nut_max == -1:
        point = 2
    elif (ip_nut >= Nut_min) and (ip_nut <= Nut_max):
        point = 2
    elif (ip_nut > Nut_max and ip_nut <= Nut_max+2) or (ip_nut >= Nut_min-2 and ip_nut < Nut_min):
        point = 1
    else:
        point = 0
    return point

def Temp_point (Temp_min, Temp_max, ip_temp):
    point = 0
    if (ip_temp >= Temp_min) and (ip_temp <= Temp_max):
        point = 2
    elif (ip_temp > Temp_max and ip_temp <= Temp_max+8) or (ip_temp >= Temp_min-8 and ip_temp < Temp_min):
        point = 1
    else:
        point = 0
    return point

def Sal_point (Sal_min, Sal_max, ip_sal):
    point = 0
    if Sal_max == -1:
        point = 2
    elif (ip_sal >= Sal_min) and (ip_sal <= Sal_max):
        point = 2
    elif (ip_sal > Sal_max and ip_sal <= Sal_max+1) or (ip_sal >= Sal_min-1 and ip_sal < Sal_min):
        point = 1
    else:
        point = 0
    return point

def Soil_type (soil_ip,soil):
    if soil_ip in soil:
        point = 2
    else:
        point = 0
    return point

def calculate_final_score(point_moi, point_pH, point_nut, point_temp, point_sal, point_soil):
    # Assign weights to factors
    w_soil = 3
    w_pH = 2
    w_moi = 1
    w_nut = 1
    w_temp = 1.5
    w_sal = 1

    # Calculate the weighted final score
    final_score = ((w_soil * point_soil) + (w_pH * point_pH)+(w_moi * point_moi)
                    + (w_nut * point_nut)+(w_temp * point_temp)+(w_sal * point_sal))

    final_score_most_is_soil = (point_soil * ((w_pH * point_pH)+(w_moi * point_moi)
                    + (w_nut * point_nut)+(w_temp * point_temp)+(w_sal * point_sal)))
    #ถามครู

    return final_score
