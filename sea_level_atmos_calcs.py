import matplotlib.pyplot as plt
import numpy as np

# Constants
R = 8.3144598  # J/mol/K
M = 0.0289644  # kg/mol (dry air)
g = 9.80665  # m/s^2
L = -0.0065  # K/m (temperature lapse rate)
T0 = 288.15  # K (temperature at sea level)
p0 = 1.01325  # atm (pressure at sea level)
rho0 = 1.225  # kg/m^3 (density at sea level)

# Altitude array
z = np.arange(0, 30000, 1000)  # 0 to 90 km in 1 km steps

# Temperature array
T = T0 + L*z

# Pressure array
p = p0 * (T/T0)**(-g*M/(R*L))

# Density array
rho = p*M/(R*T)

# Plot temperature vs altitude
plt.subplot(1, 3, 1)
plt.plot(z, T)
plt.xlabel('Altitude (m)')
plt.ylabel('Temperature (K)')

# Plot pressure vs altitude
plt.subplot(1, 3, 2)
plt.plot(z, p)
plt.xlabel('Altitude (m)')
plt.ylabel('Pressure (atm)')

# Plot density vs altitude
plt.subplot(1, 3, 3)
plt.plot(z, rho)
plt.xlabel('Altitude (m)')
plt.ylabel('Density (kg/m^3)')

plt.tight_layout()
plt.show()
