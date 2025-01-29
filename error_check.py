import math
from Trajectory1 import mach
from flow_parameters_calcs import FlowParameters
FlowParameters = FlowParameters()

# Constants
gamma = 1.4  # Ratio of specific heats for air

# Provided Mach numbers
mach_numbers = mach
# Provided calculated values
# Provided calculated values
stagnation_temp_ratios = [
    FlowParameters.stag_temp_ratio(Mo) for Mo in mach_numbers]
stagnation_pressure_ratios = [
    FlowParameters.stag_press_ratio(Mo) for Mo in mach_numbers]
stagnation_velocity_ratios = [
    FlowParameters.stag_vel_ratio(Mo) for Mo in mach_numbers]
stagnation_mach_ratios = [
    FlowParameters.stag_mach_ratio(Mo) for Mo in mach_numbers]
stag_den_ratios = [FlowParameters.stag_den_ratio(Mo) for Mo in mach_numbers]


# Initialize lists to store calculated values
calc_stagnation_temp_ratios = []
calc_stagnation_pressure_ratios = []
calc_stagnation_velocity_ratios = []
calc_stagnation_mach_ratios = []
calc_stagnation_den_ratios = []

for Mo in mach_numbers:
    if Mo < 5:  # Iterate through mach_numbers, not 'mach'
        # Calculate values for Mo < 5
        T_T0 = 1 + 0.5 * (gamma - 1) * Mo ** 2
        P_inf_P0 = (1 + 0.5 * (gamma - 1) * Mo ** 2) ** (gamma / (gamma - 1))
        V_V0 = math.sqrt(T_T0)
        M_M0 = 1
        rho_inf_rho0 = 1 / (1 + 0.5 * (gamma - 1) * Mo ** 2)
    else:
        # Calculate values for Mo > 5
        M_M0 = math.sqrt(((gamma + 1) * Mo ** 2) /
                         (2 * gamma * Mo ** 2 - (gamma - 1)))
        P_inf_P0 = (2 * gamma * Mo ** 2 - (gamma - 1)) / (gamma + 1)
        T_T0 = ((gamma + 1) * Mo ** 2) / (2 * gamma * Mo ** 2 - (gamma - 1))
        V_V0 = math.sqrt(T_T0)
        rho_inf_rho0 = (1 + (gamma - 1) * Mo ** 2 / 2) ** (1 / (gamma - 1))

    # Append calculated values to lists
    calc_stagnation_temp_ratios.append(T_T0)
    calc_stagnation_pressure_ratios.append(P_inf_P0)
    calc_stagnation_velocity_ratios.append(V_V0)
    calc_stagnation_mach_ratios.append(M_M0)
    calc_stagnation_den_ratios.append(rho_inf_rho0)

# Check if the calculated values match the provided values
temp_match = all(abs(calc - provided) < 1e-10 for calc,
                 provided in zip(calc_stagnation_temp_ratios, stagnation_temp_ratios))
pressure_match = all(abs(calc - provided) < 1e-10 for calc, provided in zip(
    calc_stagnation_pressure_ratios, stagnation_pressure_ratios))
velocity_match = all(abs(calc - provided) < 1e-10 for calc, provided in zip(
    calc_stagnation_velocity_ratios, stagnation_velocity_ratios))
mach_match = all(abs(calc - provided) < 1e-10 for calc,
                 provided in zip(calc_stagnation_mach_ratios, stagnation_mach_ratios))
den_match = all(abs(calc - provided) < 1e-10 for calc,
                provided in zip(calc_stagnation_den_ratios, stag_den_ratios))

temp_match, pressure_match, velocity_match, mach_match


print("Stagnation Temperature Ratios Match:", temp_match)
print("Stagnation Pressure Ratios Match:", pressure_match)
print("Stagnation Velocity Ratios Match:", velocity_match)
print("Stagnation Mach Ratios Match:", mach_match)
print("Stagnation den Ratios Match:", den_match)
