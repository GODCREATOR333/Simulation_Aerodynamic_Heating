from Trajectory1 import mach_values_ms
import numpy as np
from std_atm_for_all import AtmosphericModel, alt
model = AtmosphericModel(alt)
altitudes = model.altitudes
mach_array = mach_values_ms


class FlowParameters:
    def __init__(self):
        self.R = 8.3144598  # J/mol/K
        self.M = 0.0289644  # kg/mol (dry air)
        self.g = 9.80665  # m/s^2
        self.gamma = 1.4
        self.sound_speed_values = model.speed_of_sound

    def stag_temp_ratio(self, mach):
        if mach < 85:
            return 1 + 0.5 * (self.gamma - 1) * mach ** 2
        else:
            return (self.gamma + 1) * (mach ** 2) / ((2 * self.gamma * (mach ** 2)) - (self.gamma - 1))

    def stag_press_ratio(self, mach):
        if mach < 5:
            return (1 + 0.5 * (self.gamma - 1) * mach ** 2) ** (self.gamma / (self.gamma - 1))
        else:
            return (2 * self.gamma * mach ** 2 - (self.gamma - 1)) / (self.gamma + 1)

    def stag_vel_ratio(self, mach):
        stag_temp_ratio = self.stag_temp_ratio(mach)
        return np.sqrt(stag_temp_ratio)

    def stag_mach_ratio(self, mach):
        if mach < 5:
            return 1
        else:
            return np.sqrt(((self.gamma + 1) * mach ** 2) / (2 * self.gamma * mach ** 2 - (self.gamma - 1)))

    def stag_den_ratio(self, mach):
        if mach < 5:
            return 1 / (1 + 0.5 * (self.gamma - 1) * mach ** 2)
        else:
            return (1 + (self.gamma-1) * (mach ** 2)/2) ** (1/(self.gamma - 1))

    def free_stream_mach_cube(self, stag_mach_ratio, mach):
        return (stag_mach_ratio*mach) ** 3

    def get_free_stream_mach_values(self, stag_mach_ratio, mach):
        return (stag_mach_ratio*mach)


# Create an instance of FlowParameters
flow_parameters = FlowParameters()

# Calculate the parameters for each mach_value in mach_array
stag_temp_ratios = [flow_parameters.stag_temp_ratio(
    mach_value) for mach_value in mach_array]
stag_press_ratios = [flow_parameters.stag_press_ratio(
    mach_value) for mach_value in mach_array]
stag_vel_ratios = [flow_parameters.stag_vel_ratio(
    mach_value) for mach_value in mach_array]
stag_mach_ratios = [flow_parameters.stag_mach_ratio(
    mach_value) for mach_value in mach_array]
stag_den_ratios = [flow_parameters.stag_den_ratio(
    mach_value) for mach_value in mach_array]


# calculate the free stream parameters
free_stream_mach_values_cube = [flow_parameters.free_stream_mach_cube(
    stag_mach_value, mach_value) for stag_mach_value, mach_value in zip(stag_mach_ratios, mach_array)]
free_stream_mach_values = [flow_parameters.free_stream_mach_cube(
    stag_mach_value, mach_value) for stag_mach_value, mach_value in zip(stag_mach_ratios, mach_array)]

# Get the lengths of the calculated arrays
length_of_stag_temp_ratios = len(stag_temp_ratios)
length_of_stag_press_ratios = len(stag_press_ratios)
length_of_stag_vel_ratios = len(stag_vel_ratios)
length_of_stag_mach_ratios = len(stag_mach_ratios)
length_of_stag_den_ratios = len(stag_den_ratios)
length_of_free_stream_mach_values_cube = len(free_stream_mach_values_cube)

# Print the calculated parameters and their lengths
print("Length of Stagnation Temperature Ratios:", length_of_stag_temp_ratios)
print("Length of Stagnation Pressure Ratios:", length_of_stag_press_ratios)
print("Length of Stagnation Velocity Ratios:", length_of_stag_vel_ratios)
print("Length of Stagnation Mach Ratios:", length_of_stag_mach_ratios)
print("Length of Stagnation Density Ratios:", length_of_stag_den_ratios)
print("Length of free_stream_mach_values_cube:",
      length_of_free_stream_mach_values_cube)

print("Stagnation Temperature Ratios:", stag_temp_ratios)
# print("Stagnation Pressure Ratios:", stag_press_ratios)
# print("Stagnation Velocity Ratios:", stag_vel_ratios)
# print("Stagnation Mach Ratios:", stag_mach_ratios)
# print("Stagnation Density Ratios:", stag_den_ratios)
# print("free stream mach values cube:", free_stream_mach_values_cube)
