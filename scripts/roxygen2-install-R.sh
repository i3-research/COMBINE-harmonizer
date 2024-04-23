#!/bin/bash

Rscript -e 'roxygen2::roxygenize("./R/COMBINEHarmonizer")'
Rscript -e 'remotes::install_local("./R/COMBINEHarmonizer", force = TRUE)'
