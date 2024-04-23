#' build inv value map
#' @export
build_inv_value_map <- function(filename, sheet_name) {
    df <- COMBINEHarmonizer::load_data_dict(filename, sheet_name)

    the_types <- df[[COMBINEHarmonizer::VAR_TYPE]]

    ret <- lapply(the_types, build_inv_value_map_core)
    names(ret) <- df[[COMBINEHarmonizer::VAR_NAME]]

    return(ret)
}

build_inv_value_map_core <- function(the_type) {
    if (the_type == "bool") {
        return(COMBINEHarmonizer::to_inv_bool)
    } else if (the_type == "int") {
        return(COMBINEHarmonizer::to_inv_int)
    } else if (the_type == "float") {
        return(COMBINEHarmonizer::to_inv_float)
    } else if (the_type %in% names(COMBINEHarmonizer::mapping_env$INV_MAPPING)) {
        return(\(value) COMBINEHarmonizer::get_inv_mapping_value(the_type, value))
    } else {
        return(COMBINEHarmonizer::to_inv_text)
    }
}
