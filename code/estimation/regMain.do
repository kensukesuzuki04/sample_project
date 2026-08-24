*==============================================================================
* regMain.do - example estimation script
*
* Shows the repository path convention for Stata:
*   - one global root, set once at the top
*   - every other path built from it
*   - outputs mirror the code/ subfolder name (estimation)
*
* Usage: edit the root path below, then run this file.
*==============================================================================

clear all
set more off

* --- paths -------------------------------------------------------------------
* Set this to YOUR local clone. This is the only absolute path in the file.
global root "C:/Users/<username>/GitHub/sample_project"

global data         "$root/data"
global intermediate "$root/intermediate/estimation"
global output       "$root/output/estimation"

capture mkdir "$intermediate"
capture mkdir "$output"

* --- data --------------------------------------------------------------------
* Real projects load from $data. This example uses Stata's bundled auto dataset
* so the script runs without the Dropbox junctions being set up.
capture use "$data/sample.dta", clear
if _rc {
    display as text "sample.dta not found - using the bundled auto dataset."
    sysuse auto, clear
}

* --- estimation --------------------------------------------------------------
regress price mpg weight foreign

* --- export ------------------------------------------------------------------
* Outputs never go into code/ - they go to output/estimation/.
estimates store main
esttab main using "$output/regMain.tex", replace se label ///
    title("Determinants of price")

display as result "Done. Output written to $output"
