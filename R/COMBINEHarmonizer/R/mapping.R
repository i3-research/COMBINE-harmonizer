#
library(readxl)
library(stringr)
library(dplyr)

#' @export
mapping_env <- new.env()
mapping_env$MAPPING <- list()
mapping_env$INV_MAPPING <- list()

#' Initialize inverse mapping from standardized variables to the corresponding rank.
#'
#' @param filename dictionary filename
#' @param column the column name for inv mapping.
#' @export
init_inv_mapping <- function(filename, column) {
    sheet_names <- readxl::excel_sheets(filename)
    valid_sheet_names <- setdiff(sheet_names, COMBINEHarmonizer::SHEET_RESERVED_TABS)

    for (sheet_name in valid_sheet_names) {
        df <- readxl::read_xlsx(filename, sheet = sheet_name)
        update_inv_mapping(sheet_name, df, column)
    }
}

update_inv_mapping <- function(sheet_name, df, column) {
    message(c("[INFO] update_inv_mapping: sheet_name: ", sheet_name))
    df_columns <- colnames(df)
    if (!(column %in% df_columns)) {
        return(NA)
    }

    df[column] <- sapply(df[column], as.numeric)

    is_invalid <- (df$name == "") | sapply(df$name, is.na)
    df_valid <- df[!is_invalid, ]

    df_valid_dedup <- df_valid[!duplicated(df_valid["name"]), ]
    df_valid_dedup

    the_map <- df_valid_dedup[[column]]
    names(the_map) <- df_valid_dedup$name
    mapping_env$INV_MAPPING[[sheet_name]] <- the_map
}

#' Get inverse-value from inv_mapping
#
#' @param the_type the type of the value (sheet_name)
#' @param value the value
#' @return inverse value (or NA if not available)
#' @export
get_inv_mapping_value <- function(the_type, value) {
    if (is.na(value)) {
        return(NA)
    }

    type_values <- names(mapping_env$INV_MAPPING[[the_type]])

    if (value == "" && !("" %in% type_values)) {
        return(NA)
    }

    if (!(value %in% type_values)) {
        message(c("[WARN] value not in the type: the_type: ", the_type, " value: ", value))
        return(NA)
    }

    mapping_env$INV_MAPPING[[the_type]][[value]]
}
