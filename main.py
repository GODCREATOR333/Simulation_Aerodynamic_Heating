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


step1 = Step1()
temp_values = step1.get_temp_values()
pressure_values = step1.get_pressure_values()
density_values = step1.get_density_values()

print(f'The temperature values are: {temp_values}')
print(f'The pressure values are: {pressure_values}')
print(f'The density values are: {density_values}')
