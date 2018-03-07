############
Introduction
############

The |title| is a data exploration tool with a customized public web interface that allows scientists, managers, and the general public to discover and access public data from many sources. The |title| has two components:

#. a data catalog, and
#. a map interface.

The catalog provides a way to explore available datasets using text searches and filters, as well as the ability to download datasets of interest. Some datasets in the catalog can be visualized automatically through the map interface, which provides a rich suite of tools for creating charts, comparing data, and visualizing datasets in context.

*******
Catalog
*******

The catalog provides search access for all datasets within the |title|. The catalog can be used to discover, browse, and download data files. Additionally, the catalog can be used to add visualizable data layers to the data map. The catalog contains several observational data types:

* *Real-time data* are ingested, served, and displayed by the portal at the same frequency the data are collected (and sometimes reported) by the originator with little to no delay. Examples of real-time assets include weather stations, oceanographic buoys, and webcams.

* *Near real-time data* are ingested by the |title| at the same frequency that the data are made available; however, there is some delay (hours to days) between data collection and when the data provider makes it available. Examples of near real-time assets include satellite images and derived satellite products.

* *Historical data* are data that are one month old or older. Historical data are ingested from the associated Research Workspace or from national archives upon stakeholder request. Examples include species abundance surveys and similar research efforts.

The data catalog is built around a familiar search interface, with several important elements arranged around the screen:

* Filter by location map in the upper left
* Groups of common tags to help filter the catalog quickly in the column on the left
* Text search bar across the top
* A list of datasets that match the desire criteria in the main column

|catalog_initial_view|

***
Map
***

The data map interface provides interactive data exploration, mapping, and charting for visualizable layers available in the catalog. All real-time and near real-time data within the |title| are accessible as interactive visualizations in the map view (as indicated with a map preview image in the catalog). Historical data are also accessible as interactive visualizations in the map, with the exception of datasets that may be published directly to the catalog from the Research Workspace.

The map is highly customizable (``Settings`` and ``Legend``), enabling deep exploration of the data. Advanced charting features allow users to view and summarize multiple datasets, and to create custom `Data Views <http://help.axds.co/portals/DataMap.html#data-views>`_ to compare data sources, bin by time, or plot climatologies and anomalies of timeseries datasets. Users can create and share custom compilations of biological, sensor, and model outputs to spotlight environmental events or geographic locations.

The data map is built around a familiar interactive map interface, with several important elements arranged around the screen:

* Blue toolbar across the top
* Legend displayed on the right
* Grey time slider toolbar along the bottom
* Data display window in the bottom left corner
* Zoom navigation tools in the top left corner

|map_initial_view|


