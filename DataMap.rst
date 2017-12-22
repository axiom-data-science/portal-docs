.. include:: globals.txt

########
Data Map
########

**********************
Displaying Data Layers
**********************

*Several features under this heading are currently under development. Please check back soon for updates.*

Viewing Data in the Map Portal
==============================

Observation Definitions
-----------------------

For the purposes of this documentation, it's helpful to understand how the following terms are defined:

.. csv-table::
	:header: "Term", "Definition"
	:widths: 15, 50

	"**Hexagonal bin**", "A group of stations that are aggregated into a hexagon for visual summary."
	"**Station**", "A device that collects data related to the weather and environment using many different sensors (e.g. weather station)."
	"**Sensor**", "An individual measurement device affixed or associated with a station (e.g. thermometer, barometer)."
	"**Parameter**", "The type of value measured by the sensor (e.g. temperature, pressure)."

Real-Time Data
--------------

Real-time stations are aggregated into hexagonal bins to visually summarize data over a large spatial area when the map is zoomed out. This means that data from more than one station may be displayed within a hexagon. The color of the hexagon represents the average value of the select sensor parameter within that hexagon. For example, if air temperature is the selected sensor type, then the hexagon color will reflect the average temperature for all stations within that bin.

To view a summary of the station data contain within a hexagon, hover over the hexagon. The number of stations aggregated within that hexagon will be displayed as "n stations." The average value for the selected sensor type will be also be shown, followed by the time range for which that value was measured. If there are not more than one station aggregated within a hexagon, the hover-over view will display the value for the selected parameter, followed by a list of the other sensor types associated with that station and the range of associated data. By default, only five of the sensors are shown in the hover window. More sensors are indicated by the "n more sensors" in the lower left of the window.

To view data for an individual station, zoom in on the map. The hexagons will soften into points that represent the individual stations that were aggregated into that hexagon. To view current readings from that station, hover over its point. As shown in the image below, a pop-up window will display some basic information about the station, including its name, data source affilitation(s), lattitude and longitude, current readings, and available sensor parameters (e.g., air temperature, water level, and water temperature as in the example below).

|sensor_hover|

To view station data, click on the point. As shown in the image below, data from the station will appear in the data display window in the lower left corner of the window. You can use the dropdown menu in the data display window to select data from different sensors, and you can use the time slider to adjust the time period of the data.

|sensor_select|

More details about how to explore, visualize, analyze, and download these data can found on the pages that follow.

Glider Data
-----------

Ocean gliders are autonomous underwater vehicles used to collect ocean data, including temperature, salinity, conductivity, and other important measures. Unlike stationary sensor platforms such as buoys, gliders move through the water column and collect data at different locations over time.

.. note::
	For more information on gliders, see NOAA's `"What is an ocean glider" <https://oceanservice.noaa.gov/facts/ocean-gliders.html>`_ page.

Glider data can be visualized by accessing it from a data catalog. Here's an example of how to visualize glider data from the Central and Northern California Ocean Observing System (CeNCOOS) data portal:

#. Go to the CeNCOOS `data portal <http://dev.axiomdatascience.com/?portal_id=20#search?tagId=Gliders>`_.
#. Filter the catalog by selecting ``Gliders`` tag from the list on the left.
#. This will display a list of glider datasets collected off the coast of California.

To visualize the dataset, click on its name. In our CeNCOOS example, to visualize the first dataset on the list, follow these steps:

#. Click on `UCSC260-20150520T0000 <http://dev.axiomdatascience.com/?portal_id=20#search?tagId=Gliders>`_.
#. Wait for the dataset to load.

Once the dataset has loaded, you should see the view in the image below:

|glider_data_viz|

From here there are several ways to explore the glider dataset:

#. overlaid on imagery on the upper-left,
#. described by basic metadata on the lower-left,
#. displayed in a 2-dimensional plot on the upper-right, and
#. plotted in a 3-dimensional plot on the lower-right.

Additionally, the dataset can be downloaded in several different formats by using the blue downloads button in the top right |glider_data_download_icon|.

These features and more will be explored more thoroughly in upcoming updates to this documentation.

**************
Comparing Data
**************

The catalog and portal offer multiple ways of comparing data within both the mapped interface and within a :ref:`data view <data-views>`.

For assistance, please contact us via the red Feedback button |feedback_button_icon| in the top right corner of the ESM page.

Add Data Layers to the Map
==========================

There are multiple ways of adding data layers to the map.

From the data catalog:

1. From the :ref:`data catalog <data-catalog>`, browse or search for the layers you want to add.
2. On the results page, use the ``+`` icon next to any of the thumbnails, an indicator showing how many layers are currently queued will show up in the black, upper menu.
3. You can add multiple layers, it's just like a data "shopping cart".
4. Remove layers by selecting the layer indicator in the black, upper menu, and using the ``X`` icons.

From the data map:

1. From within the interactive map, use the `Search for data` bar.
2. From the results popup, use the ``+`` icon next to the layer you want to add to the map.

Climatology Charts
==================

If there are more than three years of data coverage for stations or gridded data, charts on the portal show statistics from past weather patterns along with the current data. These are not officially climatologies, which typically require 30 years of data, but they can still be useful to quickly compare how the current year fits into the data that's available at a station.

Historical patterns in station observations
-------------------------------------------

1. From the real-time sensor map or historical sensor map, click on any station that has more than three years of data.
2. The default graph will show binned data, with the dark gray line indicating the mean and the gray envelope representing the min and max values within the current year.


Historical patterns in gridded data
-----------------------------------

1. Clicking on any gridded dataset will open a :ref:`virtual sensor <virtual-sensor`.
2. If the dataset has more than three years of data, the default graph will show binned data.
3. The dark gray line indicating the mean and the gray envelope representing the min and max values within the current year.

Customize Data Charts
=====================

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

.. ***************************
.. Query and Save Vector Layer
.. ***************************

.. ***********
.. Time Slider
.. ***********

.. Hex-Binned Data
.. ===============

.. Model Data 
.. ==========

.. 4D Profile Data
.. ===============

.. *******************************
.. Add More Data Layers to the Map
.. *******************************

.. ***************************
.. Customize Individual Layers
.. ***************************

.. ***************************************
.. Station and Source Level Metadata Pages
.. ***************************************

.. *********************
.. Customize Portal View
.. *********************

.. ***********
.. Data Sharts
.. ***********

.. ********
.. Time Slider
.. ***********

.. ***************************
.. Profile Data Visualizations
.. ***************************

.. ************
.. Polygon Tool
.. ************

.. ***************
.. Virtual Sensors
.. ***************

.. ***********
.. Map Sharing
.. ***********

.. ***********
.. Data Charts
.. ***********

.. *This feature underdevelopment. Check back soon for updates.*

****************
Downloading Data
****************

Data may be downloaded through the data catalog, as described in `this <http://help.axds.co/portals/DataCatalog.html#downloading-visualized-data>`_ section.

**********
Data Views
**********

*This feature underdevelopment. Check back soon for updates.*


