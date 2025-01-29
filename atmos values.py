from CoolProp.CoolProp import PropsSI
import numpy as np
from pygasflow import isentropic_solver
import main
from main import Step1
step1 = Step1()
speed_of_sound = step1.get_speed_of_sound_values


class FlowParams:

    def __init__(self, gamma=1.4):
        self.gamma = gamma

    def calc_flow_parameters(self, Ms):
        results = isentropic_solver("m", Ms, self.gamma)
        self.stag_press_ratios = results[1]
        self.stag_dens_ratios = results[2]
        self.stag_temp_ratios = results[3]
        return results


class CheckValues:

    def __init__(self, flow_params):
        self.flow_params = flow_params

    def get_free_stream_temp(self, speed_of_sound):
        stag_temp_ratios = self.flow_params.stag_temp_ratios
        free_stream_temps = []
        for ratio, speed in zip(stag_temp_ratios, speed_of_sound):
            temp = ratio * ((speed/0.3048)/49.02)**2
            temp_k = temp/1.8
            free_stream_temps.append(temp_k)
        return free_stream_temps


class StagValues:

    def __init__(self, flow_params, check_values):
        self.flow_params = flow_params
        self.check_values = check_values

    def get_stag_temp_values(self):
        stag_temp_ratios = self.flow_params.stag_temp_ratios
        free_stream_temps = self.check_values.get_free_stream_temp(
            speed_of_sound())
        stag_temp_values = []
        for ratio, temp in zip(stag_temp_ratios, free_stream_temps):
            stag_temp = temp * (1/ratio)
            stag_temp_values.append(stag_temp)
        return stag_temp_values


# Example usage
fp = FlowParams()
cv = CheckValues(fp)
Ms = [0.08878709624796989, 0.09828388233718056, 0.8655007122248444, 0.4904194172916039,
      0.33206310479281426, 0.2456384121308542, 1.304242267120109, 0.25749957688180675,
      0.8102379638739878, 0.4735412124871189, 1.5811627110238007, 0.4758364530853777,
      1.7869336669624487, 0.3584400194098129, 0.7652577626947569, 1.9178090321358483,
      1.1545163586080964, 1.702447568227736, 2.050688668645083, 1.1670276533786088,
      2.4104346891613235, 2.8208945161747137, 3.387887413803752, 1.703434340667068,
      2.697464341229659, 1.606079652261706, 3.917386094917845, 2.286676496972833,
      3.5551246625733817, 2.8849283518501454, 4.148082481755749, 2.733751378191298,
      3.3515719050637514, 3.7544406028321977, 3.02798875684545, 5.14510271419116,
      2.2600589773742974, 5.145102700777102, 4.292693644933428, 4.025899132147182,
      5.295317257986989, 6.1168037457168305, 6.4199192882462945, 5.145102640060618,
      6.066259433682495, 7.829064769869258, 7.988603486715213, 5.906796018208612,
      12.652266182291966, 7.517502967651787, 7.704117998060269, 9.034285910521595,
      6.3362546789313114, 7.886920304575979, 13.864192755643435, 5.77713575641909,
      9.663999544347691, 15.034749288312755, 7.384953273948804]

fp.calc_flow_parameters(Ms)
free_stream_temps = cv.get_free_stream_temp(speed_of_sound())

print(f'free stream temps :::: {free_stream_temps}')

fp = FlowParams()  # Create an instance of FlowParams
# Call the method calc_flow_parameters on the instance
fp.calc_flow_parameters(Ms)
# Now you can access the attribute stag_temp_ratios
stag_temp_ratios = fp.stag_temp_ratios
print(f'stag temp ratios = [stag_temp_ratios]')
sv = StagValues(fp, cv)
stag_temp_values = sv.get_stag_temp_values()

stag_temp_rise = []
for free_temp, stag_temp in zip(free_stream_temps, stag_temp_values):
    rise = stag_temp - free_temp
    stag_temp_rise.append(rise)

print(f'stag temp rise ::::::::{stag_temp_rise}')

cp_values = []
for T in free_stream_temps:

    # Get Cp in J/kg-K using PropsSI
    cp = PropsSI('C', 'P', 101325, T, 'Air')

    cp_values.append(cp)

rise = []
