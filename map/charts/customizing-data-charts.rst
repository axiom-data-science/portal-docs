#######################
Customizing Data Charts
#######################

* Selecting the ``Legend`` icon gives you access to turn on and off historical statistics.
	- **Minimum** of the entire time-series within each bin is represented by the dashed blue line
	- **Mean to the 10th percentile** of the data is represented by the blue shaded area
	- **Mean** of the entire time-series within each bin is represented by the dashed gray line
	- **Mean to the 90th percentile** of the data is represented by the red shaded area
	- **Maximum** of the entire time-series within each bin is represented by a dashed red line
* Use the time-slider on the bottom of the chart to set a time range, or use the gear icon next to the slider to type in bounds
* The gear above the graph allows you to set the chart type and other graphing options.
	- Chart types:
		- **Line chart**: A chart of the current values with historical statistics
		- **Climatology**: Year-to-date monthly mean values of the current year compared to historical statistics
		- **Anomaly**: The data values minus the mean values across all years
		- **Curtain**: If data is available at depth, the chart will show depth on the y-axis with the values represented by colors.
	- Time bin - data can be binned across years within the following time periods:
		- **All**: no binning
		- **Days**: data is binned by day, and statistics are by day number across years
		- **Weeks**: data is binned by week, and statistics are by week number across years
		- **Months**: data is binned by month, and statistics are by month number across years
		- **Seasons**: data is binned by northern hemisphere seasons defined as the following:
			- Winter: December, January, February
			- Spring: March, April, May
			- Summer: June, July, August
			- Fall: September, October, November
		- **Years**: data is binned by years, and statistics are across years

.. note::
	Percentiles are calculated by ordering all values in the time bin across all recorded years and selecting the value at the 10% and 90% locations in the array. I.e., the shaded percentile region is telling you what the "typical" temperature is at that time of year excluding the 10% most extreme values on either end.

