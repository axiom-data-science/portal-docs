.. include:: globals.txt

.. _comparing-data:

##############
Comparing Data
##############

The catalog and portal offer multiple ways of comparing data within both the mapped interface and within a :ref:`data scenario <data-scenarios>`.

For assistance, please contact us via the red Feedback button |feedback_button_icon| in the top right corner of the ESM page.

.. _add-data-layers-to-the-map:

**************************
Add Data Layers to the Map
**************************
There are multiple ways of adding data layers to the map.


From the data catalog
=====================
1. From the :ref:`data catalog <data-catalog>`, browse or search for the layers you want to add.
2. On the results page, use the ``+`` icon next to any of the thumbnails, an indicator showing how many layers are currently queued will show up in the black, upper menu.
3. You can add multiple layers, it's just like a data "shopping cart".
4. Remove layers by selecting the layer indicator in the black, upper menu, and using the ``X`` icons.

From the Portal
===============
1. From within the interactive map, use the `Search for data` bar.
2. From the results popup, use the ``+`` icon next to the layer you want to add to the map.


.. _climatology-charts:

******************
Climatology Charts
******************
If there are more than three years of data coverage for stations or gridded data, charts on the portal show statistics from past weather patterns along with the current data. These are not officially climatologies, which typically require 30 years of data, but they can still be useful to quickly compare how the current year fits into the data that's available at a station.


Historical patterns in station observations
===========================================
1. From the real-time sensor map or historical sensor map, click on any station that has more than three years of data.
2. The default graph will show binned data, with the dark gray line indicating the mean and the gray envelope representing the min and max values within the current year.


Historical patterns in gridded data
===================================
1. Clicking on any gridded dataset will open a :ref:`virtual sensor <virtual-sensor`.
2. If the dataset has more than three years of data, the default graph will show binned data.
3. The dark gray line indicating the mean and the gray envelope representing the min and max values within the current year.


.. _customize-data-charts:

*********************
Customize Data Charts
*********************
- Selecting the ``Legend`` icon gives you access to turn on and off historical statistics.
	- **Minimum** of the entire time-series within each bin is represented by the dashed blue line 
	- **Mean to the 10th percentile** of the data is represented by the blue shaded area
	- **Mean** of the entire time-series within each bin is represented by the dashed gray line
	- **Mean to the 90th percentile** of the data is represented by the red shaded area
	- **Maximum** of the entire time-series within each bin is represented by a dashed red line
- Use the time-slider on the bottom of the chart to set a time range, or use the gear icon next to the slider to type in bounds
- The gear above the graph allows you to set the chart type and other graphing options.
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



.. _query-and-save-vector-layer:

***************************
Query and Save Vector Layer
***************************










.. _time-slider:

***********
Time Slider
***********


