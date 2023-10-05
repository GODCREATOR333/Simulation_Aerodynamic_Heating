import numpy as np
import matplotlib.pyplot as plt


def indian(alt):
    g = 9.78852
    r = 287.05307
    to = 303.15
    po = 100500
    rnot = 1.15491
    alt = alt

    if alt < 16000:
        c = -0.0065
        te = to + (c * (alt - 0))
        sl = -(g / (c * r))
        p = po * ((te / to) ** sl)
        s2 = -((g / (c * r)) + 1)
        den = rnot * ((te / to) ** s2)
    elif alt > 16000 and alt < 46000:
        c = 0.0023
        t1 = 199.0
        te = t1 + (c * (alt - 16000))
        sl = -(g / (c * r))
        p1 = 11045
        p = p1 * ((te / t1) ** sl)
        s2 = -((g / (c * r)) + 1)
        d1 = 0.1933
        den = d1 * ((te / t1) ** s2)
    elif alt > 46000 and alt <= 52000:
        te = 268.0
        p1 = 133.77
        p = p1 * (2.71828 ** (-(g / (r * te)) * (alt - 46000)))
        d1 = 0.0017
        den = d1 * (p / p1)
    elif alt > 52000 and alt < 75000:
        c = -0.003
        t1 = 268
        te = t1 + (c * (alt - 52000))
        s1 = -(g / (c * r))
        p1 = 62.3453
        p = p1 * ((te / t1) ** s1)
        s2 = -((g / (c * r)) + 1)
        d1 = 0.00077
        den = d1 * ((te / t1) ** s2)
    elif alt > 75000 and alt < 80000:
        te = 199.0
        pl = 2.1149
        p = pl * (2.71828 ** (-(g / (r * te)) * (alt - 75000)))
        dl = -0.000035
        den = dl * (p / pl)
    else:
        # Default values if none of the conditions match
        te = 0
        p = 0
        den = 0

    return te, p, den


te, p, den = indian(50000)
print("te=", te)
print("p=", p)
print("den=", den)


# # Initialize empty lists to store data points
# altitude_values = []
# temperature_values = []
# pressure_values = []
# density_values = []

# # Compute and collect data points for altitudes in steps of 100 up to the specified altitude
# for alt_point in range(0, alt + 1, 100):
#     te, p, den = indian(alt_point)
#     altitude_values.append(alt_point)
#     temperature_values.append(te)
#     pressure_values.append(p)
#     density_values.append(den)

# # Create a plot for temperature vs. altitude
# plt.figure(figsize=(8, 6))
# plt.plot(altitude_values, temperature_values)
# plt.xlabel('Altitude (m)')
# plt.ylabel('Temperature (K)')
# plt.title('Altitude vs. Temperature')
# plt.grid(True)
# plt.show()

# # Create a plot for pressure vs. altitude
# plt.figure(figsize=(8, 6))
# plt.plot(altitude_values, pressure_values)
# plt.xlabel('Altitude (m)')
# plt.ylabel('Pressure (atm)')
# plt.title('Altitude vs. Pressure')
# plt.grid(True)
# plt.show()

# # Create a plot for density vs. altitude
# plt.figure(figsize=(8, 6))
# plt.plot(altitude_values, density_values)
# plt.xlabel('Altitude (m)')
# plt.ylabel('Density')
# plt.title('Altitude vs. Density')
# plt.grid(True)
# plt.show()
