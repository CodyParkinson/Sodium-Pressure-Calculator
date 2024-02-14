


'''
Imports
'''

from iapws import IAPWS97




'''
User Inputs
'''

# cm^3
OuterCapsuleVoidVolume = 4.269

# cm^3
InnerCapsuleVoidVolume = 1.970




'''
Functions
'''

# Calculate water density from temp in C and pressure in MPa
def water_density(temp_celsius, pressure_mpa):
    water = IAPWS97(T=temp_celsius + 273.15, P=pressure_mpa)
    return water.rho  # returns the density in kg/m^3