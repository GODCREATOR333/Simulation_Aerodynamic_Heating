import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style

print(Fore.RED + Style.BRIGHT +
      "Remember the maximum altitude for this simulation is 85000 meters to be accurate and within acceptable error.")
alt = int(input("enter altitude(m):"))


def std_international(alt):

    alt = int(input("enter altitude(m):"))
    # Constants
    R = 8.3144598  # J/mol/K
    M = 0.0289644  # kg/mol (dry air)
    g = 9.80665  # m/s^2
    T0 = 288.15  # K (temperature at sea level)
    p0 = 1.01325  # atm (pressure at sea level)
    rho0 = 1.225  # kg/m^3 (density at sea level)

    # Altitude array
    altitudes = np.arange(0, alt, 1000)  # 0 to 90 km in 1 km steps

    # Temperature array
    def temperature_at_altitude(alt):

        # Constants for the ISA model
        h = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000, 95000]
        T = [288.15, 216.65, 216.65, 228.65,
             270.65, 270.65, 214.65, 214.65, 190]
        L = [-0.0065, 1e-2, 0.001, 0.0028, 1e-2, -0.0028, -0.002, -0.005, -0.005]

        for i in range(len(h) - 1):
            if alt >= h[i] and alt < h[i+1]:
                return T[i] + L[i] * (alt - h[i])

        return np.nan  # Return NaN for altitudes outside the model's range

    temp = [temperature_at_altitude(alt) for alt in altitudes]
    temperature_at_altitude(alt)

    # Pressure array
    L = -0.0065  # K/m (temperature lapse rate)
    T0_press = 288.15  # K (temperature at sea level)
    temp_press = T0 + L*altitudes
    epsilon = 1e-10  # A small constant to avoid division by zero or taking the power of a negative number
    L_pressure = -0.0065  # K/m (temperature lapse rate)
    # Check for small values and apply a floor to avoid issues
    te_safe = np.maximum(temp_press, epsilon)
    T0_safe = np.maximum(T0_press, epsilon)
    p = p0 * (te_safe / T0_safe) ** (-g * M / (R * L_pressure))

    # Density array
    for alt in altitudes:
        t = temperature_at_altitude(alt)
        den = p*M/(R*t)

    # Plot temperature vs altitude
    # Create subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

    # Plot Temperature vs. Altitude
    ax1.plot(altitudes, temp)
    ax1.set_xlabel('Altitude (m)')
    ax1.set_ylabel('Temperature (K)')
    # Plot Pressure vs. Altitude
    ax2.plot(altitudes, p)
    ax2.set_xlabel('Altitude (m)')
    ax2.set_ylabel('Pressure (atm)')

    # Plot Density vs. Altitude
    ax3.plot(altitudes, den)
    ax3.set_xlabel('Altitude (m)')
    ax3.set_ylabel('Density (kg/m^3)')

    # Show the plot
    plt.tight_layout()

    # Prepare coordinate points for the three plots
    altitude_temperature_points = list(zip(altitudes, temp))
    altitude_pressure_points = list(zip(altitudes, p))
    altitude_density_points = list(zip(altitudes, den))
    return altitude_temperature_points, altitude_pressure_points, altitude_density_points


std_international(alt)
plt.show()

altitude_temperature_points, altitude_pressure_points, altitude_density_points = std_international(
    alt)

# Print the coordinate points
print("Altitude vs Temperature:")
print(altitude_temperature_points)

print("Altitude vs Pressure:")
print(altitude_pressure_points)

print("Altitude vs  Density:")
print(altitude_density_points)
