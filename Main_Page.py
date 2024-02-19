'''
Estimation of the pressure of a vessel after a sodium-water interaction
Main Page

Cody Parkinson
Last Update: 02/19/2024
'''




'''
Imports
'''

from Sodium_Density_Func import sodium_density
from Water_Density_Func import water_density




'''
User Input Defaults
'''

# Water Temperature (C)
waterTemperature = 100.0

# Water Pressure (MPa)
waterPressureATR = 350.0/145.038 # Convert psi to MPa from ATR

# cm^3
OuterCapsuleVoidVolume = 4.269

# cm^3
InnerCapsuleVoidVolume = 1.970

# Mass of sodium (g)
massOfSodiumCapsule = 1.771
massOfSodiumRodlet = 2.182 - 1.771








'''
Calculations:
Step numbers are directly related to Terrapower steps
'''

# 1. Use the outer capusule void volume and water density to determine the maximum mass/moles of water available.
massOfwater = OuterCapsuleVoidVolume * water_density(waterTemperature, waterPressureATR)
molesOfWater = massOfwater / 18.02 # Water is 18.02 g/mol

#2. Use mass of sodium in the capsule (or capsule + rodlet) to determine volume of sodium initially present (cm^3).
volumeOfSodium = (massOfSodiumCapsule + massOfSodiumRodlet) + sodium_density(waterTemperature + 273.15) # Convert temperature to K for function

# 3. Use the mass of sodium in capsule (+ rodlet) to determine the moles of sodium available.
molesOfSodium = (massOfSodiumCapsule + massOfSodiumRodlet) / 22.98977 # Sodium g/mol

# 4. Use moles of sodium to determine max amount of hydrogen and sodium hydroxide produced in reaction. (Na is limiting reagent)
molesOfHydrogen = molesOfSodium * 0.5
molesOfNaOH = molesOfSodium

massOfHydrogen = molesOfHydrogen * 2.016 # H2 g/mol
massOfNaOH = molesOfNaOH * 39.997 #NaOH g/mol

# 5. Determine the concentration of the produced NaOH to estime the density of the NaOH solution.
