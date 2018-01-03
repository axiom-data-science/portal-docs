.. include:: globals.txt

########
Data Map
########

The map provides interactive data exploration, mapping, and charting for visualizable layers available in the catalog. The map is highly customizable, enabling deep exploration of the data. Advanced charting features allow users to view and summarize multiple datasets, and to create custom Data Views to compare data sources, bin by time, or plot climatologies and anomalies of timeseries datasets. Users can create and share custom compilations of biological, sensor, and model outputs to spotlight environmental events or geographic locations. 


**********************
Display Data Layers
**********************

This section provides information on how to view, learn more, and interact with data layers in the map. For the purposes of this documentation, it's helpful to understand how the following terms are defined:

.. csv-table::
	:header: "Term", "Definition"
	:widths: 15, 50

	"**Hexagonal bin**", "A group of stations that are aggregated into a hexagon for visual summary."
	"**Station**", "A device that collects data related to the weather and environment using many different sensors (e.g. weather station)."
	"**Sensor**", "An individual measurement device affixed or associated with a station (e.g. thermometer, barometer)."
	"**Parameter**", "The type of value measured by the sensor (e.g. temperature, pressure)."

*Several features on this page are currently under development. Check back soon for updates.*

View Data in the Map Portal
===========================

All real-time and near real-time data within the portal are accessible as interactive visualizations in the map view. Historical data are also accessible as interactive visualizations in the map, with the exception of datasets that may be published directly to the catalog from the Research Workspace. More details about how to explore, visualize, analyze, and download these data can found on the pages that follow.

Overview of Real-Time Data
---------------------------

Real-time data are ingested, served, and displayed in the portal at the same frequency the data are collected (and sometimes reported) by the originator with little to no delay. Examples of real-time assets include weather stations, oceanographic buoys, and webcams.

Real-time data from observation stations are aggregated into hexagonal bins to visually summarize data over a large spatial area when the map is zoomed out. This means that data from more than one station may be displayed within a hexagon. The color of the hexagon represents the average value of the select sensor parameter within that hexagon. For example, if air temperature is the selected sensor type, then the hexagon color will reflect the average temperature for all stations within that bin.

To view a summary of the station data contain within a hexagon, hover over the hexagon. The number of stations aggregated within that hexagon will be displayed as "n stations." The average value for the selected sensor type will be also be shown, followed by the time range for which that value was measured. If there are not more than one station aggregated within a hexagon, the hover-over view will display the value for the selected parameter, followed by a list of the other sensor types associated with that station and the range of associated data. By default, only five of the sensors are shown in the hover window. More sensors are indicated by the "n more sensors" in the lower left of the window.

To view data for an individual station, zoom in on the map. The hexagons will soften into points that represent the individual stations that were aggregated into that hexagon. To view current readings from that station, hover over its point. As shown in the image below, a pop-up window will display some basic information about the station, including its name, data source affilitation(s), lattitude and longitude, current readings, and available sensor parameters (e.g., air temperature, water level, and water temperature as in the example below).

|sensor_hover|

To view station data, click on the point. As shown in the image below, data from the station will appear in the data display window in the lower left corner of the window. You can use the dropdown menu in the data display window to select data from different sensors, and you can use the time slider to adjust the time period of the data.

|sensor_select|


Overview of Near-Real Time Data
-------------------------------

Near real-time data are ingested by the portal at the same frequency that the data are made available; however, there is some delay (hours to days) between data collection and when the data provider makes it available. Examples of near real-time assets include model outputs, satellite images, and derived satellite products.

Model and Satellite Data
""""""""""""""""""""""""

Model outputs or satellite imagery have been visually abstracted in the portal to include a schematic representation of the data attributes or variables. The variable currently being displayed is shown as a title in the right hand legend bar. The variable being displayed can be changed by clicking the caret icon and selecting from the other variables that may be available (note: the variables available will vary depending on which data layer you are viewing). The current date and time for the data being displayed is shown in the right hand legend bar beneath the data layer title.

To select your area of interest use the pan and zoom features on the map. To display values within your area of interest, hover your mouse over the map. The name of the data layers, latitude/longitude, date, time, and the value at the given location will appear. If you click on the map in any location covered by a multi-dimensional model or grid, a data chart window showing the data trends over time will appear. More information can be found in the Data Charts section of this document.

The timer slider bar at the bottom of the map can be used to view the various time intervals of data available. The interval available will vary depending on which data layer you are view. More information about using the time slider can be found in the Time Slide section of this document. Depending on your zoom level and internet speed, these time intervals layers could take a little to appear so be patient as these layers load. Once you do have them in the cache they will load more quickly as you step forward and backwards through the time.

The data layer legend on the right hand shows the color scale that is used to represent the unit of measurement. You can change the palette and scale settings by clicking on the color bar. Select among the different color palettes using the drop down menu. The legend scale can be changed by either adjusting the scale slider, or by clicking on the gear icon and entering or advancing the bounds control interval. When the map is zoomed in, the scale and color for that area can be automatically set for the data in view by clicking the ‘Autoset for data view’ button. 

Overview of Historical Data
---------------------------

Historical data are data that are one month old or older. Historical data available through the portal were sometimes collected in real-time and subsequently archived; other historical data are ingested from local or national archives upon stakeholder request.


Mobile Platforms (Gliders)
""""""""""""""""""""""""""

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

Biological Observations
"""""""""""""""""""""""

**These features and more will be explored more thoroughly in upcoming updates to this documentation.**

Data from most research-based biological observations are aggregated into hexagonal bins to visually summarize data over a large spatial area when the map is zoomed out. This means that data from more than one location or observation may be displayed within a hexagon. The color of the hexagon represents the average value of the select data parameter within that hexagon. For example, if count or abundance is the selected parameter, then the hexagon color will reflect the average count of all individuals or observations within that bin.

To view a summary of all the observation data contain within a hexagon, hover over the hexagon. A window will appear showing the summary of all observations by parameter. Additionally, the time range for which those values were measured will be shown. If you click on the hexagon, a data display window will appear showing a histogram chart summarizing the data. The number of locations or observations aggregated within that hexagon will appear below the parameter name in the data display chart.

To view data for an individual location or observation, zoom in on the map. The hexagons will soften into points that represent the individual sample locations or observation that were aggregated into that hexagon. To view current readings from that location, hover over its point. As shown in the image below, a pop-up window will display some basic information about the station, including its name, latitude and longitude, and a summary of events or observations by parameters (e.g., count by species, percent abundance, number of events, etc ).

To change the data parameters in the map, the filters can be used in the legend on the right side of the map. You can select among the measurements that are available using the caret, or by toggling on/off the checkboxes. The exact filters or measurements available vary by the data layer being shown. 

To further interact with the data in the map, the polygon tool can be used to create summary statistics across spatial areas of interest. Or, the time slider bar can be used to view the various time intervals of data available.

If when zoomed in the hexagons do not soften into points, the individual locations or observations have been intentionally aggregated for data use or confidentiality purposes. 

To view location data, click on the point. As shown in the image below, data from the station will appear in the data display window in the lower left corner of the window. You can use the dropdown menu in the data display window to select different parameters for that location (if available), or you can use the time slider to adjust the time period of the data.

Add More Data Layers to the Map
===============================

There are multiple ways of adding data layers to the map.

From the data catalog:

1. From the `data catalog <http://help.axds.co/portals/DataCatalog.html>`_, browse or search for the layers you want to add.
2. On the results page, use the ``+`` icon next to any of the thumbnails, an indicator showing how many layers are currently queued will show up in the black, upper menu.
3. You can add multiple layers, it's just like a data "shopping cart".
4. Remove layers by selecting the layer indicator in the black, upper menu, and using the ``X`` icons.
5. After you are finished adding data layers, click "Map" in the upper toolbar to view those layers in the map. 

From the data map:

1. From within the interactive map, use the ``Search for data`` bar.
2. From the results popup, use the ``+`` icon next to the layer you want to add to the map.

Learn More About Data Layers 
=============================

Within in the map, there are several ways to learn more about the data layer being displayed.

#. In the map legend to the right, you may see the ``i`` icon next to the data layer title. Click on it to view the metadata page.
#. Click on a point in the map. A data display window will appear showing a chart of the data. In the bottom right of the chart click on ``Source``. You will be directed to the data provider's webpage, if available.
#. For real-time sensor data, click on the station in the map. A data display window will appear showing a chart of the data. 

	* In the bottom left of the chart you can click on ``Station``. Summary information about the station will be shown, including the instrument location, temporal coverage, platform type, station URN or WMO ID, and the source information for the data provider. Interactive data charts for each of the sensors associated with that station will be shown on the right hand side. You can interact with these similar to other Data Charts. Under Sources, you can click on the name of the data provider to discover a list and links to all stations available in the map from that provider. 
	
	* In the bottom left of the chart you can also click on ``Sensor``. Summary information about the sensor will be shown, including parameter information, temporal coverage, and the sensor and parameter source URNs. Under parameter information, you can click the ``Download`` button to download the sensor data. You can also interact with the summary data chart for that sensor.  

Interact with and Customize Data Layers in the Map
===================================================

Once you have found a layer through the data catalog, you can view and interact with the data in a number of ways. As with other interactive maps, you can pan and zoom to adjust the view to your area of interest. Additionally, you can click on a data point of interest to open a chart that summarizes the data. A time slider at the bottom of the map can be used to move back and forth through time for timeseries data. More information about these features is provided below.

From the map, you can search for and add additional data layers to the map. Click on the catalog button in top right to return to the catalog page you most recently visited. You can also search for additional data layers to add to the map using the search bar at the top left corner. When you have selected additional layers, click ``Map`` to return to the map.

Customize Individual Layers
"""""""""""""""""""""""""""

In the map, your selected layers will appear in a legend on the right. The filters in the legend can be used to change the parameters on the map. You can select among the measurements that are available using the caret, or by toggling on/off the checkboxes. The exact filters or measurements available vary by the data layer being shown.

Individual data layers can be toggled on and off using the "Eyeball" icon to the right of the data layer name. To delete the data layer from the map, select the ``X`` icon. 

The order in which data layers appear in the map can be changed. By default, the data layer that appears at the top of the map legend will be displayed forward in the map. To move data layers backward in the map, select the ``Up/Down Arrow`` to the left of the data layer name. 

The data layer legend on the right hand side shows the color scale that is used to represent the unit of measurement. You can change the palette and scale settings by clicking on the color bar. Select among the different color palettes using the drop down menu. The legend scale can be changed by either adjusting the scale slider, or by clicking on the gear icon and entering or advancing the bounds control interval. When the map is zoomed in, the scale and color for that area can be automatically set for the data in view by clicking the ``Autoset for data view`` button.

.. Customize Map View
.. """"""""""""""""""""""""""

Time Slider
"""""""""""

The timer slider bar at the bottom of the map allows you to view temporal data. The time intervals available will vary depending on which data layer you are viewing. The bar in unavailable if there is not any time-enabled data layers loaded. By default, the time slider is set to display the most recent data that is available for that data layer. 

.. tip:: For quick reference, the time range for data being viewed in the map is shown in the right-hand map legend beneath the data layer title.  

The temporal extent for the data layers can be viewed by hovering your mouse over the time slider control. The name of the data layer, the begin and end dates for the data, and a line graph of the temporal range will appear. The temporal information will appear for all time-enabled datasets that are currently loaded in the map.  

There are several ways to interact with temporal data.

#. Click and drag both the time slider control to the right and left to step through the temporal data interactively. Or, click and drag both ends of the time slider control to adjust the time bounds. Then, click and drag the middle of the time slider control bar to step through the temporal data. For finer control of the time slider, pull down on your mouse while dragging. Hover your mouse over the time slider bar to see the temporal range of the data that has been selected.

#. Click on the gear icon to the left of the time slider for finer time controls. The bounding time interval can be entered by clicking the calendar bar. Using the calendar, enter a custom range by selecting both the start and end dates from both calendars. Or, click the preset time ranges from the list on the left to view real time, past 24 hours, past week, past 30 days, etc. of data. Select ``Apply`` to view the selected time range of data in the map.

#. Click on the gear icon to open the time control menu. Select the ``Next Time Stamp`` button to step forward to the next time stamp. For example, if the data view has been set to show data from the prior month, the next time stamp would advance to show data from the current month. Click the ``Prvious Time Stamp`` buttom to step back to the previous time stamp. To show the full start or end time extent click on the ``Step Forward`` or ``Step Backward`` to move the time control to the full start or end extent. 

Depth Filter
""""""""""""

The depth slider bar located in the bottom right of the map allows you to filter data across the water column. The depth intervals available will vary depending on which data layer you are viewing. The bar in unavailable if there is not any depth-enabled data layers loaded. By default, the depth slider is set to display all data across the water column. 

.. tip:: For quick reference, the depth range for data being viewed in the map is shown in the right-hand map legend beneath the time extent.

To filter data by depth: 

#. Click on the depth icon in the bottom right of the map. Click and drag both ends of the depth slider control to adjust the vertical bounds. Note that the depth values represent meters beneath the water surface. Click and drag the middle of the depth slider control bar to step through the vertical data. Hover your mouse over the depth slider bar to see the vertical range of the data that has been selected.

Polygon Tool
""""""""""""

To further interact with data in the map, the polygon tool can be used to create summary statistics across spatial areas of interest. To use the polygon tool:

#. Click on the polygon tool icon. Draw a polygon on the map around the area of interest using mouse clicks at each corner or bend of your shape. When you're finished drawing, double-click to complete the shape.

#. A data display window will open showing a summary chart of the data within the polygon. Beneath the data layer title at the top of the data display window, the number of observations contained within the polygon will be shown.

#. To delete the shape, click the "Trash can" icon next to the polygon tool.

Save and Share Map
===================

The custom map you have created can be shared with others. To share, in the upper toolbar click ``Share``. You will receive a custom url to your saved map state. Copy the link to share with others. 

.. Instance State Saving
.. =====================

***********
Data Charts
***********

The catalog and map offer multiple ways of comparing data within both the mapped interface and within a `data view <http://help.axds.co/portals/DataCatalog.html>`_.

For assistance, please contact us via the red Feedback button |feedback_button_icon| in the top right corner of the toolbar.

Different Chart Types
=====================

This section includes descriptions for the common charts used to display data in the portal. Data charts can be accessed both by clicking a point on a data layer in the map, or by using the custom Data Views interface.  

Categorical Variables
---------------------

* **Bar charts:** compare the size or frequency of different categories. Since the values of a categorical variable are labels for the categories, the distribution of a categorical variable gives either the count or the percent of individuals falling into each category.

Quantitative Variables
----------------------

* **Line charts:** display points connecting the data to show a continuous change over time. In the map, the line chart shows the current values together with historical statistics. The x-axis shows the occurrences and the categories being compared over time and the y-axis represents the scale, which is a set of numbers organized into equal intervals. 

* **Histograms:** show the frequency of distribution for the observations. A histogram is constructed by representing the measurements or observations that are grouped on a horizontal scale, the interval frequencies on a vertical scale, and drawing rectangles whose bases equal the class intervals and whose heights are determined by the corresponding class frequencies. 

.. tip:: In the portal, histogram charts can be created across custom areas of interest using the polygon tool. 

* **Box plots:** are useful for identifying outliers and for comparing distributions. The boxplot is a graph of a five-number summary: the minimum score, first quartile (Q1-the median of the lower half of all scores), the median, third quartile (Q3-the median of the upper half of all scores), and the maximum score. The boxplot consists of a rectangular box, which represents the middle half of all scores (between Q1 and Q3). Approximately one-fourth of the values should fall between the minimum and Q1, and approximately one-fourth should fall between Q3 and the maximum. A line in the box marks the median. Lines called whiskers extend from the box out to the minimum and maximum scores.

* **Dot plots:** consist of data points plotted on a fairly simple scale. Dot plots are suitable for small to moderate sized data sets to highlight clusters and gaps, as well as outliers. When dealing with larger data sets (around 20–30 or more data points) the box plot or histogram may be more efficient, as dot plots may become too cluttered after this point.

* **Curtain plots:** show a visual summary of vertical profiling data. f data is available at depth, the chart will show depth on the y-axis with the values represented by colors.


.. Summary Statistics
.. ==================

Climatology & Anomaly Charts
============================

If there are more than three years of data coverage for stations or gridded data, charts on the portal show statistics from past weather patterns along with the current data. These are not officially climatologies, which typically require 30 years of data, but they can still be useful to quickly compare how the current year fits into the data that's available at a station.

Historical patterns in station observations
-------------------------------------------

1. From the real-time sensor map or historical sensor map, click on any station that has more than three years of data.
2. The default graph will show binned data, with the dark gray line indicating the mean and the gray envelope representing the min and max values within the current year.


Historical patterns in gridded data
-----------------------------------

1. Clicking on any gridded dataset will open a `virtual sensor <http://help.axds.co/portals/DataCatalog.html#download-a-time-series-from-gridded-data>`_.
2. If the dataset has more than three years of data, the default graph will show binned data.
3. The dark gray line indicating the mean and the gray envelope representing the min and max values within the current year.

.. Query & Save Vector Layer for Comparison
.. ========================================

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

**

****************
Download Data
****************

Data may be downloaded through the data catalog, as described in `this <http://help.axds.co/portals/DataCatalog.html#downloading-visualized-data>`_ section.

**********
Data Views
**********

You can save a collection of data from different sensors and visualize them together for comparison and analysis. These collections are called "data views," and they are accessed by clicking on the views button |views_button_icon| near the top right corner of the blue toolbar along the top of the window.

Within the portal there are several premade data views that highlight environmental events or locations of interest. You can access these premade views by following these steps:

#. Click on the views button |views_button_icon|
#. Select the view you'd like to access from the dropdown menu

The view view will open, displaying its data for you to explore. In the example image below, you can see the ``Hurricane Sandy`` view.

|views_view|

.. note::
	If you need assistance creating a particular view, please contact us via the red feedback button |feedback_button_icon| in the top right corner of the blue toolbar.

.. Add Data Layers for Comparison
.. ==============================

.. What Different Data Layers Can Be Compared
.. ==========================================
.. e.g. physical model, biological

.. State Saving/Naming Data Views
.. ==============================

.. Customizing Data View Narratives
.. ================================

.. Share Data View
.. ===============

.. Download Data/Charts
.. ====================

Create a New View
===================

While the premade data views are interesting, the real fun starts when you begin making your own views. To do so, follow these steps and consult the GIF below:

#. If you're not in the map view, click on the map button |portal_button_icon| to get there.
#. Zoom and pan to your desired map view.
#. Click on the point that represents the data you're interested in.
#. Its data will show up in the data display window in the bottom left corner of the window.
#. Within the data display window, click on the |data_display_view_icon|.
#. To add the data to an existing view, choose it from the dropdown menu.
#. To create a new view, click on the add icon |add_view_icon|.

In the GIF below, we've zoomed in on Hawai'i and selected a sensor to view. We then added that sensor's data to a new view called "My view."

|add_new_view_gif|

Customize a View
==================

Once you've created a view, you can access it the same way you'd access a premade view described above. There are several ways you can customize your view. These are described below.

Describe Your View
--------------------

You can add a description to your view, which will appear directly underneath your view's title. Your description can include valid HTML, which allows you to include links and images, as well as some basic text formatting. To add a description, follow these steps:

#. Click on the gear icon |gear_icon| near the top right corner of the window.
#. In the popup window that appears, enter your description in the ``Description`` box.

.. tip::
	To inlcude a link in your description, format it like this: ``<a href="http://www.example.com">This text will show up</a>``

.. note::
	You can also edit the title of your view in the same popup window.

Display Your Data
--------------------

You can adjust the way  data are displayed in the chart on the right-hand side of the window, including but not limited to the following:

#. Scale the Y-axis (data values)
#. Scale the X-axis (time)
#. Re-bin the data
#. Display min/max values and/or mean values

Additionally, you can explore the selected data more in depth in the following ways:

#. Download the data
#. View the station or sensor information page 
#. View information about the data source from the data provider or organization that maintains it

Add Data to a Comparison Chart
---------------------------------

Comparison charts appear below the map and allow you to plot similar data from different sources. To add data from a saved chart to a comparison chart, follow these steps:

#. Click the |data_display_view_icon|.
#. Click the ``Add to compare chart`` box under your view's name.

The new data will appear in the comparison chart in a contrasting color, and the name of the data layer will also be added to a list below the comparison chart.

.. note::
	Comparison charts have the same options for displaying data as saved charts, which are described above under **Displaying Your Data**.

Share a View
==============

Once you've created, customized, and explored your data view, you'll probably want to share it with your friends and colleagues. To get a shareable link, follow these steps:

#. Click on the share button |share_button_icon| near the top right corner of the blue toolbar.
#. Highlight the link that appears in the popup window.
#. Copy that link and paste it anywhere you'd like to share it.

.. note::
	Anyone you share a view with will essentially see their own version of the view you have created and customized. Their edits and additions will not affect your saved view.
