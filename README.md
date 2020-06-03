# covid19_testnorm
COVID-19 TestNorm -  A tool to normalize COVID-19 testing names to LOINC codes
The following steps briefly describes how to run the TestNorm tool locally with webservice using Flask.

Install requirement packages in requirement.txt: pip install -r requirements.txt.

Run locally: python app.py.

Open browser and input: http://localhost:5000/covid19/loinc.

Input query string like "NOVEL CORONAVIRUS 2019 rRT PCR, NASOPHAR", Click Mapping button.

The mapping LOINC codes will be displayed in the page.
