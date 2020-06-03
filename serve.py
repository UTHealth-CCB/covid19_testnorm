from TestNorm.covid19_test_norm import load_rules_data, get_loinc_codes

def get_mapping_api(data_dir, covid19_lexicons_fn, covid19_testkits_fn, loinc_sarscov2_labtests_fn):
    # load rules data
    rules_data = load_rules_data(data_dir, covid19_lexicons_fn, covid19_testkits_fn, loinc_sarscov2_labtests_fn)    

    def mapping_api(input_data):
        # get input
        input = input_data
        #insert_period = False #True
        #input = pre_tokenize(input_data, insert_period)
        if not input:
            loinc_codes = []
            return loinc_codes
        # get loinc codes
        #query_ner = {'query': input.split(),'ner': []}
        #loinc_codes = get_loinc_codes(input_data, rules_data, query_ner)
        loinc_codes, _ = get_loinc_codes(input_data, rules_data)
        output = {'loinc_codes':loinc_codes}
        return output

    return mapping_api
