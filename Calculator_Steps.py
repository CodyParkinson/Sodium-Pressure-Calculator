'''
Estimation of the pressure of a vessel after a sodium-water interaction
Steps File

Cody Parkinson
Last Update: 02/28/2024

This file is used in the Main_Page to display the anticipated maximum pressure of the vessel
after a sodium and water interaction.
'''




'''
Imports
'''

from Sodium_Density_Func import sodium_density
from Water_Density_Func import water_density
from NaOH_Density_Func import NaOH_Density1




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
def MaximumPressureCalculator(waterTemperature, waterPressureATR, OuterCapsuleVoidVolume, InnerCapsuleVoidVolume, massOfSodiumCapsule, massOfSodiumRodlet):
    # 1. Use the outer capusule void volume and water density to determine the maximum mass/moles of water available.
    waterDensityAtTemp = water_density(waterTemperature, waterPressureATR)
    massOfwater = OuterCapsuleVoidVolume * waterDensityAtTemp
    molesOfWater = massOfwater / 18.02 # Water is 18.02 g/mol



    #2. Use mass of sodium in the capsule (or capsule + rodlet) to determine volume of sodium initially present (cm^3).
    sodiumDensityAtTemp = sodium_density(waterTemperature + 273.15) # Convert temperature to K for function
    totalMassOfSodium = (massOfSodiumCapsule + massOfSodiumRodlet)
    volumeOfSodium = totalMassOfSodium / sodiumDensityAtTemp



    # 3. Use the mass of sodium in capsule (+ rodlet) to determine the moles of sodium available.
    molesOfSodium = (massOfSodiumCapsule + massOfSodiumRodlet) / 22.98977 # Sodium g/mol



    # 4. Use moles of sodium to determine max amount of hydrogen and sodium hydroxide produced in reaction. (Na is limiting reagent)
    molesOfHydrogen = molesOfSodium * 0.5
    molesOfNaOH = molesOfSodium

    massOfHydrogen = molesOfHydrogen * 2.016 # H2 g/mol
    massOfNaOH = molesOfNaOH * 39.997 #NaOH g/mol



    # 5. Determine the concentration of the produced NaOH to estimate the density of the NaOH solution.
    # Note on NaOH solution mass, account for mass of NaOH and remaining water within capsule (not reacted), subtract H2 mass
    massOfNaOHSolution = massOfNaOH - massOfHydrogen + ((molesOfWater - molesOfSodium) * 18.02)

    NaOHwtPercent = (massOfNaOH / massOfNaOHSolution) * 100



    # 6. Use the denisty and mass of NaOH to determine final volume of NaOH solution. (cm^3)
    NaOHDensityAtTemp = NaOH_Density1(NaOHwtPercent, waterTemperature)
    volumeOfNaOHSolution = massOfNaOHSolution / NaOHDensityAtTemp


    # 7. Calculate the net change in liquid volume to find available void volume.
    # Initial water volume is the amount of water in the outer capsule, because it is simply the volume the water is taking up, density does not matter here.
    netChangeInVoid = volumeOfSodium + OuterCapsuleVoidVolume - volumeOfNaOHSolution



    # 8. Use the change in volume with the amount of generated H2 and temperature to calculate the postulated maximum anticipated pressure.
    # This is a simple use of the ideal gas law: P = nRT/V.
    finalPlenumVolume = netChangeInVoid + InnerCapsuleVoidVolume
    finalHydrogenPressure_atm = ((molesOfHydrogen * 0.08206 * (waterTemperature + 237.15)) / (finalPlenumVolume))/0.001
    finalHydrogenPressure_psi = finalHydrogenPressure_atm * 14.6959




    # Dictionary of all results to return to Tkinter page
    dictOfAllResults = {
        "DensityOfWater": waterDensityAtTemp,
        "DensityOfSodium": sodiumDensityAtTemp,
        "DensityOfNaOH": NaOHDensityAtTemp,
        "TotalSodiumMass": totalMassOfSodium, 
        "NaOHwt%": NaOHwtPercent,
        "NaOHVolume": volumeOfNaOHSolution,
        "NetVoidChange": netChangeInVoid,
        "FinalOpenCapsulePlenumVolume": finalPlenumVolume,
        "finalHydrogrenPressurePSI": finalHydrogenPressure_psi,
    }


    # Return the final results:
    return dictOfAllResults