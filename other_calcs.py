
class materials_props:

    def __init__(self):

        # Material Properties from experimentally collected data
        self.T = [460, 560, 660, 760, 860, 960, 1060, 1160, 1260,
                  1360, 1395, 1460, 1560, 1660, 1760, 1860, 1960, 2060]  # temp in degree rankine

        self.Cp = [0.1032, 0.1065, 0.1095, 0.113, 0.1161, 0.1195, 0.1213, 0.124, 0.1265, 0.1284, 0.1289, 0.1361, 0.1375,
                   0.1396, 0.1419, 0.1449, 0.1475, 0.1505]  # specific heat in BTU/lb-R

    def temp_convert(self):
        temp_kelvin = []
        for t in self.T:
            temp_k = [(t - 491.67) * (5/9)]
            temp_kelvin.append(temp_k)
        return temp_kelvin

    def Cp_convert(self):
        Cp_SI = []
        for cp in self.Cp:
            cp_in_si = [cp * 2326]
            Cp_SI.append(cp_in_si)
        return Cp_SI


material = materials_props()
temp_mp = material.temp_convert()
Cp_mp = material.Cp_convert()

print(f'Temperature values : {(temp_mp,2)}')
print(f'Cp values  : {(Cp_mp)}')


# Prandtl Number data
temperature_for_Pr_number = []
