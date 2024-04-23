#' flatten filename prefix
#' @export
flatten_filename_prefix <- function(filename) {
    filename_prefix <- sub("\\.csv$", "", filename)
    the_list <- strsplit(filename_prefix, "-")[[1]]
    tryCatch(
        {
            as.integer(substr(the_list[2], 1, 2))
            paste(the_list[1:2], collapse = "-")
        },
        error = function(e) {
            the_list[1]
        }
    )
}

#' flatten column tuple
#'
#' Flatten column of the flattened csv to the tuple (prefix, var-name, postfix)
#' In R, the columns become X\[prefix\].\[var-name\].\[postfix\]
#'
#' @export
flatten_column_tuple <- function(column) {
    column <- sanitize_column(column)
    column_list <- strsplit(column, "\\.")[[1]]

    prefix <- ""
    var_name <- ""
    postfix <- NA
    if (length(column_list) == 1) {
        var_name <- column_list[1]
    } else if (length(column_list) == 2) {
        var_name <- column_list[1]
        print(c("[WARN] flatten_column_tuple: column_list == 2 in column:", column))
    } else if (length(column_list) == 3) {
        prefix <- paste(column_list[1:2], collapse = "-")
        var_name <- column_list[3]
    } else if (length(column_list) == 4) {
        prefix <- paste(column_list[1:2], collapse = "-")
        var_name <- column_list[3]
        postfix <- c(column_list[4])
    } else if (length(column_list) == 5) {
        prefix <- paste(column_list[1:2], collapse = "-")
        var_name <- column_list[3]
        postfix <- column_list[4:5]
    } else {
        prefix <- paste(column_list[1:2], collapse = "-")
        var_name <- column_list[3]
        postfix <- column_list[4:5]
        print(c("[WARN] flatten_column_tuple: > 2 ':' in column:", column))
    }

    return(c(prefix, var_name, postfix))
}

#' flatten column prefix
#' @export
flatten_column_prefix <- function(column) {
    column <- sanitize_column(column)
    column_list <- strsplit(column, "\\.")[[1]]
    if (length(column_list) < 3) {
        return("")
    }

    return(paste(column_list[1:2], collapse = "-"))
}

sanitize_column <- function(column) {
    if (substring(column, 1, 1) != "X") {
        return(column)
    }

    return(substring(column, 2))
}
