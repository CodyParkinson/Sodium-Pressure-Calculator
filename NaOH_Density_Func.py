'''
NaOH Density Function based on temperature and weight percent

Cody Parkinson
Last Update: 02/26/2024
'''


'''
Section 1 based on data from:
https://www.handymath.com/cgi-bin/naohtble3.cgi?submit=Back+to+Calculator&tmptr=100&spcfgrv=&conc=70
'''
import numpy as np
from scipy.interpolate import RegularGridInterpolator


# Define the weight percent and temperature arrays based on the provided table
weight_percent = np.array([1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 50])
temperatures = np.array([0, 15, 20, 40, 60, 80, 100])

# Define the density array (fill this with the actual data from the table)
densities = np.array([
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
interp_func = RegularGridInterpolator((weight_percent, temperatures), densities)

# Define the function to get the interpolated density
def get_density(wt_percent, temp):
    point = np.array([wt_percent, temp])
    return interp_func([point])[0]

# Example usage
wt_percent_input = 50  # Example: 5% weight
temp_input = 100  # Example: 25°C

density_output = get_density(wt_percent_input, temp_input)
print(f"Estimated density at {wt_percent_input}% weight and {temp_input}°C is {density_output:.4f} g/cm^3")







'''
Section 2 based on data from:
https://advancedthermo.com/electrolytes/density_NaOH.html
'''
def weight_percent_to_molality(wt_percent, molecular_weight_NaOH=40):
    mass_NaOH = wt_percent / 100 * 1000  # mass of NaOH in grams in 1 kg of solution
    mass_water = 1000 - mass_NaOH  # mass of water in grams
    molality = mass_NaOH / molecular_weight_NaOH / (mass_water / 1000)  # molality (mol/kg)
    return molality


# Example molality and temperature arrays
molality = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])
temperatures = np.array([10.0, 25.0, 40.0, 55.0, 70.0, 85.0]) # Temperatures from your table

# Define your densities array with the actual data
densities = np.array([
    [1.00437, 1.00149, 0.99654, 0.98996, 0.98200, 0.97282],
    [1.00893, 1.00584, 1.00078, 0.99414, 0.98615, 0.97696],
    [1.01342, 1.01014, 1.00498, 0.99827, 0.99025, 0.98106],
    [1.01784, 1.01440, 1.00912, 1.00235, 0.99430, 0.98511],
    [1.02222, 1.01860, 1.01322, 1.00639, 0.99832, 0.98913],
    [1.02654, 1.02277, 1.01729, 1.01038, 1.00230, 0.99312],
    [1.03082, 1.02691, 1.02132, 1.01437, 1.00624, 0.99708],
    [1.03505, 1.03101, 1.02532, 1.01831, 1.01016, 1.00100],
    [1.03925, 1.03507, 1.02929, 1.02222, 1.01405, 1.00490],
    [1.04340, 1.03911, 1.03323, 1.02610, 1.01790, 1.00878],
    [1.05161, 1.04711, 1.04103, 1.03377, 1.02553, 1.01644],
    [1.05968, 1.05495, 1.04871, 1.04134, 1.03306, 1.02400],
    [1.06762, 1.06270, 1.05629, 1.04880, 1.04048, 1.03146],
    [1.07544, 1.07034, 1.06376, 1.05617, 1.04780, 1.03882],
    [1.08315, 1.07787, 1.07114, 1.06343, 1.05503, 1.04609],
    [1.10191, 1.09626, 1.08915, 1.08120, 1.07270, 1.06383],
    [1.12001, 1.11402, 1.10659, 1.09840, 1.08980, 1.08098],
    [1.13748, 1.13118, 1.12347, 1.11508, 1.10637, 1.09756],
    [1.15437, 1.14776, 1.13980, 1.13124, 1.12243, 1.11357],
    [1.17070, 1.16378, 1.15562, 1.14691, 1.13799, 1.12904],
    [1.18652, 1.17925, 1.17093, 1.16212, 1.15308, 1.14397],
    [1.20186, 1.19421, 1.18576, 1.17687, 1.16771, 1.15837],
    [1.21677, 1.20866, 1.20013, 1.19121, 1.18192, 1.17227]
])

# Create the interpolator function
interp_func = RegularGridInterpolator((molality, temperatures), densities, bounds_error=False, fill_value=None)

# Define the function to get the interpolated/extrapolated density
def get_density(mol, temp):
    point = np.array([[mol, temp]])
    density = interp_func(point)
    return density[0]

# Example usage
mol_input = weight_percent_to_molality(wt_percent_input)  # Example molality beyond the provided range

density_output = get_density(mol_input, temp_input)
print(f"The estimated density at {mol_input} mol/kg and {temp_input}°C is {density_output:.4f} g/cm³")


