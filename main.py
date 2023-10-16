from Trajectory1 import height_in_meters, mach, time1, time2, velocity
from std_atm_for_all import AtmosphericModel, alt
from flow_parameters_calcs import FlowParameters, flow_parameters
from flow_parameters_calcs import stag_den_ratios, stag_temp_ratios, stag_press_ratios, stag_mach_ratios, stag_vel_ratios, free_stream_mach_values_cube
model = AtmosphericModel(alt)
altitudes = model.altitudes


class Step1:
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


class Step2:  # calculating the flow parameters for step 2

    @staticmethod
    def get_free_stream_temp_values():
        free_stream_temp_values = []
        for stag_temp_ratio, sound_speed_value in zip(stag_temp_ratios, speed_of_sound_values):
            values = (stag_temp_ratio)*((sound_speed_value/49.02)**2)
            values_in_celsius = (values-491.67)*5/9
            free_stream_temp_values.append(values_in_celsius)
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
    def get_free_stream_velocity_values(mach_values):
        free_stream_velocity_values = []
        for stag_velocity_ratio, speed_of_sound_value, mach in zip(stag_vel_ratios, speed_of_sound_values, mach_values):
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


step1 = Step1()
temp_values = step1.get_temp_values()
pressure_values = step1.get_pressure_values()
density_values = step1.get_density_values()
speed_of_sound_values = step1.get_speed_of_sound_values()
time_values = time1
altitude_values = height_in_meters
velocity_values = velocity
mach_values = mach


step2 = Step2()
free_stream_temp_values = step2.get_free_stream_temp_values()
free_stream_den_values = step2.get_free_stream_density_values()
free_stream_spees_of_sound_values = step2.get_free_stream_speed_of_sound_values_cube()
free_stream_velocity_values = step2.get_free_stream_velocity_values(
    mach_values)
free_stream_viscosity_values = step2.get_free_stream_coefficient_of_viscosity_values()
free_stream_reynolds_values = step2.get_free_stream_reynolds_number_values()


length_of_temp_values = len(temp_values)
length_of_pressure_values = len(pressure_values)
length_of_density_values = len(density_values)
length_of_speed_of_sound_values = len(speed_of_sound_values)
length_of_time_values = len(time_values)
length_of_altitude_values = len(altitude_values)
length_of_velocity_values = len(velocity_values)
length_of_mach_values = len(mach_values)
length_of_free_stream_temp_values = len(free_stream_temp_values)
length_of_free_stream_density_values = len(free_stream_den_values)
length_of_free_stream_speed_of_sound_values = len(
    free_stream_spees_of_sound_values)
length_of_free_stream_velocity_values = len(free_stream_velocity_values)
length_of_free_stream_reynolds_values = len(free_stream_reynolds_values)
length_of_free_stream_viscosity_values = len(free_stream_viscosity_values)


print(f'length_of_temp_values: {length_of_temp_values}')
print(f'length_of_pressure_values : {length_of_pressure_values}')
print(f'length_of_density_values : {length_of_density_values}')
print(f'length_of_speed_of_sound_value : {length_of_speed_of_sound_values}')
print(f'length_of_time_values : {length_of_time_values}')
print(f'length_of_altitude_values : {length_of_altitude_values}')
print(f'length_of_velocity_values : {length_of_velocity_values}')
print(f'length_of_mach_values : {length_of_mach_values}')
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


# print(f'The time values are: {time_values}')
# print(f'The altitude values are: {altitude_values}')
# print(f'The mach values are: {mach_values}')
# print(f'The velocity values are: {velocity_values}')
# print(f'The temperature values are: {temp_values}')
# print(f'The pressure values are: {pressure_values}')
# print(f'The density values are: {density_values}')
# print(f'The speed of sound values are: {speed_of_sound_values}')
# print("Stagnation Pressure Ratios:", stag_press_ratios)
