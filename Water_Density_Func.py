'''
Water Density Function based on temperature and pressure

Cody Parkinson
Last Update: 02/19/2024
'''

from iapws import IAPWS97

# Calculate water density from temp in C and pressure in MPa
def water_density(temp_celsius, pressure_mpa):
    water = IAPWS97(T=temp_celsius + 273.15, P=pressure_mpa)
    return water.rho * 0.001  # returns the density in g/cm^3