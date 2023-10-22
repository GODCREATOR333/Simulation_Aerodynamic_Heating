
import tabula 

def extract_data_from_pdf(pdf_path, mach_values_list):
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    tolerance = 1
    TT0_results = []
    PP0_results = []

    for mach_value in mach_values_list:
        mach_value = round(mach_value, 1)  # Truncate to 1 decimal place

        for table_index, table in enumerate(tables, start=1):
            if 'M' in table.columns:
                mach_values = table['M'].tolist()

                for index, value in enumerate(mach_values):
                    if abs(value - mach_value) < tolerance:
                        TT0_results.append(table['T/T0'].iloc[index])
                        PP0_results.append(table['P/P0'].iloc[index])
                        break

    return TT0_results, PP0_results

    
pdf_path = './isentropic_flow_tables.pdf'
input_mach_values =[0.08878709624796989, 0.09828388233718056, 0.8655007122248444, 0.4904194172916039,
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

TT0_results, PP0_results = extract_data_from_pdf(pdf_path, input_mach_values)

print("Length of T/T0 results:", len(TT0_results))
print("Length of P/P0 results:", len(PP0_results))

def big_numbers():
    values_more_than_table = []
    for i in input_mach_values:
        if i > 4.8 :
            values_more_than_table.append(i)
    return values_more_than_table
    
big_values =big_numbers()
print(f'Big numbers {big_values}')
print(f'length of big number : {len(big_values)}')


