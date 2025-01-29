
from Trajectory1 import mach_values_ms
from std_atm_for_all import AtmosphericModel
from Trajectory1 import height_in_meters,  time1, velocity_values, mach_values_ms
from std_atm_for_all import AtmosphericModel, alt
from flow_parameters_calcs import FlowParameters, flow_parameters
import matplotlib.pyplot as plt
import numpy as np
from flow_parameters_calcs import stag_den_ratios, stag_temp_ratios, stag_press_ratios, stag_mach_ratios, stag_vel_ratios, free_stream_mach_values_cube, free_stream_mach_values
model = AtmosphericModel(alt)
altitudes = model.altitudes
gamma = 1.4
R = 287


class Step1():
    # Get temp values for all altitude points
    @staticmethod
    def get_temp_values():
        temp_values = []
        for alt in altitudes:
            temp = model.temperature_at_altitude(alt)
            temp_values.append(temp)
        return temp_values

    # Get pressure values for all altitude points
    @staticmethod
    def get_pressure_values():
        pressure_values = []
        for alt in altitudes:
            press = model.pressure_at_altitude(alt)
            pressure_values.append(press)
        return pressure_values

    # Get density values for all altitude points
    @staticmethod
    def get_density_values():
        density_values = []
        for alt in altitudes:
            dens = model.density_at_altitude(alt)
            density_values.append(dens)
        return density_values

    @staticmethod
    def get_speed_of_sound_values():
        speed_of_sound = []
        for alt in altitudes:
            sound_speed = model.speed_of_sound(alt)
            speed_of_sound.append(sound_speed)
        return speed_of_sound


step1 = Step1()
temp_values = step1.get_temp_values()
pressure_values = step1.get_pressure_values()
density_values = step1.get_density_values()
speed_of_sound_values = step1.get_speed_of_sound_values()
time_values = time1
altitude_values = height_in_meters
velocity_values = velocity_values
mach_values = mach_values_ms

length_of_temp_values = len(temp_values)
length_of_pressure_values = len(pressure_values)
length_of_density_values = len(density_values)
length_of_speed_of_sound_values = len(speed_of_sound_values)
length_of_time_values = len(time_values)
length_of_altitude_values = len(altitude_values)
length_of_velocity_values = len(velocity_values)
length_of_mach_values = len(mach_values_ms)


##### Step 1 ######

print(f'length_of_temp_values: {length_of_temp_values}')
print(f'length_of_pressure_values : {length_of_pressure_values}')
print(f'length_of_density_values : {length_of_density_values}')
print(f'length_of_speed_of_sound_value : {length_of_speed_of_sound_values}')
print(f'length_of_time_values : {length_of_time_values}')
print(f'length_of_altitude_values : {length_of_altitude_values}')
print(f'length_of_velocity_values : {length_of_velocity_values}')
print(f'length_of_mach_values : {length_of_mach_values}')


class Step2():  # calculating the flow parameters for step 2

    @staticmethod
    def get_free_stream_temp_values():
        free_stream_temp_values = []
        for stag_temp_ratio, sound_speed_value in zip(stag_temp_ratios, speed_of_sound_values):
            # convert speed of sound from m/sec to ft/sec
            values = (1) * (((sound_speed_value/0.3048)/49.02)**2)
            # convert the values from degree rankine to degree kelvin
            values_in_kelvin = (values/1.8)
            free_stream_temp_values.append(values_in_kelvin)
        return free_stream_temp_values

    @staticmethod
    def get_free_stream_density_values():
        free_stream_density_values = []
        for stag_den_ratio, density_value in zip(stag_den_ratios, density_values):
            den_values = (stag_den_ratio*density_value)
            free_stream_density_values.append(den_values)
        return free_stream_density_values

    @staticmethod
    def get_free_stream_speed_of_sound_values_cube():
        free_stream_speed_of_sound_values_cube = []
        for free_stream_temp_value in free_stream_temp_values:
            free_sound_cube_values = (
                (49.02**3)*(free_stream_temp_value**3/2)*0.3048)
            free_stream_speed_of_sound_values_cube.append(
                free_sound_cube_values)
        return free_stream_speed_of_sound_values_cube

    @staticmethod
    def get_free_stream_velocity_values(mach_values_ms):
        free_stream_velocity_values = []
        for stag_velocity_ratio, speed_of_sound_value, mach in zip(stag_vel_ratios, speed_of_sound_values, mach_values_ms):
            free_velocity_values = (
                stag_velocity_ratio*mach*speed_of_sound_value)
            free_stream_velocity_values.append(free_velocity_values)
        return free_stream_velocity_values

    @staticmethod
    def get_free_stream_coefficient_of_viscosity_values():
        free_stream_coefficient_of_viscosity_values = []
        for free_stream_temp_value in free_stream_temp_values:
            mu = 1.716 * 10**-5 * (free_stream_temp_value/288.15)**(3/2) * \
                ((288.15 + 110.4)/(free_stream_temp_value + 110.4))
            free_stream_coefficient_of_viscosity_values.append(mu)
        return free_stream_coefficient_of_viscosity_values

    @staticmethod
    def get_free_stream_reynolds_number_values():
        L = 10
        free_stream_reynolds_number_values = []
        for free_den_value, free_vel_value, free_viscosity_value in zip(free_stream_den_values, free_stream_velocity_values, free_stream_viscosity_values):
            rey_values = (
                ((free_den_value*free_vel_value*L)/free_viscosity_value))  # L is the Dimension L in meters  from body details, For Now let L =10 meters
            free_stream_reynolds_number_values.append(rey_values)
        return free_stream_reynolds_number_values


step2 = Step2()
free_stream_temp_values = step2.get_free_stream_temp_values()
free_stream_den_values = step2.get_free_stream_density_values()
free_stream_spees_of_sound_values = step2.get_free_stream_speed_of_sound_values_cube()
free_stream_velocity_values = step2.get_free_stream_velocity_values(
    mach_values_ms)
free_stream_viscosity_values = step2.get_free_stream_coefficient_of_viscosity_values()
free_stream_reynolds_values = step2.get_free_stream_reynolds_number_values()


length_of_free_stream_temp_values = len(free_stream_temp_values)
length_of_free_stream_density_values = len(free_stream_den_values)
length_of_free_stream_speed_of_sound_values = len(
    free_stream_spees_of_sound_values)
length_of_free_stream_velocity_values = len(free_stream_velocity_values)
length_of_free_stream_reynolds_values = len(free_stream_reynolds_values)
length_of_free_stream_viscosity_values = len(free_stream_viscosity_values)


# ##### Step 2 #####
print(
    f'length_of_free_stream_temp_values : {length_of_free_stream_temp_values}')
print(
    f'length_of_free_stream_density_values : {length_of_free_stream_density_values}')
print(
    f'length_of_free_stream_speed_of_sound_values  : {length_of_free_stream_speed_of_sound_values }')
print(
    f'length_of_free_stream_velocity_values : {length_of_free_stream_velocity_values}')
print(
    f'length_of_free_stream_reynolds_values : {length_of_free_stream_reynolds_values}')
print(
    f'length_of_free_stream_viscosity_values : {length_of_free_stream_viscosity_values}')


class Step3:

    # @staticmethod
    # def get_stag_temp_value_1():
    #     stag_temp_values = []
    #     for stag_temp_ratio, free_temp_value, free_stream_mach_value in zip(stag_temp_ratios, free_stream_temp_values, free_stream_mach_values):
    #         temp_value = (free_temp_value*(1+(gamma-1)/2)
    #                       * free_stream_mach_value**2)
    #         stag_temp_values.append(temp_value)
    #     return stag_temp_values

    @staticmethod
    def get_stag_temp_value_2():
        stag_temp_values = []
        for stag_temp_ratio, free_temp_value, free_stream_mach_value in zip(stag_temp_ratios, free_stream_temp_values, free_stream_mach_values):
            temp_value = (free_temp_value*(1/stag_temp_ratio))
            stag_temp_values.append(temp_value)
        return stag_temp_values

    # @staticmethod
    # def get_stag_temp_value_3():
    #     stag_temp_values = []
    #     for vel, free_temp_value in zip(velocity_values, free_stream_temp_values):
    #         cp = 1004.5
    #         temp_value = (free_temp_value)+((vel**2)/(2*cp))
    #         stag_temp_values.append(temp_value)
    #     return stag_temp_values

    @staticmethod
    def get_stag_temp_rise_1():
        stag_temp_rise = []
        for free_temp_value, stag_temp_value in zip(free_stream_temp_values, stag_temp_values):
            temp_rise = stag_temp_value-free_temp_value
            stag_temp_rise.append(temp_rise)
        return stag_temp_rise


step3 = Step3()
stag_temp_values = step3.get_stag_temp_value_2()
stag_temp_rise = step3.get_stag_temp_rise_1()
length_of_stag_temp_values = len(stag_temp_values)
##### Step 3 #####
print(
    f'length_of_stag_temp_values : {length_of_stag_temp_values}')


# class Step3_1():

#     @staticmethod
#     def get_infinitesimal_temp_values():
#         T_infinitesimal = []

#         for i in range(len(free_stream_temp_values)):

#             T_free_i = free_stream_temp_values[i]
#             T0_i = stag_temp_values[i]

#             intermediate_T = []  # store 100 values for this pair

#             for fraction in np.linspace(0, 1, num=100):

#                 T = T_free_i + (T0_i - T_free_i)*fraction
#                 intermediate_T.append(T)

#             # add this pair's 100 values to full list
#             T_infinitesimal.extend(intermediate_T)

#         return T_infinitesimal

#     # @staticmethod
#     # def get_variable_Cp_values(free_stream_temp_values, stag_temp_values):
#     #     T_values = np.arange(free_stream_temp_values, stag_temp_values + 1)
#     #     Cp_avg = (1 / (stag_temp_values - free_stream_temp_values)) * \
#     #         np.trapz(Cp(T_values), dx=1)
#     #     return Cp_avg
#     # # Calculate average Cp for each pair of T_inf and T0 values
#     # for T_inf, T0 in zip(free_stream_temp_values, stag_temp_values):
#     #     Cp_avg = get_variable_Cp_values(
#     #         free_stream_temp_values, stag_temp_values)
#     #     print(
#     #         f"For free stream temp values = {free_stream_temp_values} K and stag temp values = {stag_temp_ratios} K, Average Cp = {Cp_avg} kJ/kg-K")


# step3_1 = Step3_1()
# T_infinitesimal = step3_1.get_infinitesimal_temp_values()
# length_of_infinitesimal_temp_values = len(T_infinitesimal)
# print(
#     f"length of Infinitesimal Temperature values : { length_of_infinitesimal_temp_values}")


class Step3_2:
    def __init__(self):
        self.coefficients = {
            'A': 28.11,
            'B': 0.1967,
            'C': 0.4802,
            'D': -0.1743,
            'E': 0.02279,
            'F': -1.447e-05,
            'G': 2.947e-09
        }

    def calculate_avg_Cp_values(self):
        T_infinitesimal = step2.get_free_stream_temp_values()
        A = self.coefficients['A']
        B = self.coefficients['B']
        C = self.coefficients['C']
        D = self.coefficients['D']
        E = self.coefficients['E']
        F = self.coefficients['F']
        G = self.coefficients['G']

        avg_Cp_values = []

        # Function to calculate Cp(T) for air
        def Cp_air(T):
            return A + B * T + C * T**2 + D * T**3 + E * T**4 + F * T**5 + G * T**6

        avg_Cp_values = [Cp_air(T) for T in T_infinitesimal]

        return avg_Cp_values


step3_2 = Step3_2()
infinitesimal_Cp_values = step3_2.calculate_avg_Cp_values()

length_of_Cp_values = len(infinitesimal_Cp_values)
print(f'length of infinitesimal cp values : {length_of_Cp_values}')


# class Step3_3:
#     def get_Cp_values(self, infinitesimal_Cp_values, T_infinitesimal, stag_temp_values, free_stream_temp_values):
#         total_integrals = []  # Initialize the list to store individual integrals

#         for i in range(0, len(T_infinitesimal), 100):
#             T_inf_subset = T_infinitesimal[i:i+100]
#             C_p_subset = infinitesimal_Cp_values[i:i+100]

#             # Calculate the average Cp for this pair
#             T0_i = stag_temp_values[i // 100]  # Index conversion
#             T_free_i = free_stream_temp_values[i // 100]  # Index conversion
#             sum_of_cp_in_a_subset = sum(C_p_subset)

#             Cp_avg = sum_of_cp_in_a_subset / len(C_p_subset)

#             # Calculate the step size for this subset
#             step_size = T_inf_subset[1] - T_inf_subset[0]

#             # Initialize the integral for this subset
#             subset_integral = 0

#             # Integrate using the trapezoidal rule for this subset
#             for j in range(1, len(T_inf_subset) - 1):
#                 subset_integral += 0.5 * (Cp_avg + Cp_avg) * step_size

#             # Add the integral for this subset to the list
#             total_integrals.append(subset_integral)

#         return total_integrals


# step3_3 = Step3_3()  # Create an instance of the Step3_3 class
# Cp_values = step3_3.get_Cp_values(
#     infinitesimal_Cp_values, T_infinitesimal, stag_temp_values, free_stream_temp_values)

# length_of_cp_values = len(Cp_values)

# print(f'Length of Cp values: {length_of_cp_values}')
# print(f'Cp values: {Cp_values}')


class Step3_4:
    def get_stag_temp_rise_from_Cp(self, free_stream_velocity_values, infinitesimal_Cp_values):
        stagnation_temperature_rises = []

        for velocity, final_cp in zip(free_stream_velocity_values, infinitesimal_Cp_values):
            delta_t0oo = 0.5 * ((velocity ** 2) / (4.186*9.81*final_cp))
            stagnation_temperature_rises.append(delta_t0oo)

        return stagnation_temperature_rises


step3_4 = Step3_4()
stagnation_temperature_rises = step3_4.get_stag_temp_rise_from_Cp(
    free_stream_velocity_values, infinitesimal_Cp_values)
# print(f'Stagnation Temperature Rises: {stagnation_temperature_rises}')


class Step3_5:
    @staticmethod
    def plot_stag_temp_rise_vs_velocity():
        plt.figure(figsize=(10, 12))
        plt.plot(velocity_values, stag_temp_rise)
        plt.xlabel('Free Stream Velocity (m/s)')
        plt.ylabel('Stagnation Temperature Rise (K)')
        plt.title('Stagnation Temperature Rise vs Free Stream Velocity')
        plt.grid(True)
        plt.show()


step3_5 = Step3_5()
step3_5.plot_stag_temp_rise_vs_velocity()


# print(f'The time values are: {time_values}')
# print(f'The altitude values are: {altitude_values}')
# print(f'The velocity values are: {velocity_values}')
# print(f'The temperature values are: {temp_values}')
# print(f'The pressure values are: {pressure_values}')
# print(f'The density values are: {density_values}')
# print(f'The speed of sound values are: {speed_of_sound_values}')
# print("Stagnation Pressure Ratios:", stag_press_ratios)
# print(f'The mach values are: {mach_values}')

# print(f'stag_temp_ratios : {stag_temp_ratios}')
print(f'Free_stream_temp_values : {free_stream_temp_values}')
print(f'stag_temp_values : {stag_temp_values}')
# print(f'Cp values {infinitesimal_Cp_values}')
# print(f'Infinitesimal Temp values = {T_infinitesimal}')
# print(f"Average Cp values: {avg_Cp_values}")
# print(f'stag temp rise values : {stag_temp_rise}')

# print(f'Free_stream_velocity_values : {free_stream_velocity_values}')
