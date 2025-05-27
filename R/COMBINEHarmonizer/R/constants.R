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

#' Reserved tab: naming convention
#' @export
SHEET_NAMING_CONVENTION <- "naming convention"

#' Reserved tabs in the spreadsheet
#' @export
SHEET_RESERVED_TABS <- c(
    SHEET_VARIABLES,
    SHEET_MAIN,
    SHEET_FOLLOW_UP,
    SHEET_NAMING_CONVENTION
)

# Columns in the dictionary
#' Category
#' @export
DATA_DICT_CATEGORY <- "Category"

#' Subcategory
#' @export
DATA_DICT_SUBCATEGORY <- "Subcategory"

#' type
#' @export
DATA_DICT_VAR_TYPE <- "type"

#' Standardized variable names dictionary
#' @export
DATA_DICT_VAR_NAME <- "Standardized_VariableNames_Dictionary"

#' Variable description
#' @export
DATA_DICT_DESCRIPTION <- "Variable_Description"

#' redcap
#' @export
DATA_DICT_REDCAP_VAR_NAME <- "redcap"

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

#' Category Period mapping
#' @export
CATEGORY_SHEET_MAP <- list()
CATEGORY_SHEET_MAP[[CATEGORY_PRE_INTERVENTION]] <- SHEET_MAIN
CATEGORY_SHEET_MAP[[CATEGORY_INTERVENTION]] <- SHEET_MAIN
CATEGORY_SHEET_MAP[[CATEGORY_POST_INTERVENTION]] <- SHEET_MAIN
CATEGORY_SHEET_MAP[[CATEGORY_NICU_DISCHARGE]] <- SHEET_MAIN
CATEGORY_SHEET_MAP[[CATEGORY_FOLLOW_UP]] <- SHEET_FOLLOW_UP

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
        exclude_columns = c("siteID", "birthDate")
    ),
    list(
        name = "01-03-maternal-demographics.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "motherRaceOther1",
            "motherRaceOther2",
            "motherRaceOther3",
            "motherRaceOther4",
            "motherRaceOther5",
            "motherRaceOther6",
            "motherRace2",
            "motherEducation2",
            "motherInsurancePublic"
        )
    ),
    list(
        name = "01-04-pregnancy-history.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-05-labor-delivery.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "laborAntibioticsCode2",
            "laborAntibioticsCode3",
            "laborAntibioticsCode4",
            "laborAntibioticsCode5",
            "laborAntibioticsCode6"
        )
    ),
    list(
        name = "01-05_1-pse.csv",
        data_dict = SHEET_MAIN,
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
        name = "01-05_2-emergency-csection.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "deliveryMode",
            "emergencyCSection"
        )
    ),
    list(
        name = "01-06-birth.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-06_1-apgar.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "Apgar5min",
            "Apgar10min",
            "Apgar10minLess5",
            "Apgar10minLessEq5",
            "Apgar5minLessEq5"
        )
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
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "pre_PositiveCultureOrganismCode2",
            "pre_PositiveCultureOrganismCode3",
            "pre_AntibioticsCode2",
            "pre_AntibioticsCode3"
        )
    ),
    list(
        name = "01-10-pre-other-med.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "pre_Anticonvulsants",
            "pre_Anticonvulsants2",
            "pre_Anticonvulsants3",
            "pre_AnalgesicsSedatives",
            "pre_AnalgesicsSedatives2",
            "pre_AnalgesicsSedatives3",
            "pre_Antipyretics",
            "pre_Antipyretics2",
            "pre_Antipyretics3",
            "pre_Paralytics",
            "pre_Paralytics2",
            "pre_Paralytics3"
        )
    ),
    list(
        name = "01-11-pre-imaging.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "pre_HeadSonogramResult2",
            "pre_HeadSonogramResult3",
            "pre_HeadSonogramResult4",
            "pre_HeadSonogramResult5",
            "pre_HeadSonogramResult6",
            "pre_HeadSonogramResult7",
            "pre_HeadSonogramResult8",
            "pre_HeadCTResult2",
            "pre_HeadCTResult3",
            "pre_HeadCTResult4",
            "pre_HeadCTResult5",
            "pre_HeadCTResult6",
            "pre_HeadCTResult7",
            "pre_HeadCTResult8",
            "pre_BrainMRIResult2",
            "pre_BrainMRIResult3",
            "pre_BrainMRIResult4",
            "pre_BrainMRIResult5",
            "pre_BrainMRIResult6",
            "pre_BrainMRIResult7",
            "pre_BrainMRIResult8"
        )
    ),
    list(
        name = "01-12-neuro-exam.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "01-12_1-total-modified-sarnat.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "pre_NeuroExamLevelConsciousnessScore",
            "pre_NeuroExamSpontaneousActivityScore",
            "pre_NeuroExamPostureScore",
            "pre_NeuroExamToneScore",
            "pre_NeuroExamSuckScore",
            "pre_NeuroExamMoroScore",
            "pre_NeuroExamPupilsScore",
            "pre_NeuroExamHeartRateScore",
            "pre_NeuroExamRespirationScore"
        )
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
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "positiveCultureOrganismCode2",
            "positiveCultureOrganismCode3",
            "antibioticsCode2",
            "antibioticsCode3",
            "rewarmingAntibioticsCode2",
            "rewarmingAntibioticsCode3"
        )
    ),
    list(
        name = "02-08-other-med.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "anticonvulsants",
            "anticonvulsants2",
            "anticonvulsants3",
            "analgesicsSedatives",
            "analgesicsSedatives2",
            "analgesicsSedatives3",
            "antipyretics",
            "antipyretics2",
            "antipyretics3",
            "paralytics",
            "paralytics2",
            "paralytics3"
        )
    ),
    list(
        name = "02-09-imaging.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "headSonogramResult2",
            "headSonogramResult3",
            "headSonogramResult4",
            "headSonogramResult5",
            "headSonogramResult6",
            "headSonogramResult7",
            "headSonogramResult8",
            "headCTResult2",
            "headCTResult3",
            "headCTResult4",
            "headCTResult5",
            "headCTResult6",
            "headCTResult7",
            "headCTResult8",
            "brainMRIResult2",
            "brainMRIResult3",
            "brainMRIResult4",
            "brainMRIResult5",
            "brainMRIResult6",
            "brainMRIResult7",
            "brainMRIResult8"
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
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "post_HeadSonogramResult2",
            "post_HeadSonogramResult3",
            "post_HeadSonogramResult4",
            "post_HeadSonogramResult5",
            "post_HeadSonogramResult6",
            "post_HeadSonogramResult7",
            "post_HeadSonogramResult8",
            "post_HeadCTResult2",
            "post_HeadCTResult3",
            "post_HeadCTResult4",
            "post_HeadCTResult5",
            "post_HeadCTResult6",
            "post_HeadCTResult7",
            "post_HeadCTResult8",
            "post_BrainMRIResult2",
            "post_BrainMRIResult3",
            "post_BrainMRIResult4",
            "post_BrainMRIResult5",
            "post_BrainMRIResult6",
            "post_BrainMRIResult7",
            "post_BrainMRIResult8"
        )
    ),
    list(
        name = "03-04-post-neuro-exam.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c("post_NeuroExamSectionID")
    ),
    list(
        name = "03-04_1-total-modified-sarnat.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "post_NeuroExamLevelConsciousnessScore",
            "post_NeuroExamSpontaneousActivityScore",
            "post_NeuroExamPostureScore",
            "post_NeuroExamToneScore",
            "post_NeuroExamSuckScore",
            "post_NeuroExamMoroScore",
            "post_NeuroExamPupilsScore",
            "post_NeuroExamHeartRateScore",
            "post_NeuroExamRespirationScore"
        )
    ),
    list(
        name = "03-05-mri.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "MRIDate",
            "MRIReader",
            "MRIReadDate",
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
            "MRIAbnormalRegion1_c",
            "MRIAbnormalRegion2",
            "MRIAbnormalRegion2_c",
            "MRIAbnormalRegion3",
            "MRIAbnormalRegion3_c",
            "MRIAbnormalSide_c",
            "MRIAbnormalGrayMatterWhiteMatter_c",
            "MRIAbnormalExtent1_c",
            "MRIAbnormalExtent2",
            "MRIAbnormalExtent2_c",
            "MRIAbnormalType_c",
            "MRIAbnormalType2",
            "MRIAbnormalType2_c",
            "MRICerebralAtrophy_c",
            "MRICerebralAtrophyGlobalLocal_c",
            "MRICerebralAtrophyQualAssessCC_c",
            "MRICerebralAtrophyQualAssessVDLeft_c",
            "MRICerebralAtrophyQualAssessVDRight_c",
            "MRIInfarction_c",
            "MRIInfarctionArterialTerritoryLeft_c",
            "MRIInfarctionArterialTerritoryRight_c",
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
        name = "03-05_s1-mri.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "MRINRNPatternOfInjuryMerge"
        )
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
        name = "04-01_1-length-of-stay.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-02-cardiovascular.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-03-respiratory.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargePulmonaryStartDate2",
            "dischargePulmonaryStartTime2",
            "dischargePulmonaryEndDate2",
            "dischargePulmonaryEndTime2",
            "dischargePulmonaryStartDate3",
            "dischargePulmonaryStartTime3",
            "dischargePulmonaryEndDate3",
            "dischargePulmonaryEndTime3"
        )
    ),
    list(
        name = "04-04-hematology.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-05-metabolic.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-06-renal.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-07-gastrointestinal.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-08-skin.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-09-auditory.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-10-surgery.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeSurgeryCode2",
            "dischargeSurgeryCode3"
        )
    ),
    list(
        name = "04-11-infection.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeSepticemiaOrganismCode2",
            "dischargeSepticemiaOrganismCode3",
            "dischargeMeningitisOrganismCode2",
            "dischargeMeningitisOrganismCode3"
        )
    ),
    list(
        name = "04-12-neuro-exam.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeNeuroExamStatus"
        )
    ),
    list(
        name = "04-12_1-total-modified-sarnat.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeNeuroExamLevelConsciousnessScore",
            "dischargeNeuroExamSpontaneousActivityScore",
            "dischargeNeuroExamPostureScore",
            "dischargeNeuroExamToneScore",
            "dischargeNeuroExamSuckScore",
            "dischargeNeuroExamMoroScore",
            "dischargeNeuroExamPupilsScore",
            "dischargeNeuroExamHeartRateScore",
            "dischargeNeuroExamRespirationScore"
        )
    ),
    list(
        name = "04-13-seizure.csv",
        data_dict = SHEET_MAIN
    ),
    list(
        name = "04-14-birth-defect.csv",
        data_dict = SHEET_MAIN,
        exclude_columns = c(
            "dischargeBirthDefectCode2",
            "dischargeBirthDefectCode3"
        )
    ),
    list(
        name = "04-15-home-therapy.csv",
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
        name = "20-09-secondary.csv",
        data_dict = SHEET_FOLLOW_UP
    ),
    list(
        name = "20-10-outcome.csv",
        data_dict = SHEET_FOLLOW_UP
    ),
    list(
        name = "20-10_1-disability-level-death.csv",
        data_dict = SHEET_FOLLOW_UP
    )
)

#' Significance level / threshold for p-value
#' @export
P_VALUE_THRESHOLD <- 10^(-5)
