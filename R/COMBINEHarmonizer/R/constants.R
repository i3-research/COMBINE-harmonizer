#' Dictionary spreadsheet
#' @export
DATA_DICTIONARY_EXCEL <- "Dictionary_HIE_clinical_variables.xlsx"


#' Reserved tabs in the spreadsheet
#' Reserved tab: Variables
#' @export
SHEET_VARIABLES <- "Variables"

#' Reserved tab: main
#' @export
SHEET_MAIN <- "main"

#' Reserved tab: follow-up
#' @export
SHEET_FOLLOW_UP <- "follow-up"

#' Reserved tab: derived data
#' @export
SHEET_DERIVED_DATA <- "derived data"

#' Reserved tab: naming convention
#' @export
SHEET_NAMING_CONVENTION <- "naming convention"

#' Reserved tabs in the spreadsheet
#' @export
SHEET_RESERVED_TABS <- c(
    SHEET_VARIABLES,
    SHEET_MAIN,
    SHEET_FOLLOW_UP,
    SHEET_DERIVED_DATA,
    SHEET_NAMING_CONVENTION
)

# Columns in the dictionary
#' Category
#' @export
CATEGORY <- "Category"

#' Subcategory
#' @export
SUBCATEGORY <- "Subcategory"

#' type
#' @export
VAR_TYPE <- "type"

#' Standardized variable names dictionary
#' @export
VAR_NAME <- "Standardized_VariableNames_Dictionary"

#' Variable description
#' @export
DESCRIPTION <- "Variable_Description"

#' redcap
#' @export
REDCAP_VAR_NAME <- "redcap"

###
# Categories
###
#' Category Pre-intervention
#' @export
CATEGORY_PRE_INTERVENTION <- "Pre-intervention"

#' Category Intervention
#' @export
CATEGORY_INTERVENTION <- "Intervention"

#' Category Post-intervention
#' @export
CATEGORY_POST_INTERVENTION <- "Post-intervention"

#' Category NICU Discharge
#' @export
CATEGORY_NICU_DISCHARGE <- "NICU Discharge"

#' Category Follow Up
#' @export
CATEGORY_FOLLOW_UP <- "Follow Up"

#' Category Derived Data
#' @export
CATEGORY_DERIVED_DATA <- "Derived Data"

#' Category Period mapping
#' @export
CATEGORY_PERIOD_MAP <- list()
CATEGORY_PERIOD_MAP[[CATEGORY_PRE_INTERVENTION]] <- SHEET_MAIN
CATEGORY_PERIOD_MAP[[CATEGORY_INTERVENTION]] <- SHEET_MAIN
CATEGORY_PERIOD_MAP[[CATEGORY_POST_INTERVENTION]] <- SHEET_MAIN
CATEGORY_PERIOD_MAP[[CATEGORY_NICU_DISCHARGE]] <- SHEET_MAIN
CATEGORY_PERIOD_MAP[[CATEGORY_FOLLOW_UP]] <- SHEET_FOLLOW_UP
CATEGORY_PERIOD_MAP[[CATEGORY_DERIVED_DATA]] <- SHEET_DERIVED_DATA

#' Filename info
#' @export
FILENAME_INFOS <- list(
    list(
        name = "00-02-screening.csv",
        is_merge = FALSE,
        data_dict = SHEET_MAIN,
        exclude_columns = c("siteID")
    ),
    list(
        name = "00-12-neuro-exam.csv",
        is_merge = FALSE,
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-02-screening.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c("siteID")
    ),
    list(
        name = "01-03-maternal-demographics.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-04-pregnancy-history.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-05-labor-delivery.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-06-birth.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-07-pre-temperature.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-08-pre-cardiovascular.csv",
        data_dict = SHEET_MAIN
    ),
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
    list(
        name = "01-09-pre-infection.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-10-pre-other-med.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-11-pre-imaging.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-12-neuro-exam.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-01-temperature.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-02-cardiovascular.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-03-respiratory.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-04-blood-gas.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-05-hematology.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-05_s-hematology.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-06_s-blood-value.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-07-infection.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-08-other-med.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-09-imaging.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "03-01-post-temperature.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "03-01_s-post-temperature.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "03-02-post-blood-value.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "03-03-post-imaging.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "03-04-post-neuro-exam.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c("post_NeuroExamSectionID")
    ),
    list(
        name = "03-05-mri.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "MRIStrength_c",
            "MRIAdequateQuality_c",
            "MRIT1Axial_c",
            "MRIT1Coronal_c",
            "MRIT1Sagittal_c",
            "MRIT2Axial_c",
            "MRIT2Coronal_c",
            "MRIT2Sagittal_c",
            "MRIT2FLAIRAxial_c",
            "MRIT2FLAIRCoronal_c",
            "MRIT2FLAIRSagittal_c",
            "MRIGRESWIAxial_c",
            "MRIGRESWICoronal_c",
            "MRIGRESWISagittal_c",
            "MRISPGRAxial_c",
            "MRISPGRCoronal_c",
            "MRISPGRSagittal_c",
            "MRIDWI_c",
            "MRIADC_c",
            "MRIMRS_c",
            "MRIOther_c",
            "MRIOverallDiagnosis_c",
            "MRIAbnormal_c",
            "MRICererbalAtrophy_c",
            "MRICererbalAtrophyGlobalLocal_c",
            "MRICererbalAtrophyQualAssessCC_c",
            "MRICererbalAtrophyQualAssessVDLeft_c",
            "MRICererbalAtrophyQualAssessVDRight_c",
            "MRIInfarction_c",
            "MRIInfarctionAterialTerritoryLeft_c",
            "MRIInfarctionAterialTerritoryRight_c",
            "MRIInfarctionWatershedLeft_c",
            "MRIInfarctionWatershedRight_c",
            "MRIMidlineShift_c",
            "MRIBGT_c",
            "MRIPLIC_c",
            "MRIALIC_c",
            "MRIWatershed_c",
            "MRIWhiteMatterInjury_c",
            "MRIFocalCorticalInjury_c",
            "MRINRNPatternOfInjury_c",
            "MRINRNPatternOfInjuryExtent_c",
            "MRINRNPatternOfInjuryLateral_c",
            "subjectID_with_postfix",
            "subjectID_postfix"
        )
    ),
    list(
        name = "03-05_s-mri.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "siteID",
            "birthNumber",
            "MRIAvailable_c",
            "MRIObtainWindow_c",
            "MRISendRTIDate",
            "MRIReceiveRTIDate",
            "MRINoObtainReason_c"
        )
    ),
    list(
        name = "02-11-elevated-temperature.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-12-fluctuated-temperature.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-13-bradycardia.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-14-adverse-event.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-15-violation.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-16-interrupt.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "02-17-discontinue.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-16-wdraw-support.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-17-limit-care.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-01-status.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeStatus",
            "homeTherapyStatus",
            "homeTherapyVentilator",
            "homeTherapyOxygen",
            "homeTherapyGavageTubeFeed",
            "homeTherapyGastrostomyTubeFeed",
            "homeTherapyTemperatureBlanket",
            "homeTherapyAnticonvulsantMedication",
            "homeTherapyOther",
            "homeTherapyOtherText"
        )
    ),
    list(
        name = "04-02-neuro-exam.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeNeuroExamStatus"
        )
    ),
    list(
        name = "04-03-cardiovascular.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-04-respiratory.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-05-hematology.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-06-metabolic.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-07-renal.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-08-gastrointestinal.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-09-skin.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-10-auditory.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-11-surgery.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-12-infection.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-13-seizure.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-14-birth-defect.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-15-home-therapy.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "20-00-follow-up.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID",
            "birthDate",
            "visitDate",
            "birthNumber",
            "center_orig"
        )
    ),
    list(
        name = "20-01-ses.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "20-02-medical-history.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "20-03-medical-exam.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "20-04-bayley-iii.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "20-05-gmfcs.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "20-06-status.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "20-07-readmission.csv",
        data_dict = SHEET_FOLLOW_UP
    ),
    list(
        name = "20-08-lost.csv",
        data_dict = SHEET_FOLLOW_UP,
        exclude_columns = c(
            "siteID"
        )
    ),
    list(
        name = "30-01-secondary.csv",
        data_dict = SHEET_DERIVED_DATA
    ),
    list(
        name = "30-02-outcome.csv",
        data_dict = SHEET_DERIVED_DATA
    ),
    list(
        name = "30-03-mri.csv",
        data_dict = SHEET_DERIVED_DATA
    ),
    list(
        name = "31-02-total-modified-sarnat.csv",
        data_dict = SHEET_DERIVED_DATA
    ),
    list(
        name = "31-03-mri.csv",
        data_dict = SHEET_DERIVED_DATA
    ),
    list(
        name = "31-04-pse.csv",
        data_dict = SHEET_DERIVED_DATA,
        exclude_columns = c(
            "cordMishap",
            "uterineRupture",
            "placentalProblem",
            "shoulderDystocia",
            "maternalHemorrhage",
            "maternalTrauma",
            "maternalCardioRespiratoryArrest",
            "maternalSeizure",
            "perinatalSentinelEvent"
        )
    ),
    list(
        name = "31-05-disability-level-death.csv",
        data_dict = SHEET_DERIVED_DATA
    ),
    list(
        name = "31-06-emergency-csection.csv",
        data_dict = SHEET_DERIVED_DATA,
        exclude_columns = c(
            "deliveryMode",
            "emergencyCSection"
        )
    ),
    list(
        name = "31-07-length-of-stay.csv",
        data_dict = SHEET_DERIVED_DATA
    )
)

#' Significance level / threshold for p-value
#' @export
P_VALUE_THRESHOLD <- 10^(-5)
