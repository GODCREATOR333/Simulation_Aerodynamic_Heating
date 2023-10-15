from Trajectory1 import height_in_meters, mach, time1, time2, velocity
from std_atm_for_all import AtmosphericModel, alt
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


step1 = Step1()
temp_values = step1.get_temp_values()
pressure_values = step1.get_pressure_values()
density_values = step1.get_density_values()
speed_of_sound_values = step1.get_speed_of_sound_values()
time_values = time1
altitude_values = height_in_meters
velocity_values = velocity
mach_values = mach


length_of_temp_values = len(temp_values)
length_of_pressure_values = len(pressure_values)
length_of_density_values = len(density_values)
length_of_speed_of_sound_values = len(speed_of_sound_values)
length_of_time_values = len(time_values)
length_of_altitude_values = len(altitude_values)
length_of_velocity_values = len(velocity_values)
length_of_mach_values = len(mach_values)


print(f'length_of_temp_values: {length_of_temp_values}')
print(f'length_of_pressure_values : {length_of_pressure_values}')
print(f'length_of_density_values : {length_of_density_values}')
print(f'length_of_speed_of_sound_value : {length_of_speed_of_sound_values}')
print(f'length_of_time_values : {length_of_time_values}')
print(f'length_of_altitude_values : {length_of_altitude_values}')
print(f'length_of_velocity_values : {length_of_velocity_values}')
print(f'length_of_mach_values : {length_of_mach_values}')


print(f'The time values are: {time_values}')
print(f'The altitude values are: {altitude_values}')
print(f'The mach values are: {mach_values}')
print(f'The velocity values are: {velocity_values}')
print(f'The temperature values are: {temp_values}')
print(f'The pressure values are: {pressure_values}')
print(f'The density values are: {density_values}')
print(f'The speed of sound values are: {speed_of_sound_values}')
