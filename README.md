# covid19_testnorm
This repository contains supplementary data and code to the tool: COVID-19 TestNorm -  A tool to normalize COVID-19 testing names to LOINC codes.

TestNorm

This folder contains COVID19 TestNorm codes for rules-based method including entity recognition and LOINC mapping.

data

This folder contains the full list of LOINC SARS CoV 2 lab tests (from https://loinc.org/sars-coronavirus-2/), and IVD testkits data (from https://loinc.org/sars-cov-2-and-covid-19/), and Covid19 lexicons file (mannually annotated from multi-sites data).

templates

This folder contains the example template file for TestNorm WebAPI using Flask.

Run

The following steps briefly describe how to install and run the TestNorm tool locally with webservice using Flask.

Install requirement packages in requirement.txt: pip install -r requirements.txt.

Run locally: python app.py.

Open browser and input: http://localhost:5000/covid19/loinc.

Input query string like "NOVEL CORONAVIRUS 2019 rRT PCR, NASOPHAR", Click Mapping button.

The mapping LOINC codes will be displayed in the page.
