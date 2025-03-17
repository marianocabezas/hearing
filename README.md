# Hearing Analysis

## Research Questions

### Screening/Self-diagnosis Queries
1. Of those with adult-onset hearing loss, at what age did they have a screening test performed?
2. At what age did they visit their GP about their hearing?
3. Is there a relationship between the severity of hearing loss and the date of their first screening or first GP visit related to hearing?

### Intervention Queries
1. What were the first interventions provided by the GP in response to a hearing-loss diagnosis?
2. Do care plans or intervention procedures exist for patients with hearing loss?
3. Are the interventions standardised across GP clinics?

### Post-Intervention Outcomes
1. After a referral to an audiologist/ENT, did the patient have any further hearing-related visits to the GP?
2. What aspects of the patient data changed after accessing hearing intervention(s)?
3. What post-intervention data quantifies a good outcome?

## Data Sources
- audiogram_HL_demographics.csv
- frank_audiogram.csv

## audiogram_device_analysis.ipynb

### Scripts
1. Demographics of people with hearing loss (HEIDI warehouse)
- Plot type: sn.histplot
- Data: audiogram_HL_demographics.csv
- x: HL_AGE
- hue: GENDER_TEXT

2. Device type by age (HEIDI warehouse)
- Plot type: sn.histplot
- Data: audiogram_HL_demographics.csv
- x: HL_AGE
- hue: DEVICE_TYPE

3. Device type by ear (HEIDI warehouse)
- Plot type: sn.histplot
- Data: audiogram_HL_demographics.csv
- x: HL_AGE
- hue: DEVICE_TYPE

4. Initial 3FAHL Right vs Age
- Plot type: sn.scatterplot
- Data: frank_audiogram.csv
- x: HL_AGE
- y: INITIAL_3FAHL_RIGHT
- hue: GENDER_TEXT
- Additional features: sn.regplot for each group

5. Initial 3FAHL Left vs Age
- Plot type: sn.scatterplot
- Data: frank_audiogram.csv
- x: HL_AGE
- y: INITIAL_3FAHL_LEFT
- hue: GENDER_TEXT
- Additional features: sn.regplot for each group

6. HL Age and Audigram Scores grouped by device type
- Plot type: sn.kdeplot
- Data: audiogram_HL_demographics.csv
- x: FAHL3 score (left and right)
- y: HL_AGE
- hue: DEVICE_TYPE

7. Descriptive Statistics Grouped By Gender
- Function used: pd.dataframe.describe()
- data: audiogram_HL_demographics.csv
- index: PATIENT_ID

8. Specsavers AU and NZ Age Range
- Function used: pandas queries
- Data: 'AU_screeners_data.csv', 'NZ_screeners_data.csv'

9. General demographics of SpecSavers participants (Australia)
- Plot type: sn.histplot
- Data: AU_screeners_data.csv
- x: age

10. General demographics of SpecSavers participants (Australia) with 3FAHL > 20dB
- Plot type: histplot
- Data: AU_screeners_data.csv
- x: age

11. Demographics of Specsaver entries with hearing loss
- Function used: pd.assign, pd.to_numeric, pd.str.contains
- Data: au_ages

12. Age range of Specsavers entries with hearing loss
- Functions used: pd.assign, pd.groupby, pd.describe
- Data: filt_spec_demo

13. Specsavers Jitter 3FAHL Right by Age
- Plot type: histplot
- Data: filt_spec_demo
- x: age + rand()





