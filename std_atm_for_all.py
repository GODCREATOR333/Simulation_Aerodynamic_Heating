import scipy.interpolate as interp
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style
from Trajectory1 import height_in_meters, velocity_values, time1, time2

alt = height_in_meters

print(Fore.RED + Style.BRIGHT +
      "Remember the maximum altitude for this simulation is 85000 meters to be accurate and within acceptable error.")


class AtmosphericModel:
    def __init__(self, alt):
        self.R = 8.3144598  # J/mol/K
        self.M = 0.0289644  # kg/mol (dry air)
        self.g = 9.80665  # m/s^2
        self.T0 = 288.15  # K (temperature at sea level)
        self.p0 = 1.01325  # atm (pressure at sea level)
        self.rho0 = 1.225  # kg/m^3 (density at sea level)
        self.altitudes = alt
        # creates altitude array from 0 to alt+1000(meters) in a step size of 1000meters

    def temperature_at_altitude(self, alt):
        h = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000, 95000]
        T = [288.15, 216.65, 216.65, 228.65,
             270.65, 270.65, 214.65, 214.65, 190]
        L = [-0.0065, 1e-9, 0.001, 0.0028, 1e-9, -0.0028, -0.002, -0.005, -0.005]

        for i in range(len(h) - 1):
            if alt >= h[i] and alt < h[i + 1]:
                return T[i] + L[i] * (alt - h[i])

        return np.nan

    def pressure_at_altitude(self, alt):
        L = -0.0065  # K/m (temperature lapse rate)
        T0_press = 288.15  # K (temperature at sea level)
        temp_press = self.T0 + L * alt
        epsilon = 1e-10
        L_pressure = -0.0065  # K/m (temperature lapse rate)
        te_safe = np.maximum(temp_press, epsilon)
        T0_safe = np.maximum(T0_press, epsilon)
        p = self.p0 * (te_safe / T0_safe) ** (-self.g *
                                              self.M / (self.R * L_pressure))
        return p

    def density_at_altitude(self, alt):
        t = self.temperature_at_altitude(alt)
        den = self.pressure_at_altitude(alt) * self.M / (self.R * t)
        return den

    def speed_of_sound(self, alt):
        t = self.temperature_at_altitude(alt)
        speed_of_sound = 19.935296 * (t ** 0.5)
        return speed_of_sound

    def calc_mach_values(self, alt):

        speed_of_sound_values = [self.speed_of_sound(h) for h in alt]
        mach_values = []
        for vel, sound_speed in zip(velocity_values, speed_of_sound_values):
            mach = vel / sound_speed
            mach_values.append(mach)
        return mach_values

    def std_international(self):
        temperature_values = [self.temperature_at_altitude(
            alt) for alt in self.altitudes]
        pressure_values = [self.pressure_at_altitude(
            alt) for alt in self.altitudes]
        density_values = [self.density_at_altitude(
            alt) for alt in self.altitudes]
        speed_of_sound_values = [
            self.speed_of_sound(alt)for alt in self.altitudes]  # this is require for plotting , since we are not plotting
        # now it is greyed out
        mach_values = self.calc_mach_values(self.altitudes)

        # Create subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

        # Plot Temperature vs. Altitude
        ax1.plot(self.altitudes, temperature_values)
        ax1.set_xlabel('Altitude (m)')
        ax1.set_ylabel('Temperature (K)')

        # Plot Pressure vs. Altitude
        ax2.plot(self.altitudes, pressure_values)
        ax2.set_xlabel('Altitude (m)')
        ax2.set_ylabel('Pressure (atm)')

        # Plot Density vs. Altitude
        ax3.plot(self.altitudes, density_values)
        ax3.set_xlabel('Altitude (m)')
        ax3.set_ylabel('Density (kg/m^3)')

        # Show the plot
        plt.tight_layout()
        #########################################
        #########################################
        plt.show()

    def plot_points(self):
        # Generate coordinate points for temperature, pressure, and density
        altitude_points = self.altitudes
        temperature_points = [self.temperature_at_altitude(
            alt) for alt in altitude_points]
        pressure_points = [self.pressure_at_altitude(
            alt) for alt in altitude_points]
        density_points = [self.density_at_altitude(
            alt) for alt in altitude_points]
        speed_of_sound_points = [self.speed_of_sound(
            alt)for alt in altitude_points]
        mach_points = self.calc_mach_values(altitude_points)

        # Prepare coordinate points for the three plots
        altitude_temperature_points = list(
            zip(altitude_points, temperature_points))
        altitude_pressure_points = list(zip(altitude_points, pressure_points))
        altitude_density_points = list(zip(altitude_points, density_points))
        altitude_sound_speed_points = list(
            zip(altitude_points, speed_of_sound_points))
        altitude_mach_points = list(
            zip(altitude_points, mach_points))

        #################################################################################################
        #################################################################################################
        # Print the coordinate points in list form
        # print("Altitude vs Temperature:")
        # for alt, temp in zip(altitude_points, temperature_points):
        #     print(f"Altitude: {alt} m, Temperature: {temp} K")

        # print("Altitude vs Pressure:")
        # for alt, press in zip(altitude_points, pressure_points):
        #     print(f"Altitude: {alt} m, Pressure: {press} atm")

        # print("Altitude vs Density:")
        # for alt, den in zip(altitude_points, density_points):
        #     print(f"Altitude: {alt} m, Density: {den} kg/m^3")

        print("Altitude vs Speed of Sound:")
        for alt, sound_speed in zip(altitude_points, speed_of_sound_points):
            print(
                f"Altitude: {alt} m, Speed of sound: {sound_speed} m/sec")

        #####################################################################################################
        #####################################################################################################
        # Print the coordinate points in (x,Y) form
        # print("Altitude vs Temperature:")
        # print("\t".join([f"({alt}, {temp})" for alt,
        #       temp in altitude_temperature_points]))

        # print("Altitude vs Pressure:")
        # print("\t".join([f"({alt}, {press})" for alt,
        #       press in altitude_pressure_points]))

        # print("Altitude vs Density:")
        # print("\t".join([f"({alt}, {den})" for alt,
        #       den in altitude_density_points]))

        # print("Altitude vs Speed of sound:")
        # print("\t".join([f"({alt}, {sound_speed})" for alt,
        #       sound_speed in altitude_sound_speed_points]))

        print("Velocity vs Mach:")
        for vel, mach in zip(velocity_values, mach_points):
            print(f"Velocity: {vel}, Mach: {mach}")

        return altitude_temperature_points, altitude_pressure_points, altitude_density_points, mach_points


# Create an instance of the AtmosphericModel class
atmosphere = AtmosphericModel(alt)
# Call std_international to perform calculations and plotting
atmosphere.std_international()

atmosphere.plot_points()

mach = atmosphere.calc_mach_values(alt)
print(f'length of mach : {len(mach)}')
# print(f'mach-values = == {mach}')


# Time vs Altitude
plt.subplot(2, 2, 1)
plt.plot(time1, height_in_meters)
plt.title('Time vs Altitude')
plt.xlabel('Time (sec)')
plt.ylabel('Altitude (m)')

# Time vs Mach Number
plt.subplot(2, 2, 2)
plt.plot(time1, mach)
plt.title('Time vs Mach Number')
plt.xlabel('Time (sec)')
plt.ylabel('Mach Number')
plt.tight_layout()
plt.show()
