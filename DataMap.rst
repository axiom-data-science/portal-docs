.. include:: globals.txt

########
Data Map
########

**********************
Displaying Data Layers
**********************

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

***********
Data Charts
***********

*This feature underdevelopment. Check back soon for updates.*

****************
Downloading Data
****************

Data may be downloaded through the data catalog, as described in `this <http://help.axds.co/portals/DataCatalog.html#downloading-visualized-data>`_ section.

**********
Data Views
**********

*This feature underdevelopment. Check back soon for updates.*


