###################################################################################
#########
# Equality constraints: Energy Flow Balance (thermodynamic balance)
#
###################################################################################
#########
###################################################################################
#########
# Heat Transfer Constraints: Heat Balance
#
def get_greenhouse_heat_energy(T,T_outside):
    Material_Conductivity = 0.002 # conductance of farm wall and roof [kW/m^2/K]
    Area_of_Conduction = 2560 # surface area of farm walls and roof m^2
    delT = T_outside - T # difference in temperature between outside and inside
    return Material_Conductivity*Area_of_Conduction*delT

def get_humidity_heat_energy(Humidification_Rate, Dehumidification_Rate):
    Plant_Humidity_Release = 120.7; # [g/s] loss of water into air
    Latent_Heat_of_Vaporization = 2.257 # [J/g]

    return - Latent_Heat_of_Vaporization*(
        Humidification_Rate
        + Plant_Humidity_Release
        - Dehumidification_Rate
    )

############################################################################################
# Heat Transfer Constraints: Humidity Balance
def get_internal_humidity_energy(x):
    Humidification_Rate, Dehumidification_Rate = x[6:8]
    Plant_Humidity_Release = 120.7; # [g/s] loss of water into air
    return (
        Plant_Humidity_Release
        + Humidification_Rate
        - Dehumidification_Rate
    )
def RH_Inside(T,T_outside,RH_outside):
    T_dewpoint = ((T_outside-273.15) - ((100 - RH_outside)/5))
    RH_newtemp = (5*((T_dewpoint) - (T-273.15)) + 100)
    return RH_newtemp

def get_water_holding_capacity(T):
    return (0.7278*(T*9/5 - 459.67) - 32.189)