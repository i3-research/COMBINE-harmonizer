library(dplyr)

#' Compute Pearson's correlation coefficient analysis between x-columns and y-columns
#'
#' @param df Dataframe to process
#' @param x_columns x-columns for Pearson's correlation coefficient analysis
#' @param y_columns y-columns for Pearson's correlation coefficient analysis
#' @return Dataframe with ycolumns as (r, R^2, p-value, valid, valid-x, valid-y, valid-percent)
#' @export
corr <- function(df, x_columns, y_columns) {
    df_rets <- list()
    for (idx in seq_along(x_columns)) {
        x_column <- x_columns[idx]
        message(c("corr: (", idx, "/", length(x_columns), ") x_column: ", x_column))
        for (y_column in y_columns) {
            corr <- NA
            r2 <- NA
            pvalue <- NA

            corr_coeff_ret <- corr_coeff(df, x_column, y_column)
            coeff <- corr_coeff_ret$coeff
            meta <- corr_coeff_ret$meta

            corr <- coeff$estimate[["cor"]]
            if (!is.na(corr)) {
                r2 <- corr^2
            }
            pvalue <- coeff$p.value

            val <- list(
                corr = corr,
                r2 = r2,
                pvalue = pvalue,
                valid = meta$valid,
                valid_x = meta$valid_x,
                valid_y = meta$valid_y,
                valid_percent = meta$valid_percent
            )
            df_ret <- data.frame(
                x = rep(x_column, length(val)),
                y = unlist(purrr::map(names(val), \(x) paste(y_column, x, collapse = " "))),
                val = unname(unlist(val))
            )
            df_rets <- dplyr::bind_rows(df_rets, df_ret)
        }
    }
    return(df_rets)
}

corr_coeff <- function(df, x_column, y_column) {
    is_valid_x <- !is.na(df[[x_column]])
    is_valid_y <- !is.na(df[[y_column]])
    is_valid <- is_valid_x & is_valid_y
    df_valid <- df[is_valid, ]

    meta <- list(
        valid = sum(is_valid),
        valid_x = sum(is_valid_x),
        valid_y = sum(is_valid_y),
        df = nrow(df),
        valid_percent = as.numeric(sum(is_valid)) / as.numeric(nrow(df))
    )

    if (meta$valid == 0) {
        message(c("[WARN] no valid data: x_column: ", x_column, " y_column: ", y_column))
        coeff <- list(
            estimate = list(cor = NA),
            p.value = NA
        )
        return(list(coeff = coeff, meta = meta))
    }

    coeff <- cor.test(
        x = df_valid[[x_column]],
        y = df_valid[[y_column]],
        method = "pearson",
        alternative = "two.sided"
    )

    return(list(coeff = coeff, meta = meta))
}
