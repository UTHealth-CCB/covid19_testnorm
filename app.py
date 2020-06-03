import os
from flask import Flask, render_template, request, jsonify
from serve import get_mapping_api

app = Flask(__name__)

# load the mapping api
root_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(root_dir, 'data')
#saved_model_dir = os.path.join(root_dir, 'model/saved_model')
covid19_lexicons_fn = 'Covid19_lexicons.csv'
covid19_testkits_fn = 'Covid19_ivd_testkits.csv'
loinc_sarscov2_labtests_fn = 'Loinc_Sarscov2_Export_20200603.csv'
mapping_api = get_mapping_api(data_dir, covid19_lexicons_fn, covid19_testkits_fn, loinc_sarscov2_labtests_fn)

@app.route('/covid19/loinc')
def index():
    return render_template('index.html')

@app.route('/mapping', methods=['POST'])
def mapping():
    json = request.get_json()
    covid19_testing_names = json['covid19_testing_names']    
    print('covid19 testing names: '+ covid19_testing_names)
    # output format: {'loinc_codes':loinc_codes}
    output_data = mapping_api(covid19_testing_names)
    print(output_data)
    #return jsonify(loinc_codes=output_data)
    return jsonify(output_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)