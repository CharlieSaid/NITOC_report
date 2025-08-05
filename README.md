# NITOC REPORT
 - by Charlie Said

## Rationale

## Work Log
Issues I encountered.

### Non-standardized event names
Several years list Lincoln Douglas debate as "Lincoln-Douglas", while modern years eliminate the hyphen.  This inconsistency across years created a split column which had to be repaired in the data gathering script.

Later on, same issue encountered with Mars Hill and Mars Hill Impromptu.
### Non-standardized tournament name
For every year except 2019, the official name of NITOC has been the National Invitational Tournament of Champions.  In 2019, however, it is listed as the National Invitational Tournament Of Champions.  The only difference is the capitalization of the word "of".  To resolve this issue, I simply selected tournaments whose name included "National Invitational Tournament" and didn't even try to handle both cases.  This solution maximizes simplicity and readibility.

### Plotnine
Seaborn works well with MatPlotLib and Pyplot, but is lacking some of R's nicer features.  I discovered Plotnine, a package that lets you build R plots in Python, and it works quite well.  The only issue so far is the formatting inconsistency.