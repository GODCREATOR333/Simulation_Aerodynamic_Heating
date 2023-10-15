 print("Altitude vs Temperature:")
        print("\t".join([f"({alt}, {temp})" for alt,
              temp in altitude_temperature_points]))

        print("Altitude vs Pressure:")
        print("\t".join([f"({alt}, {press})" for alt,
              press in altitude_pressure_points]))

        print("Altitude vs Density:")
        print("\t".join([f"({alt}, {den})" for alt,
              den in altitude_density_points]))
        return altitude_temperature_points, altitude_pressure_points, altitude_density_points