import pandas as pd
import os
 
# Read Excel file
excel_file = 'Book_day.xlsx'
df = pd.read_excel(excel_file)
PBHP = 180
IBHP = 260
GCRL = 2
TSTEP = 1
limit = 1500
 
# To delete the existing one
output_file = './Wind_DailyCRM.INC'
if os.path.exists(output_file):
    os.remove(output_file)
 
initial_lines = (f"-- Production well controls (all start producing at day 1)\n\n")
 
# Write content to the file
with open(output_file, 'w') as file:
    file.write(initial_lines)
    for day, rate in enumerate(df['Norne'], start=1):
        file.write(f"GCONINJE\n")
        file.write(f"\tG1\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        file.write(f"\tG2\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        file.write(f"\tG3\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        file.write(f"\tG4\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        #file.write(f"\tG5\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        #file.write(f"\tG6\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        #file.write(f"\tG7\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        #file.write(f"\tG8\tWAT\tRATE\t{rate}\t1*\t1*\t1*\tYES\t1*\t1*\t1*\t1*\t/\n")
        file.write(f"/\n\n")
        file.write(f"TSTEP\n {TSTEP} /--{day} \n\n")
        # if rate < limit:
        #     file.write(f"WCONPROD\n\t'PROD'\t'OPEN'\t'BHP'\t1*  1* 1* 1* 1*\t{PBHP}  /\n/\nWCONINJE\n\t'INJ'\tWATER\t'OPEN'\tRATE\t{rate}\t1*\t{IBHP}\t/\n \t'INJX' \t'WAT' \t'OPEN' \tRATE \t0 \t1* \t{IBHP} \t/\n \t'I' \t'WAT' \t'STOP'\tRATE \t{limit} \t1* \t{IBHP}\t/\n/\nWGRUPCON\n\t'INJ'\tYes \t 0 \tRAT \t 1 \t / \n\t'INJX'\tYes \t 0.01 \tRAT \t 1 \t / \n/\nGRUPTRAG\n\t'G1'\t RATE\t2000\t/\n/\n\n \nTSTEP\n {TSTEP} /--{day} \n\n")
        # else:
        #     file.write(f"WCONPROD\n\t'PROD'\t'OPEN'\t'BHP'\t1*  1* 1* 1* 1*\t{PBHP}  /\n/\nWCONINJE\n\t'INJ' \t'WAT' \t'OPEN' \tRATE \t{limit} \t1* \t{IBHP} \t/\n\t'INJX' \t'WAT' \t'OPEN' \tRATE \t{rate-limit} \t1* \t{IBHP} \t/\n\t'I' \t'WAT'\t'STOP'\tRATE \t{limit} \t1* \t{IBHP}\t/\n/\nWGRUPCON\n\t'INJ'\tYes \t 0 \tRAT \t 1 \t / \n\t'INJX'\tYes \t 0.01 \tRAT \t 1 \t /\n/ \n\nGRUPTRAG\n\t'G1'\t RATE\t2000\t/\n/\n\n \nTSTEP\n {TSTEP} /--{day}\n\n")
 
 