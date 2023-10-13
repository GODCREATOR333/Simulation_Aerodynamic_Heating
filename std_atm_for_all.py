import matplotlib.pyplot as plt
import numpy as np

alt = int(input("enter altitude :"))


def indian(alt):
    # Constants
    R = 8.3144598  # J/mol/K
    M = 0.0289644  # kg/mol (dry air)
    g = 9.80665  # m/s^2
    L = -0.0065  # K/m (temperature lapse rate)
    T0 = 288.15  # K (temperature at sea level)
    p0 = 1.01325  # atm (pressure at sea level)
    rho0 = 1.225  # kg/m^3 (density at sea level)

    # Altitude array
    z = np.arange(0, alt, 1000)  # 0 to 90 km in 1 km steps

    # Temperature array
    te = T0 + L*z

    # Pressure array
    epsilon = 1e-10  # A small constant to avoid division by zero or taking the power of a negative number

    # Check for small values and apply a floor to avoid issues
    te_safe = np.maximum(te, epsilon)
    T0_safe = np.maximum(T0, epsilon)
    p = p0 * (te_safe / T0_safe) ** (-g * M / (R * L))

    # Density array
    den = p*M/(R*te)

    # Plot temperature vs altitude
    # Create subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

    # Plot Temperature vs. Altitude
    ax1.plot(z, te)
    ax1.set_xlabel('Altitude (m)')
    ax1.set_ylabel('Temperature (K)')

    # Plot Pressure vs. Altitude
    ax2.plot(z, p)
    ax2.set_xlabel('Altitude (m)')
    ax2.set_ylabel('Pressure (atm)')

    # Plot Density vs. Altitude
    ax3.plot(z, den)
    ax3.set_xlabel('Altitude (m)')
    ax3.set_ylabel('Density (kg/m^3)')

    # Show the plot
    plt.tight_layout()
    plt.show()


indian(alt)
