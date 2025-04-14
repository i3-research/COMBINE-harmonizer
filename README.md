# COMBINE-harmonizer

Consortium Of MRI Biomarkers In Neonatal Encephalopathy (COMBINE) aims to develop prognostic biomarkers to predict adverse outcomes and ultimately improve patient care for the neonatal encephalopathy (NE) population. This is the repository for harmonizing the NE-related datasets.

Currently the following datasets are included:

* [Late-Hypothermia](https://doi.org/10.57982/hs6z-4j46) ([LH, Laptook et al., JAMA, 2017](https://doi.org/10.1001/jama.2017.14972))
* [Optimizing-Cooling](https://doi.org/10.57982/yjay-3487) ([OC, Shankaran et al., JAMA, 2017](10.1001/jama.2017.7218))

## Getting Started

The results can be reproduced with the following steps:

* Install `COMBINE_harmonizer` python package: `pip install .`
* Install `COMBINEHarmonizer` R package: `R -e 'remotes::install_local("./R/COMBINEHarmonizer")'`.
* Download the [LH](https://doi.org/10.57982/hs6z-4j46) and [OC](https://doi.org/10.57982/yjay-3487) datasets.
* Copy config.tmpl.yaml to config.yaml and update the corresponding configurations.
* Execute: `scripts/exec-all-ipynb.sh`

## Data Organization

This repository provides the following files and directories to harmonize the data:

* **Dictionary_HIE_clinical_variables.xlsx**: Data dictionary of the data harmonization framework.
* **config.yaml.tmpl**: Template for the configuration.
* **COMBINE_harmonizer**: utility functions for python scripts.
* **Dictionary**: Dictionary related `.ipynb` scripts.
* **LH**: LH-specific harmonization `.ipynb` scripts.
* **OC**: OC-specific harmonization `.ipynb` scripts.
* **Merge**: The `.ipynb` scripts for merging the dataset-specific data.
* **Analysis**: The `.ipynb` scripts for analyzing the data.
* **REDCap**: The `.ipynb` scripts for uploading to the [REDCap](https://project-redcap.org/) database.
* **results**: Results from the scripts.
* **zz-exec.ipynb**: The `.ipynb` script executing all the scripts to reproduce the results.
* **scripts**: The shell scripts for development and operation.

## LH Dataset

The following files are not available on the public dataset. Please contact the corresponding owner for more information:

* Participant registry data (lh01.sas7bdat)
* Fluctuated Temperature (lh06f.sas7bdat)
* MRI registry data (lhmr01.sas7bdat)
* MRI summary from the local hospitals (lhmr02.sas7bdat)
* MRI data from the designated radiologists in the study (lhmr03.sas7bdat)
* Lost Followup (lf12.sas7bdat)

## OC Dataset

The following files are not available on the public dataset. Please contact the corresponding owner for more information:

* Participant registry data (oc01.sas7bdat)
* Post-intervention Temperature (oc06d.sas7bdat)
* Infection (oc09i.sas7bdat)
* MRI registry data (ocmr01.sas7bdat)
* MRI summary from the local hospitals (ocmr02.sas7bdat)
* MRI data from the designated radiologists in the study (ocmr03.sas7bdat)
* Lost Followup (of12.sas7bdat)

## REDCap

We can construct the REDCap format (instruments and data dictionary) through:

* `./scripts/exec-all-redcap.sh`

Please refer to the script and walk through the `.ipynb` files for more information.

## Results

Please read [results/README.md](https://github.com/i3-research/COMBINE-harmonizer/tree/main/results/README.md) for more information about results.

## License

The Software is © 2025 Consortium Of MRI Biomarkers In Neonatal Encephalopathy (COMBINE) under the [MIT License](https://opensource.org/license/mit).

[Results from COMBINE-harmonizer (in /results)](https://github.com/i3-research/COMBINE-harmonizer/tree/main/results) by Consortium Of MRI Biomarkers In Neonatal Encephalopathy (COMBINE) are marked with [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).
