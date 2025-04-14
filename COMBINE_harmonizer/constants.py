# -*- coding: utf-8 -*-

from typing import TypedDict

# Dictionary spreadsheet
DATA_DICTIONARY_EXCEL = 'Dictionary_HIE_clinical_variables.xlsx'

# Studies
STUDY_LH = 'LH'
STUDY_OC = 'OC'

# Directories in the code repository
DIR_DICTIONARY = 'Dictionary'
DIR_MERGE = 'Merge'
DIR_ANALYSIS = 'Analysis'
DIR_REDCAP = 'REDCap'

# Columns in the dictionary
DATA_DICT_CATEGORY = 'Category'
DATA_DICT_SUBCATEGORY = 'Subcategory'
DATA_DICT_VAR_TYPE = 'type'
DATA_DICT_VAR_NAME = 'Standardized_VariableNames_Dictionary'
DATA_DICT_DESCRIPTION = 'Variable_Description'
DATA_DICT_REDCAP_VAR_NAME = 'redcap'


# Default ordinal column in ordinal tabs
DEFAULT_ORDINAL_COLUMN = '_rank'


class DataDict(TypedDict):
    Category: str
    Subcategory: str
    type: str
    Standardized_VariableNames_Dictionary: str
    Variable_Description: str
    redcap: str

    LH: str
    OC: str


# Reserved tabs in the spreadsheet
SHEET_VARIABLES = 'Variables'
SHEET_MAIN = 'main'
SHEET_FOLLOW_UP = 'follow-up'
SHEET_NAMING_CONVENTION = 'naming convention'

SHEET_RESERVED_TABS = [
    SHEET_VARIABLES,
    SHEET_MAIN,
    SHEET_FOLLOW_UP,
    SHEET_NAMING_CONVENTION,
]

# Categories
CATEGORY_PRE_INTERVENTION = "Pre-intervention"
CATEGORY_INTERVENTION = "Intervention"
CATEGORY_POST_INTERVENTION = "Post-intervention"
CATEGORY_NICU_DISCHARGE = "NICU Discharge"
CATEGORY_FOLLOW_UP = "Follow Up"

CATEGORIES = [
    CATEGORY_PRE_INTERVENTION,
    CATEGORY_INTERVENTION,
    CATEGORY_POST_INTERVENTION,
    CATEGORY_NICU_DISCHARGE,
    CATEGORY_FOLLOW_UP,
]

CATEGORY_SHEET_MAP = {
    CATEGORY_PRE_INTERVENTION: SHEET_MAIN,
    CATEGORY_INTERVENTION: SHEET_MAIN,
    CATEGORY_POST_INTERVENTION: SHEET_MAIN,
    CATEGORY_NICU_DISCHARGE: SHEET_MAIN,

    CATEGORY_FOLLOW_UP: SHEET_FOLLOW_UP,

}

CATEGORY_ABBREVIATE_MAP = {
    CATEGORY_PRE_INTERVENTION: "pre",
    CATEGORY_INTERVENTION: "",
    CATEGORY_POST_INTERVENTION: "post",
    CATEGORY_NICU_DISCHARGE: "discharge",

    CATEGORY_FOLLOW_UP: "followup",
}

CATEGORY_EVENT_MAP = {val: f'{idx} {val}' for idx, val in enumerate(CATEGORIES)}

SUBCATEGORY_IDENTITY = 'Identity'
SUBCATEGORY_SCREENING = 'Screening'
SUBCATEGORY_MATERNAL_DEMOGRAPHICS = 'Maternal Demographics'
SUBCATEGORY_PATERNAL_DEMOGRAPHICS = 'Paternal Demographics'
SUBCATEGORY_PREGNANCY_HISTORY = 'Pregnancy History'
SUBCATEGORY_LABOR_AND_DELIVERY = 'Labor Delivery'
SUBCATEGORY_BIRTH_INFORMATION = 'Birth'

SUBCATEGORY_TREATMENT = 'Treatment'
SUBCATEGORY_TEMPERATURE = 'Temperature'
SUBCATEGORY_CARDIOVASCULAR = 'Cardiovascular'
SUBCATEGORY_RESPIRATORY = 'Respiratory'
SUBCATEGORY_BLOOD_GAS_RESPIRATORY = 'Blood Gas'
SUBCATEGORY_HEMATOLOGY_CBC = 'Hematology CBC'
SUBCATEGORY_HEMATOLOGY = 'Hematology'
SUBCATEGORY_BLOOD_VALUE_OTHER = 'Blood Value'
SUBCATEGORY_INFECTION = 'Infection'
SUBCATEGORY_OTHER_MEDICINE = 'Other Medication'
SUBCATEGORY_IMAGING_REPORT = 'Imaging'
SUBCATEGORY_NEURO_EXAM = 'Neuro Exam'
SUBCATEGORY_ELEVATED_TEMPERATURE = 'Elevated Temperature'
SUBCATEGORY_FLUCTUATED_TEMPERATURE = 'Fluctuated Temperature'
SUBCATEGORY_BRADYCARDIA = 'Bradycardia'
SUBCATEGORY_ADVERSE_EVENT = 'Adverse Event'
SUBCATEGORY_PROTOCOL_VIOLATION = 'Violation'
SUBCATEGORY_INTERRUPTION_OF_INTERVENTION = 'Interrupt'
SUBCATEGORY_DISCONTINUATION_OF_INTERVENTION = 'Discontinue'

SUBCATEGORY_MRI = 'MRI'
SUBCATEGORY_MRS = 'MRS'
SUBCATEGORY_EEG = 'EEG'

SUBCATEGORY_STATUS = 'Status'
SUBCATEGORY_METABOLIC = 'Metabolic'
SUBCATEGORY_RENAL = 'Renal'
SUBCATEGORY_GASTROINTESTINAL = 'Gastrointestinal'
SUBCATEGORY_SKIN = 'Skin'
SUBCATEGORY_AUDITORY = 'Auditory'
SUBCATEGORY_SURGERY = 'Surgery'
SUBCATEGORY_SEIZURE = 'Seizure'
SUBCATEGORY_BIRTH_DEFECT = 'Birth Defect'
SUBCATEGORY_HOME_THERAPY = 'Home Therapy'
SUBCATEGORY_WITHDRAWAL_OF_SUPPORT = 'Withdrawal of Support'
SUBCATEGORY_LIMITATION_OF_CARE = 'Limitation of Care'

SUBCATEGORY_FOLLOWUP = 'Follow Up'
SUBCATEGORY_SOCIOECONOMIC_STATUS = 'SES'
SUBCATEGORY_MEDICAL_HISTORY = 'Medical History'
SUBCATEGORY_MEDICAL_EXAM = 'Medical Exam'
SUBCATEGORY_BAYLEY_III = 'Bayley-III'
SUBCATEGORY_GMFCS = 'GMFCS'
SUBCATEGORY_READMISSION = 'Readmission'
SUBCATEGORY_LOST_FOLLOW_UP = 'Lost Followup'
SUBCATEGORY_PHONE_FOLLOW_UP = 'Phone Followup'

SUBCATEGORY_SECONDARY_ANALYSIS = 'Secondary'
SUBCATEGORY_OUTCOME = 'Outcome'

SUBCATEGORY_ABBREVIATE_MAP = {  # max: 7 chars.
    SUBCATEGORY_IDENTITY: 'id',
    SUBCATEGORY_SCREENING: 'screening',
    SUBCATEGORY_MATERNAL_DEMOGRAPHICS: 'maternal_demographics',
    SUBCATEGORY_PATERNAL_DEMOGRAPHICS: 'paternal_demographics',
    SUBCATEGORY_PREGNANCY_HISTORY: 'pregnancy_history',
    SUBCATEGORY_LABOR_AND_DELIVERY: 'labor_and_delivery',
    SUBCATEGORY_BIRTH_INFORMATION: 'birth_information',

    SUBCATEGORY_TREATMENT: 'treatment',
    SUBCATEGORY_TEMPERATURE: 'temperature',
    SUBCATEGORY_CARDIOVASCULAR: 'cardiovascular',
    SUBCATEGORY_RESPIRATORY: 'respiratory',
    SUBCATEGORY_BLOOD_GAS_RESPIRATORY: 'blood_gas_respiratory',
    SUBCATEGORY_HEMATOLOGY_CBC: 'hematology_cbc',
    SUBCATEGORY_BLOOD_VALUE_OTHER: 'blood_value_other',
    SUBCATEGORY_INFECTION: 'infection',
    SUBCATEGORY_OTHER_MEDICINE: 'other_medicine',
    SUBCATEGORY_IMAGING_REPORT: 'imaging_report',
    SUBCATEGORY_NEURO_EXAM: 'neuro_exam',
    SUBCATEGORY_ELEVATED_TEMPERATURE: 'elevated_temperature',
    SUBCATEGORY_FLUCTUATED_TEMPERATURE: 'fluctuated_temperature',
    SUBCATEGORY_BRADYCARDIA: 'bradycardia',
    SUBCATEGORY_ADVERSE_EVENT: 'adverse_event',
    SUBCATEGORY_PROTOCOL_VIOLATION: 'protocol_violation',
    SUBCATEGORY_INTERRUPTION_OF_INTERVENTION: 'interruption_of_intervention',
    SUBCATEGORY_DISCONTINUATION_OF_INTERVENTION: 'discontinuation_of_intervention',

    SUBCATEGORY_MRI: 'mri',
    SUBCATEGORY_MRS: 'mrs',
    SUBCATEGORY_EEG: 'eeg',

    SUBCATEGORY_STATUS: 'status',
    SUBCATEGORY_METABOLIC: 'metabolic',
    SUBCATEGORY_HEMATOLOGY: 'hematology',
    SUBCATEGORY_RENAL: 'renal',
    SUBCATEGORY_GASTROINTESTINAL: 'gastrointestinal',
    SUBCATEGORY_SKIN: 'skin',
    SUBCATEGORY_AUDITORY: 'auditory',
    SUBCATEGORY_SURGERY: 'surgery',
    SUBCATEGORY_SEIZURE: 'seizure',
    SUBCATEGORY_BIRTH_DEFECT: 'birth_defect',
    SUBCATEGORY_HOME_THERAPY: 'home_therapy',
    SUBCATEGORY_WITHDRAWAL_OF_SUPPORT: 'withdrawal_of_support',
    SUBCATEGORY_LIMITATION_OF_CARE: 'limitation_of_care',

    SUBCATEGORY_FOLLOWUP: 'followup',
    SUBCATEGORY_SOCIOECONOMIC_STATUS: 'socioeconomic_status',
    SUBCATEGORY_MEDICAL_HISTORY: 'medical_history',
    SUBCATEGORY_MEDICAL_EXAM: 'medical_exam',
    SUBCATEGORY_BAYLEY_III: 'bayley_3',
    SUBCATEGORY_GMFCS: 'gmfcs',
    SUBCATEGORY_READMISSION: 'readmission',
    SUBCATEGORY_LOST_FOLLOW_UP: 'lost_follow_up',
    SUBCATEGORY_PHONE_FOLLOW_UP: 'phone_follow_up',

    SUBCATEGORY_SECONDARY_ANALYSIS: 'secondary_analysis',
    SUBCATEGORY_OUTCOME: 'outcome',
}

# Types
BASIC_TYPE_BOOL = 'bool'
BASIC_TYPE_INT = 'int'
BASIC_TYPE_FLOAT = 'float'
BASIC_TYPE_CENTER = 'center'
BASIC_TYPE_DATE = 'date'
BASIC_TYPE_TIME = 'time'
BASIC_TYPE_TEXT = 'text'

# Flatten index
FLATTEN_INDEX = '_flatten_index'

# Max integer
MAX_INT = 999999999999999999

# Reserved columns for identificatio
RESERVED_COLUMNS: list[str] = [
    '_study',
    'center',
    'subjectID',
    'uniqueID',
    'MRI_ID',
    'followupCenter',
    'followupID',
    'uniqueFollowupID',
    '_flatten_index'
]

# The csv file merged and flattened from all other files
MERGE_FLATTEN_CSV = 'zz-merged-flatten.csv'

# The xlsx file merged from all other files
MERGE_XLSX = 'zz-merged.xlsx'

# Merging columns for flattening all the files into zz-merged-flatten.csv
FLATTEN_MERGE_COLUMNS = ['_study', 'center', 'subjectID', 'uniqueID']

# Follow up merging columns for flattening into zz-merged-flatten.csv
FLATTEN_FOLLOW_UP_COLUMNS = ['followupID', 'uniqueFollowupID']


# Filename info
class FilenameInfo(TypedDict, total=False):
    name: str
    is_merge: bool
    data_dict: str
    exclude_columns: list[str]
    category: str
    subcategory: str
    summary: bool


FILENAME_INFOS: list[FilenameInfo] = [
    {
        'name': '00-02-screening.csv',
        'is_merge': False,
        'data_dict': SHEET_MAIN,
        'exclude_columns': ['siteID'],
        'subcategory': SUBCATEGORY_SCREENING,
    },
    {
        'name': '00-12-neuro-exam.csv',
        'is_merge': False,
        'data_dict': SHEET_MAIN,
        'exclude_columns': [],
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '01-02-screening.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': ['siteID', 'birthDate'],
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_SCREENING,
    },
    {
        'name': '01-03-maternal-demographics.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_MATERNAL_DEMOGRAPHICS,
        'exclude_columns': [
            'motherRaceOther1',
            'motherRaceOther2',
            'motherRaceOther3',
            'motherRaceOther4',
            'motherRaceOther5',
            'motherRaceOther6',
            'motherRace2',
            'motherEducation2',
            'motherInsurancePublic',
        ],
    },
    {
        'name': '01-04-pregnancy-history.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_PREGNANCY_HISTORY,
    },
    {
        'name': '01-05-labor-delivery.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_LABOR_AND_DELIVERY,
        'exclude_columns': [
            'laborAntibioticsCode2',
            'laborAntibioticsCode3',
            'laborAntibioticsCode4',
            'laborAntibioticsCode5',
            'laborAntibioticsCode6',
        ],
    },
    {
        'name': '01-05_1-pse.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'cordMishap',
            'uterineRupture',
            'placentalProblem',
            'shoulderDystocia',
            'maternalHemorrhage',
            'maternalTrauma',
            'maternalCardioRespiratoryArrest',
            'maternalSeizure',
            'perinatalSentinelEvent',
        ],
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_LABOR_AND_DELIVERY,
    },
    {
        'name': '01-05_2-emergency-csection.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'deliveryMode',
            'emergencyCSection',
        ],
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_LABOR_AND_DELIVERY,
    },
    {
        'name': '01-06-birth.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_BIRTH_INFORMATION,
    },
    {
        'name': '01-06_1-apgar.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_BIRTH_INFORMATION,
        'exclude_columns': [
            'Apgar5min',
            'Apgar10min',
            'Apgar10minLess5',
            'Apgar10minLessEq5',
            'Apgar5minLessEq5',
        ],
    },
    {
        'name': '01-07-pre-temperature.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_TEMPERATURE,
    },
    {
        'name': '01-08-pre-cardiovascular.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_CARDIOVASCULAR,
    },
    # XXX Skip respiratory / Blood gas / Hematology in the Pre-intervention
    # for now because there is only 1 record in blood gas.
    # {
    #     'name': '01-13-pre-respiratory.csv',
    #     'data_dict': SHEET_MAIN,
    # },
    # {
    #     'name': '01-14-pre-blood-gas.csv',
    #     'data_dict': SHEET_MAIN,
    # },
    # {
    #     'name': '01-15-pre-hematology.csv',
    #     'data_dict': SHEET_MAIN,
    # },
    {
        'name': '01-09-pre-infection.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_INFECTION,
        'exclude_columns': [
            'pre_PositiveCultureOrganismCode2',
            'pre_PositiveCultureOrganismCode3',
            'pre_AntibioticsCode2',
            'pre_AntibioticsCode3',
        ],
    },
    {
        'name': '01-10-pre-other-med.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_OTHER_MEDICINE,
        'exclude_columns': [
            'pre_Anticonvulsants',
            'pre_Anticonvulsants2',
            'pre_Anticonvulsants3',
            'pre_AnalgesicsSedatives',
            'pre_AnalgesicsSedatives2',
            'pre_AnalgesicsSedatives3',
            'pre_Antipyretics',
            'pre_Antipyretics2',
            'pre_Antipyretics3',
            'pre_Paralytics',
            'pre_Paralytics2',
            'pre_Paralytics3',
        ],
    },
    {
        'name': '01-11-pre-imaging.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_IMAGING_REPORT,
        'exclude_columns': [
            'pre_HeadSonogramResult2',
            'pre_HeadSonogramResult3',
            'pre_HeadSonogramResult4',
            'pre_HeadSonogramResult5',
            'pre_HeadSonogramResult6',
            'pre_HeadSonogramResult7',
            'pre_HeadSonogramResult8',
            'pre_HeadCTResult2',
            'pre_HeadCTResult3',
            'pre_HeadCTResult4',
            'pre_HeadCTResult5',
            'pre_HeadCTResult6',
            'pre_HeadCTResult7',
            'pre_HeadCTResult8',
            'pre_BrainMRIResult2',
            'pre_BrainMRIResult3',
            'pre_BrainMRIResult4',
            'pre_BrainMRIResult5',
            'pre_BrainMRIResult6',
            'pre_BrainMRIResult7',
            'pre_BrainMRIResult8',
        ],
    },
    {
        'name': '01-12-neuro-exam.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
        ],
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '01-12_1-total-modified-sarnat.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'pre_NeuroExamLevelConsciousnessScore',
            'pre_NeuroExamSpontaneousActivityScore',
            'pre_NeuroExamPostureScore',
            'pre_NeuroExamToneScore',
            'pre_NeuroExamSuckScore',
            'pre_NeuroExamMoroScore',
            'pre_NeuroExamPupilsScore',
            'pre_NeuroExamHeartRateScore',
            'pre_NeuroExamRespirationScore',
        ],
        'category': CATEGORY_PRE_INTERVENTION,
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '02-01-temperature.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_TEMPERATURE,
    },
    {
        'name': '02-02-cardiovascular.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_CARDIOVASCULAR,
    },
    {
        'name': '02-03-respiratory.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_RESPIRATORY,
    },
    {
        'name': '02-04-blood-gas.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_BLOOD_GAS_RESPIRATORY,
    },
    {
        'name': '02-05-hematology.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_HEMATOLOGY_CBC,
    },
    {
        'name': '02-05_s-hematology.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_HEMATOLOGY_CBC,
        'summary': True,
    },
    {
        'name': '02-06_s-blood-value.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_BLOOD_VALUE_OTHER,
        'summary': True,
    },
    {
        'name': '02-07-infection.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_INFECTION,
        'exclude_columns': [
            'positiveCultureOrganismCode2',
            'positiveCultureOrganismCode3',
            'antibioticsCode2',
            'antibioticsCode3',
            'rewarmingAntibioticsCode2',
            'rewarmingAntibioticsCode3',
        ],
    },
    {
        'name': '02-08-other-med.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_OTHER_MEDICINE,
        'exclude_columns': [
            'anticonvulsants',
            'anticonvulsants2',
            'anticonvulsants3',
            'analgesicsSedatives',
            'analgesicsSedatives2',
            'analgesicsSedatives3',
            'antipyretics',
            'antipyretics2',
            'antipyretics3',
            'paralytics',
            'paralytics2',
            'paralytics3',
        ],
    },
    {
        'name': '02-09-imaging.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_IMAGING_REPORT,
        'exclude_columns': [
            'headSonogramResult2',
            'headSonogramResult3',
            'headSonogramResult4',
            'headSonogramResult5',
            'headSonogramResult6',
            'headSonogramResult7',
            'headSonogramResult8',
            'headCTResult2',
            'headCTResult3',
            'headCTResult4',
            'headCTResult5',
            'headCTResult6',
            'headCTResult7',
            'headCTResult8',
            'brainMRIResult2',
            'brainMRIResult3',
            'brainMRIResult4',
            'brainMRIResult5',
            'brainMRIResult6',
            'brainMRIResult7',
            'brainMRIResult8',
        ],
    },
    {
        'name': '02-11-elevated-temperature.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_ELEVATED_TEMPERATURE,
    },
    {
        'name': '02-12-fluctuated-temperature.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_FLUCTUATED_TEMPERATURE,
    },
    {
        'name': '02-13-bradycardia.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_BRADYCARDIA,
    },
    {
        'name': '02-14-adverse-event.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_ADVERSE_EVENT,
    },
    {
        'name': '02-15-violation.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_PROTOCOL_VIOLATION,
    },
    {
        'name': '02-16-interrupt.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_INTERRUPTION_OF_INTERVENTION,
    },
    {
        'name': '02-17-discontinue.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_INTERVENTION,
        'subcategory': SUBCATEGORY_DISCONTINUATION_OF_INTERVENTION,
    },
    {
        'name': '03-01-post-temperature.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_TEMPERATURE,
    },
    {
        'name': '03-01_s-post-temperature.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_TEMPERATURE,
        'summary': True,
    },
    {
        'name': '03-02-post-blood-value.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_BLOOD_VALUE_OTHER,
    },
    {
        'name': '03-03-post-imaging.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_IMAGING_REPORT,
        'exclude_columns': [
            'post_HeadSonogramResult2',
            'post_HeadSonogramResult3',
            'post_HeadSonogramResult4',
            'post_HeadSonogramResult5',
            'post_HeadSonogramResult6',
            'post_HeadSonogramResult7',
            'post_HeadSonogramResult8',
            'post_HeadCTResult2',
            'post_HeadCTResult3',
            'post_HeadCTResult4',
            'post_HeadCTResult5',
            'post_HeadCTResult6',
            'post_HeadCTResult7',
            'post_HeadCTResult8',
            'post_BrainMRIResult2',
            'post_BrainMRIResult3',
            'post_BrainMRIResult4',
            'post_BrainMRIResult5',
            'post_BrainMRIResult6',
            'post_BrainMRIResult7',
            'post_BrainMRIResult8',
        ],
    },
    {
        'name': '03-04-post-neuro-exam.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'post_NeuroExamSectionID',
        ],
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '03-04_1-total-modified-sarnat.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'post_NeuroExamLevelConsciousnessScore',
            'post_NeuroExamSpontaneousActivityScore',
            'post_NeuroExamPostureScore',
            'post_NeuroExamToneScore',
            'post_NeuroExamSuckScore',
            'post_NeuroExamMoroScore',
            'post_NeuroExamPupilsScore',
            'post_NeuroExamHeartRateScore',
            'post_NeuroExamRespirationScore',
        ],
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '03-05-mri.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'MRIDate',
            'MRIReader',
            'MRIReadDate',
            'MRIStrength_c',
            'MRIAdequateQuality_c',
            'MRIT1Axial_c',
            'MRIT1Coronal_c',
            'MRIT1Sagittal_c',
            'MRIT2Axial_c',
            'MRIT2Coronal_c',
            'MRIT2Sagittal_c',
            'MRIT2FLAIRAxial_c',
            'MRIT2FLAIRCoronal_c',
            'MRIT2FLAIRSagittal_c',
            'MRIGRESWIAxial_c',
            'MRIGRESWICoronal_c',
            'MRIGRESWISagittal_c',
            'MRISPGRAxial_c',
            'MRISPGRCoronal_c',
            'MRISPGRSagittal_c',
            'MRIDWI_c',
            'MRIADC_c',
            'MRIMRS_c',
            'MRIOther_c',
            'MRIOverallDiagnosis_c',
            'MRIAbnormal_c',
            'MRIAbnormalRegion1_c',
            'MRIAbnormalRegion2',
            'MRIAbnormalRegion2_c',
            'MRIAbnormalRegion3',
            'MRIAbnormalRegion3_c',
            'MRIAbnormalSide_c',
            'MRIAbnormalGrayMatterWhiteMatter_c',
            'MRIAbnormalExtent1_c',
            'MRIAbnormalExtent2',
            'MRIAbnormalExtent2_c',
            'MRIAbnormalType_c',
            'MRIAbnormalType2',
            'MRIAbnormalType2_c',

            'MRICerebralAtrophy_c',
            'MRICerebralAtrophyGlobalLocal_c',
            'MRICerebralAtrophyQualAssessCC_c',
            'MRICerebralAtrophyQualAssessVDLeft_c',
            'MRICerebralAtrophyQualAssessVDRight_c',
            'MRIInfarction_c',
            'MRIInfarctionArterialTerritoryLeft_c',
            'MRIInfarctionArterialTerritoryRight_c',
            'MRIInfarctionWatershedLeft_c',
            'MRIInfarctionWatershedRight_c',
            'MRIMidlineShift_c',
            'MRIBGT_c',
            'MRIPLIC_c',
            'MRIALIC_c',
            'MRIWatershed_c',
            'MRIWhiteMatterInjury_c',
            'MRIFocalCorticalInjury_c',
            'MRINRNPatternOfInjury_c',
            'MRINRNPatternOfInjuryExtent_c',
            'MRINRNPatternOfInjuryLateral_c',
            'subjectID_with_postfix',
            'subjectID_postfix',
        ],
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_MRI,
    },
    {
        'name': '03-05_s-mri.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'siteID',
            'birthNumber',
            'MRIAvailable_c',
            'MRIObtainWindow_c',
            'MRISendRTIDate',
            'MRIReceiveRTIDate',
            'MRINoObtainReason_c',
        ],
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_MRI,
        'summary': True,
    },
    {
        'name': '03-05_s1-mri.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'MRINRNPatternOfInjuryMerge',
        ],
        'category': CATEGORY_POST_INTERVENTION,
        'subcategory': SUBCATEGORY_MRI,
        'summary': True,
    },
    {
        'name': '04-01-status.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'dischargeStatus',
            'homeTherapyStatus',
            'homeTherapyVentilator',
            'homeTherapyOxygen',
            'homeTherapyGavageTubeFeed',
            'homeTherapyGastrostomyTubeFeed',
            'homeTherapyTemperatureBlanket',
            'homeTherapyAnticonvulsantMedication',
            'homeTherapyOther',
            'homeTherapyOtherText',
        ],
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_STATUS,
    },
    {
        'name': '04-01_1-length-of-stay.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_STATUS,
    },
    {
        'name': '04-02-cardiovascular.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_CARDIOVASCULAR,
    },
    {
        'name': '04-03-respiratory.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_RESPIRATORY,
        'exclude_columns': [
            'dischargePulmonaryStartDate2',
            'dischargePulmonaryStartTime2',
            'dischargePulmonaryEndDate2',
            'dischargePulmonaryEndTime2',
            'dischargePulmonaryStartDate3',
            'dischargePulmonaryStartTime3',
            'dischargePulmonaryEndDate3',
            'dischargePulmonaryEndTime3',
        ],
    },
    {
        'name': '04-04-hematology.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_HEMATOLOGY,
    },
    {
        'name': '04-05-metabolic.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_METABOLIC,
    },
    {
        'name': '04-06-renal.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_RENAL,
    },
    {
        'name': '04-07-gastrointestinal.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_GASTROINTESTINAL,
    },
    {
        'name': '04-08-skin.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_SKIN,
    },
    {
        'name': '04-09-auditory.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_AUDITORY,
    },
    {
        'name': '04-10-surgery.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_SURGERY,
        'exclude_columns': [
            'dischargeSurgeryCode2',
            'dischargeSurgeryCode3',
        ],
    },
    {
        'name': '04-11-infection.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_INFECTION,
        'exclude_columns': [
            'dischargeSepticemiaOrganismCode2',
            'dischargeSepticemiaOrganismCode3',

            'dischargeMeningitisOrganismCode2',
            'dischargeMeningitisOrganismCode3',
        ],
    },
    {
        'name': '04-12-neuro-exam.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'dischargeNeuroExamStatus',
        ],
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '04-12_1-total-modified-sarnat.csv',
        'data_dict': SHEET_MAIN,
        'exclude_columns': [
            'dischargeNeuroExamLevelConsciousnessScore',
            'dischargeNeuroExamSpontaneousActivityScore',
            'dischargeNeuroExamPostureScore',
            'dischargeNeuroExamToneScore',
            'dischargeNeuroExamSuckScore',
            'dischargeNeuroExamMoroScore',
            'dischargeNeuroExamPupilsScore',
            'dischargeNeuroExamHeartRateScore',
            'dischargeNeuroExamRespirationScore',
        ],
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_NEURO_EXAM,
    },
    {
        'name': '04-13-seizure.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_SEIZURE,
    },
    {
        'name': '04-14-birth-defect.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_BIRTH_DEFECT,
        'exclude_columns': [
            'dischargeBirthDefectCode2',
            'dischargeBirthDefectCode3',
        ],
    },
    {
        'name': '04-15-home-therapy.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_HOME_THERAPY,
    },
    {
        'name': '04-16-wdraw-support.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_WITHDRAWAL_OF_SUPPORT,
    },
    {
        'name': '04-17-limit-care.csv',
        'data_dict': SHEET_MAIN,
        'category': CATEGORY_NICU_DISCHARGE,
        'subcategory': SUBCATEGORY_LIMITATION_OF_CARE,
    },
    {
        'name': '20-00-follow-up.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
            'birthDate',
            'visitDate',
            'birthNumber',
            'center_orig',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_IDENTITY,
    },
    {
        'name': '20-01-ses.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_SOCIOECONOMIC_STATUS,
    },
    {
        'name': '20-02-medical-history.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_MEDICAL_HISTORY,
    },
    {
        'name': '20-03-medical-exam.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_MEDICAL_EXAM,
    },
    {
        'name': '20-04-bayley-iii.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_BAYLEY_III,
    },
    {
        'name': '20-05-gmfcs.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_GMFCS,
    },
    {
        'name': '20-06-status.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_STATUS,
    },
    {
        'name': '20-07-readmission.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_READMISSION,
    },
    {
        'name': '20-08-lost.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'exclude_columns': [
            'siteID',
        ],
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_LOST_FOLLOW_UP,
    },
    {
        'name': '20-09-secondary.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_SECONDARY_ANALYSIS,
    },
    {
        'name': '20-10-outcome.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_OUTCOME,
    },
    {
        'name': '20-10_1-disability-level-death.csv',
        'data_dict': SHEET_FOLLOW_UP,
        'category': CATEGORY_FOLLOW_UP,
        'subcategory': SUBCATEGORY_OUTCOME,
    },
]

# Significance level / threshold for p-value
P_VALUE_THRESHOLD = 10**(-5)

REMOVE_COLUMNS = set([
    "subjectID_with_postfix",
    "subjectID_postfix",
])

# REDCap
REDCAP_EXCLUDE_FILEINFO_COLUMNS = ['_study', 'center', 'subjectID', 'uniqueID', '_flatten_index']
REDCAP_ID_COLUMNS = ['study_unique_id', 'study', 'center', 'subject_id', 'unique_id']
REDCAP_ID_FORM = 'identifier'
