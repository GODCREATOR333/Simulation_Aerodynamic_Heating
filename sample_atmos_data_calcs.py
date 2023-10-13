

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

alt = int(input("enter altitude:"))
y = alt


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
    p = p0 * (te/T0)**(-g*M/(R*L))

    # Density array
    den = p*M/(R*te)

    return te, p, den


# te, p, den = indian(alt)
# print("te=", te)
# print("p=", p)
# print("den=", den)


# Inputs
y = np.linspace(0, 10000, 100)  # altitude array (m)
t = np.linspace(0, 200, 100)   # time array (s)
a = interp1d(t, y)(t)        # altitude at times t (m)
m = np.linspace(0.8, 10, len(t))
ts = 288.15                  # start temperature (K)
atmos = 1                    # atmosphere model flag (1=Indian, 0=US Std)
body = 2                     # vehicle type flag
sweep = 30.0                 # wing sweep angle (deg)
angle = 5.0                  # angle of attack (deg)
alpha = 0.0                  # sideslip angle (deg)
gamma = 1.4                  # ratio of specific heats
R = 287.0                    # gas constant (J/kg/K)
atmos = 1
# Atmosphere models
if atmos == 1:
    # Indian atm model
    print("Using Indian atmosphere model")
else:
    # US Std atmosphere model
    print("Using US Standard atmosphere model")

# Calculations
temp = np.zeros_like(y)
pres = np.zeros_like(y)
dens = np.zeros_like(y)
avel = np.zeros_like(y)
vel = np.zeros_like(y)
dyn = np.zeros_like(y)
cpmax = np.zeros_like(y)
ipres = np.zeros_like(y)
ltemp = np.zeros_like(y)
lma = np.zeros_like(y)
lspres = np.zeros_like(y)
lpres = np.zeros_like(y)


# Loops to calculate profiles
for i in range(len(y)):
    te, p, den = indian(y[i])
    temp[i] = te[0]
    pres[i] = p[0]
    dens[i] = den[0]
    # Other calculations
    avel[i] = np.sqrt(gamma*R*temp[-1])
    vel[i] = m[i]*avel[i]
    dyn[i] = 0.5*dens[i]*vel[i]*vel[i]
    theta = (angle+alpha)*np.pi/180
    cpmax[i] = (pres[i] - lspres[i])/dyn[i]
    ipres[i] = dyn[i]*cpmax[i]*(np.cos(theta)**2) + pres[i]
    lma[i] = np.sqrt(((lspres[i]/lpres[i])**((gamma-1)/gamma))-1)*(2/(gamma-1))
    ltemp[i] = temp[i]*(1+(((gamma-1)/2)*m[i]*m[i]))

# Print outputs
# print("Altitude:", y)
print("Temperature:", temp)
print("Pressure:", pres)
print("Velocity:", vel)
print("Stagnation Temperature:", ltemp)

# Initialize empty lists to store data points
altitude_values = []
temperature_values = []
pressure_values = []
density_values = []

# Compute and collect data points for altitudes in steps of 100 up to the specified altitude
for alt_point in range(0, alt + 1, 100):
    te, p, den = indian(alt_point)
    altitude_values.append(alt_point)
    temperature_values.append(te)
    pressure_values.append(p)
    density_values.append(den)

# Create a plot for temperature vs. altitude
plt.figure(figsize=(8, 6))
plt.plot(altitude_values, temperature_values)
plt.xlabel('Altitude (m)')
plt.ylabel('Temperature (K)')
plt.title('Altitude vs. Temperature')
plt.grid(True)
plt.show()

# Create a plot for pressure vs. altitude
plt.figure(figsize=(8, 6))
plt.plot(altitude_values, pressure_values)
plt.xlabel('Altitude (m)')
plt.ylabel('Pressure (atm)')
plt.title('Altitude vs. Pressure')
plt.grid(True)
plt.show()

# Create a plot for density vs. altitude
plt.figure(figsize=(8, 6))
plt.plot(altitude_values, density_values)
plt.xlabel('Altitude (m)')
plt.ylabel('Density')
plt.title('Altitude vs. Density')
plt.grid(True)
plt.show()
