'''
Sodium Density Function for calculation of density based on temperature

Cody Parkinson
Last Update: 02/19/2024

Issues with function:
The function is designed to be most accuarate with sodium at 600 C. Below this there are differences between the 
actual recorded density and calculated density. Example at 100 C sodium is said to have a density of 0.927 g/cm^3. 
The function returns 0.930 g/cm^3. This difference is larger than the 0.02% at 600 C and above. Although there is a
difference, it will be neglected for now given the ease of being able to calculate sodium density at different temperatures.
If a better model is found for sodium under 600 C, it will be implemented, but for now, this model will be used.
'''

# Polynomials from https://www.thermalfluidscentral.org/encyclopedia/index.php/Thermophysical_Properties:_Sodium

import numpy as np

def sodium_density(temp_K):

    # Coefficients α_0 to α_5
    alpha = [6.9583, -3.9865e-4, 2.6890e-7, -2.5843e-10, 1.0321e-13, -1.6518e-17]

    # Calculate the natural log of density
    ln_density_kg_m3 = sum(alpha[i] * temp_K**i for i in range(6))

    # Convert density to g/cm³ and return
    density_g_cm3 = np.exp(ln_density_kg_m3) * 0.001
    return density_g_cm3


