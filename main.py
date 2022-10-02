# GLOBAL constants
"""
C + O2 --> CO2
H2 + 0.5(O2) --> H2O
CO + 0.5(O2) --> CO2
S + O2 --> SO2
CH4 + 2O2 -- C02 + 2H2O
2C2H2 + 5O2 --> 4CO2 + 2H2O
C2H4 + 3O2  --> 2CO2 + 2H2O
C2H6 + 3.5O2 --> 2CO2 + 3H2O

"""

# C = 12
# S =32
# O = 32
# H = 2
# N = 28
# CH4 = 16
# C2H2 = 26
# C2h4 = 28
# C2H6 = 30

# LITERS =  22.4
# KILO = 28.95



def combustion():
    print("\n\n\t\t\t______________________________________COMBUSTION NUMERICAL______________________________________\t\t\t\t\n\n")

    p_composition = {
    "H" : 2, "N": 28, "C":12 ,"O" :32, "S" :32, "H2O" :18, "CH4" : 16,"C2H2":26 ,"C2H4" : 28, "C2H6" : 30
    }
    kmol_comp={}

# combustion factor of oxygen for each element individually

    oxy_comp_factor= {"H" : 0.5, "N": 0, "C":1 ,"O" :-1, "S" :1,"CH4" : 2,"C2H2":2.5 ,"C2H4" : 3, "C2H6" : 3.5,"H2O":0,"CO":0.5}

    co2_comp_factor= {"H" : 0, "N": 0,"C":1 , "CH4" : 1,"C2H2":2 ,"C2H4" : 2, "C2H6" : 2, "S":0 , "O":0,"H2O":0,"CO":1}

    h2O_comp_factor = {"CH4" :2, "C2H2" :1,"C2H4" : 2, "C2H6" : 3, "H": 1,"N" : 0,"O":0,"C":0 ,"S":0,"H2O":1,"CO":0}

    total_oxy_req=0
    total_H2O = 0
    total_CO2 = 0
    min_air_req_for_combn = 0

    fuel_type= str(input("What is your Fuel Type? (Solid / gas)->   "))
    min_air_for= float(input("Mininum air for what Kg / cubic meters of Fuel->   "))
    excess_air_supplied= float(input("Enter excess air->   "))
    dw=str(input("Dry(D) OR Wet(W) ->  "))

    print("Enter 'Q' when entering elements are done!")
    if fuel_type.lower() == "solid":
        while True:
            ele= str(input("\nEnter Element: "))
            if ele == "Q":                                  #condition when Elemens are done entering
                print("Elements are done\n")
                break

# getting the kmol of every element in the coal

            given_mass= float(input("Enter given mass: "))
            kmol= (given_mass/p_composition[ele])
            kmol_comp.update({ele:round(kmol,4)})
            print(kmol_comp.items())
            
# Getting started with process of combustion
    # combustion of every element and their flue gasses
            total_oxy_req+=(kmol_comp[ele]*oxy_comp_factor[ele])
            print(f"total Oxygen required = {total_oxy_req}")

            if ele=='N': N_in_flue = kmol_comp[ele]
            if ele=='S': SO2_flue = kmol_comp[ele] 
            total_H2O+=(kmol_comp[ele]*h2O_comp_factor[ele])
            total_CO2+=(kmol_comp[ele]*co2_comp_factor[ele])
        
        print(f"Total Oxygen required for combustion = { total_oxy_req}")
        min_air_req_for_combn = total_oxy_req * (100/21)  
        print("\t\t\t1. MINIMUM AIR")    
        print(f"\n\tMininum air required for combustion is {round(min_air_req_for_combn,4)}")
        m3_of_o2 = (min_air_for/100)*(min_air_req_for_combn *22.4)
        kg_of_o2 = (min_air_for/100)*(min_air_req_for_combn *28.95)
        print(f"\nMininum air required for combustion of {round(min_air_for,4)} kg of fuel is {round(m3_of_o2,4)} cubic meters OR {round(kg_of_o2,4)} kg.")

    # Calculation against actual air
        print("\t\t\t2. AGAINST ACTUAL AIR")
        actual_air_supplied = (100+excess_air_supplied)*(min_air_req_for_combn) / 100
        print(f"\nActual air supplied is {round(actual_air_supplied,4)} kmol.")
        excess_air = actual_air_supplied - min_air_req_for_combn
        print(f"Excess air supplied is {round(excess_air,4)} kmol.")

        free_oxy_flue = round(excess_air*0.21,4)
        print(f"free O2 = {free_oxy_flue} kmol.")
        N_flue = round((N_in_flue + 0.79*actual_air_supplied),4)
        print(f"N2 in flue gas = {N_flue} kmol.")
        print(f"CO2 in flue gas = {total_CO2} kmol.")
        print(f"SO2 in flue gas = {SO2_flue} kmol.")

        if (dw=='W'):
            total_flue = round((free_oxy_flue + N_flue + total_CO2 + SO2_flue +total_H2O ),4)
            print(f"\nTotal flue is {total_flue} kmol.")
        else:
            total_flue = round((free_oxy_flue + N_flue + total_CO2 + SO2_flue),4)
            print(f"\nTotal flue is {total_flue} kmol.")

# Volumetric composotions of components in fuel
        per_oxy_in_fuel = round((free_oxy_flue * 100/total_flue),4)
        per_CO_in_fuel = round((total_CO2 * 100/total_flue),4)
        per_N_in_fuel = round((N_flue * 100/total_flue),4)
        per_SO_in_fuel = round((SO2_flue * 100/total_flue),4)

        if dw=='W':
            per_H2O_in_fuel = round((total_H2O * 100/total_flue),4)
            print(f"\nVolumetric compostions found to be:\n\t% O2 = {per_oxy_in_fuel}\n\t% N2 = {per_N_in_fuel}\n\t% CO2 = {per_CO_in_fuel}\n\t% SO2 = {per_SO_in_fuel}\n\t% H2O = {per_H2O_in_fuel}\n")

        else: print(f"\nVolumetric compostions found to be:\n\t% O2 = {per_oxy_in_fuel}\n\t% N2 = {per_N_in_fuel}\n\t% CO2 = {per_CO_in_fuel}\n\t% SO2 = {per_SO_in_fuel}\n")


    elif fuel_type.lower() == "gas":

        while True:
            ele= str(input("\nEnter Element: "))
            if ele == "Q":                                  #condition when Elemens are done entering
                print("Elements are done\n")
                break

# getting the kmol of every element in the coal

            given_mass= float(input("Enter given mass: "))
            kmol= (given_mass)
            kmol_comp.update({ele:round(kmol,4)})
            print(kmol_comp.items())
            
# Getting started with process of combustion
    # combustion of every element and their flue gasses
            total_oxy_req+=(kmol_comp[ele]*oxy_comp_factor[ele])
            print(f"total o2 req {total_oxy_req}")

            if ele=='N': N_in_flue = kmol_comp[ele]
            if ele=='S': SO2_flue = kmol_comp[ele]              #compo of SO2_flue
            total_H2O+=(kmol_comp[ele]*h2O_comp_factor[ele])
            total_CO2+=(kmol_comp[ele]*co2_comp_factor[ele])
        print(f"\nTotal Oxygen required for combustion = { total_oxy_req}")
        print("\t\t\t1. MINIMUM AIR")    
        min_air_req_for_combn = total_oxy_req * (100/21)    
        print(f"\n\tMininum air required for combustion is {round(min_air_req_for_combn,4)}")
        m3_of_o2 = (min_air_for/100)*(min_air_req_for_combn)
        print(f"Mininum air required for combustion of {round(min_air_for,4)} kg/cubic meters of fuel is {round(m3_of_o2,4)} cubic meters")

    # Calculation against actual air
        print("\t\t\t2. AGAINST ACTUAL AIR")
        actual_air_supplied = (100+excess_air_supplied)*(min_air_req_for_combn) / 100
        print(f"\nActual air supplied is {round(actual_air_supplied,4)} cubic meters.")
        excess_air = actual_air_supplied - min_air_req_for_combn
        print(f"Excess air supplied is {round(excess_air,4)} cubic meters.")

        free_oxy_flue = round(excess_air*0.21,4)
        print(f"\tfree O2 in Flue gas = {free_oxy_flue} cubic meters.")
        N_flue = round((N_in_flue + 0.79*actual_air_supplied),4)
        print(f"\tN2 in flue gas = {N_flue} cubic meters.")
        print(f"\tCO2 in flue gas= {total_CO2} cubic meters.")
        print(f"\tSO2 in flue gas= {SO2_flue} cubic meters.")

        if (dw=='W'):
            total_flue = round((free_oxy_flue + N_flue + total_CO2 + SO2_flue +total_H2O ),4)
            print(f"\nTotal flue is {total_flue} cubic meters.")
        else:
            total_flue = round((free_oxy_flue + N_flue + total_CO2 + SO2_flue),4)
            print(f"\nTotal flue is {total_flue} cubic meters.")

# Volumetric composotions of components in fuel
        per_oxy_in_fuel = round((free_oxy_flue * 100/total_flue),4)
        per_CO_in_fuel = round((total_CO2 * 100/total_flue),4)
        per_N_in_fuel = round((N_flue * 100/total_flue),4)
        per_SO_in_fuel = round((SO2_flue * 100/total_flue),4)

        if dw=='W':
            per_H2O_in_fuel = round((total_H2O * 100/total_flue),4)
            print(f"\nVolumetric compostions found to be:\n\t% O2 = {per_oxy_in_fuel}\n\t% N2 = {per_N_in_fuel}\n\t% CO2 = {per_CO_in_fuel}\n\t% SO2 = {per_SO_in_fuel}\n\t% H2O = {per_H2O_in_fuel}\n")

        else: print(f"\nVolumetric compostions found to be:\n\t% O2 = {per_oxy_in_fuel}\n\t% N2 = {per_N_in_fuel}\n\t% CO2 = {per_CO_in_fuel}\n\t% SO2 = {per_SO_in_fuel}\n")




if __name__ == "__main__":
    combustion()