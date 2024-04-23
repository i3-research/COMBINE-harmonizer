#' to inverse of bool
#
#' @param value value
#' @export
to_inv_bool <- function(value) {
    if (is.na(value)) {
        return(NULL)
    }

    if (!typeof(value) == "character") {
        return(as.numeric(value))
    }

    if (value %in% c("true", "TRUE", "True")) {
        return(1.0)
    } else if (value %in% c("false", "FALSE", "False")) {
        return(0.0)
    } else if (value %in% c("unknown")) {
        return(NULL)
    }

    message(c("[WARN] to_inv_bool: invalid val: ", value))
    return(0.0)
}

#' int to float (assuming already int).
#'
#' @param value value
#' @export
to_inv_int <- function(value) {
    if (is.na(value)) {
        return(NULL)
    }

    return(as.numeric(value))
}

#' float to float (assuming already float).
#'
#' @param value value
#' @export
to_inv_float <- function(value) {
    if (is.na(value)) {
        return(NULL)
    }

    return(as.numeric(value))
}

#' inverse text: still the same value.
#'
#' @param value value
#' @export
to_inv_text <- function(value) {
    return(value)
}
