import os
import sys

from TestNorm.covid19_test_norm import load_rules_data, get_loinc_codes

if __name__ == '__main__':  
    if len(sys.argv) > 1:
        input = sys.argv[1]
    else:
        print("Usage: python test.py 'COVID19-test-name'")
        input = 'Coronavirus (COVID-19) NAA City Health Dept'
        print('using the default input: {}'.format(input))                
    rules_data = load_rules_data()    
    loinc_codes, _ = get_loinc_codes(input, rules_data)
    print('mapping {} to LOINC codes: {}'.format(input, loinc_codes))    
