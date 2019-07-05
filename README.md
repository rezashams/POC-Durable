

A poc to run  durable for two rules.

Data are gotten from test.json.

Two rules:

Patient must be female.

Patient must be male AND older than 70 years.

PatientStatus.value must be one of a pre-defined list of vaules supplied by the CRO. (e.g. ScreenSuccess, ScreenFail, Randomized, Withdrawn, Completed). PatientStatus can be set on any visit and if a PatientStatus DM rule is not defined for a visit, the PatientStatus for that visit will be a default value. e.g. Continuing.

install:

1- pip install durable_rules

2- python rule1&2.py

3- python rule3.py
