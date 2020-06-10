# covid19_testnorm

Coronavirus disease 2019 (COVID-19) was declared as a pandemic by the World Health Organization (WHO) on March 11th 2020 and it has raised a serious global health crisis since then. As stated by Science - “it is more important than ever for scientists around the world to openly share their knowledge, expertise, tools, and technology” [1].

To efficiently conduct clinical studies across different institutions within a network, one requirement is to normalize clinical data to common data models (CDM) and standard terminologies. Among different types of clinical data, COVID-19 diagnostic testings are extremely important for all the following analyses, as they are the primary means to identify the confirmed COVID-19 cases. To address the urgency of the pandemic, individual institutions have created local names and local codes for those new COVID-19 testings in their EHRs. Meanwhile, LOINC (The standard code system for laboratory observations), a widely used international standard for lab tests, has responded quickly by developing a new set of standard codes for COVID-19 testings, to guide standard coding of COVID-19 testings in clinical settings. 

This repository contains supplementary data and code to the tool: COVID-19 TestNorm -  A tool to normalize COVID-19 testing names to LOINC codes.

Figure 1 shows an overview of the modules of the COVID-19 TestNorm system, mainly including entity recognition and LOINC mapping, with inputs from knowledge components such as lexicons and coding rules. 

![Alt text](/docs/overview.png?raw=true "Overview of COVID19 TestNorm")

Figure 2 shows the flow chart of coding rules for COVID-19 LOINC mapping. 

![Alt text](/docs/coding_rules.png?raw=true "Flow chart of Coding rules for COVID19 mapping")


TestNorm

This folder contains COVID19 TestNorm codes for rules-based method including entity recognition and LOINC mapping.

data

This folder contains the full list of LOINC SARS CoV 2 lab tests (from https://loinc.org/sars-coronavirus-2/), and IVD testkits data (from https://www.cdc.gov/csels/dls/sars-cov-2-livd-codes.html and https://loinc.org/sars-cov-2-and-covid-19/), and Covid19 lexicons file (mannually annotated from multi-sites data).


Run

The following steps briefly describe how to run the TestNorm tool.

Install requirement packages in requirement.txt: pip install -r requirements.txt.

Run the test.py: python test.py 'NOVEL CORONAVIRUS 2019 rRT PCR, NASOPHAR'.

The mapping LOINC codes together with long common name will be displayed as: '94759-8' and 'SARS coronavirus 2 (COVID19) RNA [Presence] in Nasopharynx by NAA with probe detection'

References

[1] Barton CM, Alberti M, Ames D, Atkinson J-A, Bales J, Burke E, et al. Call for transparency of COVID-19 models. Science. 2020 01;368(6490):482–3.
