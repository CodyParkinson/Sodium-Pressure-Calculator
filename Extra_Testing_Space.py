'''
Extra Testing Space

Cody Parkinson
Last Update: 03/4/2024

This space will not be linked anywhere. It is just for quick testing.
'''












































































































'''
# PRESSURE BASED ON AMOUNT OF SODIUM GRAPH

from Sodium_Density_Func import sodium_density
from Water_Density_Func import water_density
from NaOH_Density_Func import NaOH_Density1

import numpy as np
import matplotlib.pyplot as plt

# Assuming water_density, sodium_density, and NaOH_Density1 functions are defined as per your original code

def MaximumPressureCalculator_Mass(waterTemperature, waterPressureATR, OuterCapsuleVoidVolume, InnerCapsuleVoidVolume, massOfSodium):
    # 1. Use the outer capsule void volume and water density to determine the maximum mass/moles of water available.
    waterDensityAtTemp = water_density(waterTemperature, waterPressureATR)
    massOfwater = OuterCapsuleVoidVolume * waterDensityAtTemp
    molesOfWater = massOfwater / 18.02  # Water is 18.02 g/mol
    
    # 2. Use the mass of sodium to determine the volume of sodium initially present (cm^3).
    sodiumDensityAtTemp = sodium_density(waterTemperature + 273.15)  # Convert temperature to K for function
    volumeOfSodium = massOfSodium / sodiumDensityAtTemp

    # 3. Determine the moles of sodium available.
    molesOfSodium = massOfSodium / 22.98977  # Sodium g/mol

    # 4. Calculate the max amount of hydrogen and sodium hydroxide produced in reaction.
    molesOfHydrogen = molesOfSodium * 0.5
    molesOfNaOH = molesOfSodium
    massOfHydrogen = molesOfHydrogen * 2.016  # H2 g/mol
    massOfNaOH = molesOfNaOH * 39.997  # NaOH g/mol

    # 5. Determine the concentration of the produced NaOH to estimate the density of the NaOH solution.
    massOfNaOHSolution = massOfNaOH - massOfHydrogen + ((molesOfWater - molesOfSodium) * 18.02)
    NaOHwtPercent = (massOfNaOH / massOfNaOHSolution) * 100

    # 6. Use the density and mass of NaOH to determine final volume of NaOH solution. (cm^3)
    NaOHDensityAtTemp = NaOH_Density1(NaOHwtPercent, waterTemperature)
    volumeOfNaOHSolution = massOfNaOHSolution / NaOHDensityAtTemp

    # 7. Calculate the net change in liquid volume to find available void volume.
    netChangeInVoid = volumeOfSodium + OuterCapsuleVoidVolume - volumeOfNaOHSolution

    # 8. Calculate the postulated maximum anticipated pressure using the ideal gas law.
    finalPlenumVolume = netChangeInVoid + InnerCapsuleVoidVolume
    finalHydrogenPressure_atm = ((molesOfHydrogen * 0.08206 * (waterTemperature + 237.15)) / (finalPlenumVolume)) / 0.001
    finalHydrogenPressure_psi = finalHydrogenPressure_atm * 14.6959

    return finalHydrogenPressure_psi

def plot_pressure_vs_mass_of_sodium(waterTemperature, waterPressureATR, OuterCapsuleVoidVolume, InnerCapsuleVoidVolume, min_mass, max_mass):
    # Range of sodium masses
    sodium_masses = np.linspace(min_mass, max_mass, 50)

    # Calculate pressures for each mass
    pressures = [MaximumPressureCalculator_Mass(waterTemperature, waterPressureATR, OuterCapsuleVoidVolume, InnerCapsuleVoidVolume, mass)
                 for mass in sodium_masses]

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(sodium_masses, pressures)
    ax.set_xlabel('Mass of Sodium (g)')
    ax.set_ylabel('Hydrogen Pressure (psi)')
    ax.set_title('Hydrogen Pressure vs Mass of Sodium')

    plt.show()

# Example usage:
plot_pressure_vs_mass_of_sodium(100.0, 3, 100, 50, 1.0, 120.0)
'''




'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator

# Define the weight percent and temperature arrays based on the table
weight_percent1 = np.array([1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 50])
temperatures1 = np.array([0, 15, 20, 40, 60, 80, 100])

# Define the density array
densities1 = np.array([
    # Temperatures: 0°C, 15°C, 20°C, 40°C, 60°C, 80°C, 100°C
    [1.0124, 1.01065, 1.0095, 1.0033, 0.9941, 0.9824, 0.9693],  # 1%
    [1.0244, 1.02198, 1.0207, 1.0139, 1.0045, 0.9929, 0.9797],  # 2%
    [1.0482, 1.04441, 1.0428, 1.0352, 1.0254, 1.0139, 1.0009],  # 4%
    [1.0943, 1.08887, 1.0869, 1.0780, 1.0676, 1.0560, 1.0432],  # 8%
    [1.1399, 1.13327, 1.1309, 1.1210, 1.1101, 1.0983, 1.0855],  # 12%
    [1.1849, 1.17761, 1.1751, 1.1645, 1.1531, 1.1408, 1.1277],  # 16%
    [1.2296, 1.22183, 1.2191, 1.2079, 1.1960, 1.1833, 1.1700],  # 20%
    [1.2741, 1.26582, 1.2629, 1.2512, 1.2388, 1.2259, 1.2124],  # 24%
    [1.3182, 1.30940, 1.3064, 1.2942, 1.2814, 1.2682, 1.2546],  # 28%
    [1.3614, 1.35200, 1.3490, 1.3362, 1.3232, 1.3097, 1.2960],  # 32%
    [1.4030, 1.39330, 1.3900, 1.3768, 1.3634, 1.3498, 1.3360],  # 36%
    [1.4435, 1.43340, 1.4300, 1.4164, 1.4027, 1.3889, 1.3750],  # 40%
    [1.4825, 1.47200, 1.4685, 1.4545, 1.4405, 1.4266, 1.4127],  # 44%
    [1.5210, 1.51020, 1.5065, 1.4922, 1.4781, 1.4641, 1.4503],  # 48%
    [1.5400, 1.52900, 1.5253, 1.5109, 1.4967, 1.4827, 1.4690],  # 50%
])

# Create the interpolator function
interp_func1 = RegularGridInterpolator((weight_percent1, temperatures1), densities1, bounds_error=False, fill_value=None)



# Define the function to get the interpolated density
def NaOH_Density(wt_percent, temp):
    point = np.array([wt_percent, temp])
    return interp_func1([point])[0]

# Plotting densities as a function of temperature for different weight percents
plt.figure(figsize=(12, 8))

# Define a range of temperatures for plotting
temperature_range = np.linspace(100, 500, 50)  # 0°C to 100°C

# List of weight percents to plot
weight_percents_to_plot = [10, 30, 50, 70]  # Example weight percents

# Plotting the densities for each weight percent
for wt in weight_percents_to_plot:
    density_values = [NaOH_Density(wt, temp) for temp in temperature_range]
    plt.plot(temperature_range, density_values, label=f"{wt}% NaOH")

plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Density (g/cm³)', fontsize=12)
plt.title('Density of NaOH Solutions as a Function of Temperature', fontsize=14)
plt.legend()
plt.grid(True)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

'''







'''
import matplotlib.pyplot as plt
import numpy as np

# Define the function to calculate sodium density
def sodium_density(temp_C):
    # Convert Celsius to Kelvin
    temp_K = temp_C + 273.15

    alpha = [6.9583, -3.9865e-4, 2.6890e-7, -2.5843e-10, 1.0321e-13, -1.6518e-17]
    ln_density_kg_m3 = sum(alpha[i] * temp_K**i for i in range(6))
    density_g_cm3 = np.exp(ln_density_kg_m3) * 0.001
    return density_g_cm3

# Generate a range of temperatures (in Celsius)
temperatures_C = np.linspace(100, 500, 50)  # From 0°C to 1000°C

# Calculate densities for each temperature
densities = [sodium_density(temp) for temp in temperatures_C]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(temperatures_C, densities, label="Density of Sodium")
plt.xlabel("Temperature (°C)", fontsize=14)
plt.ylabel("Density (g/cm³)", fontsize=14)
plt.title("Density of Sodium as a Function of Temperature")
plt.legend()
plt.grid(True)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()
'''