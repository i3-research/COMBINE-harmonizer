library(readxl)
library(tidyr)

#' Load Data Dictionary with filling the category column
#'
#' @param filename data dictionary filename
#' @param sheet_name sheet name to load
#' @export
load_data_dict <- function(filename, sheet_name) {
    df_data_dict <- readxl::read_xlsx(filename, COMBINEHarmonizer::SHEET_VARIABLES)

    is_valid_var <- !is.na(df_data_dict[[COMBINEHarmonizer::DATA_DICT_VAR_NAME]])
    is_valid_type <- !is.na(df_data_dict[[COMBINEHarmonizer::DATA_DICT_VAR_TYPE]])
    is_valid <- is_valid_var & is_valid_type
    df_data_dict_valid <- df_data_dict[is_valid, ]

    df_data_dict_valid <- data_dict_fill_category(df_data_dict_valid)

    sheet_names <- lapply(
        df_data_dict_valid[[COMBINEHarmonizer::DATA_DICT_CATEGORY]],
        \(x) COMBINEHarmonizer::CATEGORY_SHEET_MAP[[x]]
    )
    is_valid_sheet_name <- sheet_names == sheet_name

    df_data_dict_valid <- df_data_dict_valid[is_valid_sheet_name, ]

    return(df_data_dict_valid)
}

data_dict_fill_category <- function(df) {
    return(tidyr::fill(df, COMBINEHarmonizer::DATA_DICT_CATEGORY))
}
