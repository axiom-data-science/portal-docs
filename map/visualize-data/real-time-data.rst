##############
Real-Time Data
##############

Real-time data are ingested, served, and displayed in the |title| at the same frequency the data are collected (and sometimes reported) by the originator with little to no delay. Examples of real-time assets include weather stations, oceanographic buoys, and webcams. For the purposes of this documentation, it's helpful to understand how the following real-time data terms are defined:

.. csv-table::
	:header: "Term", "Definition"
	:widths: 15, 50

	"**Hexagonal bin**", "A group of stations that are aggregated into a hexagon for visual summary."
	"**Station**", "A device that collects data related to the weather and environment using many different sensors (e.g. weather station)."
	"**Sensor**", "An individual measurement device affixed or associated with a station (e.g. thermometer, barometer)."
	"**Parameter**", "The type of value measured by the sensor (e.g. temperature, pressure)."


Real-time data from observation stations are aggregated into hexagonal bins to visually summarize data over a large spatial area when the map is zoomed out. This means that data from more than one station may be displayed within a hexagon. The color of the hexagon represents the average value of the selected sensor parameter within that hexagon. For example, if air temperature is the selected sensor type, then the hexagon color will reflect the average temperature for all stations within that bin.

To view a summary of the station data contained within a hexagon, hover your mouse over the hexagon. The number of stations aggregated within that hexagon will be displayed as "n stations." The average value for the selected sensor type will be also be shown, followed by the time range for which that value was measured. If there are not more than one station aggregated within a hexagon, the hover-over view will display the value for the selected parameter, followed by a list of the other sensor types associated with that station and the range of associated data. By default, only five of the sensors are shown in the hover window. More sensors are indicated by the "n more sensors" in the lower left of the window.

To view data for an individual station, zoom in on the map. The hexagons will soften into points that represent the individual stations that were aggregated into that hexagon. To view current readings from that station, hover over its point. As shown in the image below, a pop-up window will display some basic information about the station, including its name, data source affilitation(s), latitude and longitude, current readings, and available sensor parameters (e.g., air temperature, water level, and water temperature as in the example below).

|sensor_hover|

To view station data, click on the point. As shown in the image below, data from the station will appear in the data display window in the lower left corner of the window. You can use the dropdown menu in the data display window to select data from different sensors, and you can use the `time slider <http://help.axds.co/portals/DataMap.html#interact-with-and-customize-data-layers-in-the-map>`_ to adjust the time period of the data.

|sensor_select|



