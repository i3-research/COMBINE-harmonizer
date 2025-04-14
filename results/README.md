# Results

Currently there are 4 results in this directory, data dictionary, summary of the variables, Pearson's correlation coefficient analysis, and the REDCap data dictionary.

## Data Dictionary (`Dictionary_HIE_clinical_variables.xlsx`)

This data dictionary is manually input based on the knowledge to the datasets, including the following tabs:
* `Variables`: the definition of the standardized variable names (`Standardized_VariableNames_Dictionary`) and the corresponding Category, Subcategory, type, description, REDCap variable name, and the mapping to the variable names in the datasets. Notice that the REDCap variable names and the mapping to the variable names in the datasets in this data dictionary are only the preliminary information. Please refer to `REDCap/data_dictionary.csv` and `variable-summary.xlsx` for the finalized version.
* `name convention`: basic rules in naming variables.
* Other tabs: the mapping of ordinal types (with `_rank` in the column) or nominal types (without `_rank` in the column). For ordinal types, in addition to `_rank` as the default rank setting, other rank settings can be provided with prefix `_rank.` and specified in the code (ex: `_rank.0` in `signOfHIETone`).

## Summary of the Variables (`variable-summary.xlsx`)

The content in this spreadsheet is generated from `Analysis/00-check-basic-info.ipynb`, including the following tabs:
* `01-number of variables`: from `20-01-basic-info-len-columns.csv`, specifying number of variables in each generated file.
* `01-1-number of variables-detail`: inferred tab from `01-number of variables`.
* `02-variable-info`: from `20-02-basic-info-variables.csv`, specifying the information of each variable, including:
    * number of data with (and without) value.
    * the corresponding `LH` and `OC` variable name.
    * the type of the variable.
    * category and subcategory that this variable belongs to.
* `02-1-variable-type`: inferred from `02-variable-info`, focusing on the variable types.
* `02-2-filename-distribution`: inferred from `01-number of variables` and `02-variable-info`, focusing on the number of the variables in each file.
* `02-3-type-distribution`: inferred from `02-variable-info`, focusing on the distribution of the types.
* `03-death-disability-level`: from `20-03-basic-info-death-disability-distribution.csv`, specifying the distribution of `disability level and death` in different studies.
* `03-1-death-disability-level-with-missing`: inferred from `03-death-disability-level`, adding number of missing data of `disability level and death`.
* `03-2-death-disability-level-distribution`: inferred from `03-1-death-disability-level-with-missing`.

Variables with similar concept are excluded in `variable-summary.xlsx`. The excluded variables are listed in `exclude_columns` in `COMBINE_harmonizer.constants.FILENAME_INFOS`.

## Pearson's Correlation Coefficient Analysis (`correlation-analysis.xlsx`)

The content of this spreadsheet is generated from `Analysis/11-correlation-coefficient.ipynb`, including the following tabs, where the variables with blue color are the variables of interest:
* `correlation-disability-level-death`: Association between variables and 5-category `disability-level and death`.
* `correlation-moderate-servere-disability-death`: Association between variables and Boolean `moderate/severe disability or death`.
* `correlation-bayley-iii-cog`: Association between variables and Bayley-III Cognitive Composite Scales.
* `correlation-bayley-iii-cog-R`: Association between variables and Bayley-III Cognitive Composite Scales, from `Analysis/11-correlation-coefficient-R.ipynb`.
* `correlation-bayley-iii-lang`: Association between variables and Bayley-III Language Composite Scales.
* `correlation-bayley-iii-motor`: Association between variables and Bayley-III Motor Composite Scales.

## REDCap

In this directory, variables in each category / subcategory are specified in `instruments-csv` files, where the first number in the prefix of the filename represents the chronological category, as:
* 01: Pre-intervention
* 02: Intervention
* 03: Post-intervention
* 04: NICU Discharge
* 05: Follow Up

All the variables are aggregated in `data_dictionary.csv` generated from REDCap.

## License

[Results from COMBINE-harmonizer](https://github.com/i3-research/COMBINE-harmonizer/tree/main/results) by Consortium Of MRI Biomarkers In Neonatal Encephalopathy (COMBINE) is marked with [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)
