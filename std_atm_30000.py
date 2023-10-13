# import libraries
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import math

# constants
pi = np.pi
gama = 1.4
sigma = 5.67e-8
# W/m^2 K-1
g = 9.81
r = 287
alpha = 0
angle = 90

# Input Data
atmtable = {
    'Elevation (m)': [-2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000, 22000, 24000, 26000, 28000, 30000],
    'Temperature (K)': [301.2, 297.9, 294.7, 291.4, 288.15, 284.9, 281.7, 278.4, 275.2, 271.9, 268.7, 265.4, 262.2, 258.9, 255.7, 252.4, 249.2, 245.9, 242.7, 239.5, 236.2, 233.0, 229.7, 226.5, 223.3, 220.0, 216.8, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 216.7, 218.6, 220.6, 222.5, 224.5, 226.5],
    'Pressure (atm)': [1.2778, 1.2070, 1.1393, 1.0748, 1.01325, 0.9546, 0.8988, 0.8456, 0.7950, 0.7469, 0.7012, 0.6578, 0.6166, 0.5775, 0.5405, 0.5054, 0.4722, 0.4408, 0.4111, 0.3830, 0.3565, 0.3315, 0.3080, 0.2858, 0.2650, 0.2454, 0.2270, 0.2098, 0.1940, 0.1793, 0.1658, 0.1533, 0.1417, 0.1310, 0.1211, 0.1120, 0.1035, 0.09572, 0.08850, 0.08182, 0.07565, 0.06995, 0.06467, 0.05980, 0.05529, 0.04047, 0.02972, 0.02188, 0.01616, 0.01197],
    'Density': [1.2067, 1.1522, 1.0996, 1.0489, 1.0000, 0.9529, 0.9075, 0.8638, 0.8217, 0.7812, 0.7423, 0.7048, 0.6689, 0.6343, 0.6012, 0.5694, 0.5389, 0.5096, 0.4817, 0.4549, 0.4292, 0.4047, 0.3813, 0.3589, 0.3376, 0.3172, 0.2978, 0.2755, 0.2546, 0.2354, 0.2176, 0.2012, 0.1860, 0.1720, 0.1590, 0.1470, 0.1359, 0.1256, 0.1162, 0.1074, 0.09930, 0.09182, 0.08489, 0.07850, 0.07258, 0.05266, 0.03832, 0.02797, 0.02047, 0.01503],
}

trajectory_data = {
    'Time (s)': [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Altitude (m)': [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Mach Number': [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
}

material_properties = {
    'Material': 'Carbon Phenolic Ablative',
    # Approximate thermal conductivity in W/m K
    'Thermal Conductivity (W/m K)': 0.05,
    # Approximate specific heat capacity in J/kg K
    'Specific Heat Capacity (J/kg K)': 1500.0,
    'Density (kg/m³)': 1600.0  # Approximate density in kg/m³
}


BODY = {
    'Nose Cone Diameter (m)': 1.5,  # Diameter of the nose cone in meters
    # Surface area of the nose cone in square meters (approximate)
    'Nose Cone Surface Area (m²)': 7.06858
}

altitude = 24000  # Replace this with the altitude you're interested in
index = atmtable['Elevation (m)'].index(altitude)

elevation = atmtable['Elevation (m)'][index]
temperature = atmtable['Temperature (K)'][index]
pressure = atmtable['Pressure (atm)'][index]
density = atmtable['Density'][index]


print(f"At altitude {elevation} m:")
print(f"Temperature: {temperature} K")
print(f"Pressure: {pressure} atm")
print(f"Density: {density}")


# Input Data
elevation = atmtable['Elevation (m)']
temperature = atmtable['Temperature (K)']
pressure = atmtable['Pressure (atm)']
density = atmtable['Density']

# Create subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

# Plot Temperature vs. Elevation
ax1.plot(elevation, temperature, label='Temperature (K)', color='r')
ax1.set_ylabel('Temperature (K)')
ax1.set_xlabel('Elevation (m)')
ax1.legend()

# Plot Pressure vs. Elevation
ax2.plot(elevation, pressure, label='Pressure (atm)', color='g')
ax2.set_ylabel('Pressure (atm)')
ax2.set_xlabel('Elevation (m)')
ax2.legend()

# Plot Density vs. Elevation
ax3.plot(elevation, density, label='Density', color='b')
ax3.set_ylabel('Density')
ax3.set_xlabel('Elevation (m)')
ax3.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
