import os
import sys
import pandas as pd

from TestNorm.covid19_test_norm import load_rules_data, get_loinc_codes

if __name__ == '__main__':  
    if len(sys.argv) > 1:
        input = sys.argv[1]
        if input.endswith('.csv'):
            if len(sys.argv) > 2:
                output = sys.argv[2]
            else:
                output = ''
    else:
        print("Usage: python test.py COVID19-labtest-names or python input-test-csv-file output-test-csv-file")
        print('Please note that test-input-csv is a csv file which contains one column "Covid19LabtestNames" with multiple rows of COVID19 labtest names, e.g., an example test.csv in the current folder')
        input = 'NOVEL CORONAVIRUS 2019 rRT PCR, NASOPHAR'
        print('using the default test input')             
    rules_data = load_rules_data()    
    if not input.endswith('.csv'):        
        # test for one COVID19 labtest testnames
        loinc_codes = get_loinc_codes(input, rules_data)
        print('Input: {}, Results: {}'.format(input, loinc_codes['loinc']))
    else:
        # batch test for input's csv file
        if os.path.exists(input):
            loinc_codes = []
            df_test = pd.read_csv(input)  
            loinc_test_names = df_test.iloc[:, 0] #The first column: Covid19LabtestNames
            loinc_auto_codes = []
            loic_long_names = []
            for input in loinc_test_names:
                loinc_output = get_loinc_codes(input, rules_data)
                print('Input: {}, Result: {}-{}'.format(input, loinc_output['loinc']['Codes'], loinc_output['loinc']['Long Common Names']))
                loinc_auto_codes.append('|'.join(loinc_output['loinc']['Codes']))            
                loic_long_names.append('|'.join(loinc_output['loinc']['Long Common Names']))            
            if output:
                df_output = pd.DataFrame(zip(loinc_test_names, loinc_auto_codes, loic_long_names), columns = ['Covid19LabtestNames', 'AutoLoincCodes', 'LongCommonNames'])
                print('Save output to {}'.format(output))
                df_output.to_csv(output, index=False)
        else:
            print('{} not exits, please input csv file with correct path and make sure the file exists.'.format(input))