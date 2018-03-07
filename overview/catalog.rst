#######
Catalog
#######

The catalog provides search access for all datasets within the |title|. The catalog can be used to discover, browse, and download data files. Additionally, the catalog can be used to add visualizable data layers to the map. The catalog contains several observational data types:

* *Real-time data* are ingested, served, and displayed by the portal at the same frequency the data are collected (and sometimes reported) by the originator with little to no delay. Examples of real-time assets include weather stations, oceanographic buoys, and webcams.

* *Near real-time data* are ingested by the portal at the same frequency that the data are made available; however, there is some delay (hours to days) between data collection and when the data provider makes it available. Examples of near real-time assets include satellite images and derived satellite products.

* *Historical data* are data that are one month old or older. Historical data are ingested from the associated `Research Workspace <http://help.axds.co/portals/DataCatalog.html#data-files-from-the-research-workspace>`_ or from national archives upon stakeholder request. Examples include species abundance surveys and similar research efforts.

*********************
Searching the Catalog
*********************

From the |title| home page, click on ``Explore Data Layers`` to navigate to the catalog.

Within the catalog, you will find a listing of all the data layers accessible through the |title|. By default, the data layers are shown in alphabetical order. There are several ways the data layers can be browsed or searched.

* Click a category tag in the left sidebar. The data layers that are associated with the tag will be displayed. More than one category tag can be selected at the same time.

* Enter a search term. Just type the data you are interested in finding into the search box in the upper left toolbar. As you type, you may see matching terms (e.g. ``Hints``) and actual data layers (e.g. ``Results``) appear below the toolbar's search box. Click on the ``Hints`` or ``Results`` of interest and the search results will appear in the data catalog.

* Filter the result types in the left sidebar. All data layers in the catalog are categorized as ``Map layers`` (e.g. static GIS layers), ``Projects`` (e.g. research project data files displayed from the Research Workspace), or ``Sensor stations`` (e.g. real-time sensor observations). Select the checkboxes to display or narrow the data layers by these ``Results`` types.

* Do an advanced search by space, time, or method. Click on ``Advanced search options`` in the left sidebar.

	* Using the ``Spatial filter`` option, you can click on the rectangle icon to draw a bounding box on the map, or you can type the latitude/longitude coordinates. The data layers occuring in that spatial area will appear in the data catalog.

	* Using the ``Filter time`` option, you can adjust the time slider or type the start/end date range. The data layers occuring during that temporal period will appear in the data catalog.

	* Using the ``Access method`` option, you can select data service method from which data layers can be downloaded from the catalog.

*********
Data DOIs
*********

*This feature is under development. Check back soon for updates.*

**************
Layer Metadata
**************

To learn more about the data layer, click on the title in the catalog. You will be taken to a metadata page that shows the URL to the source data, the data description, and any usage notes. There will also be an inset map where you can explore the dataset as a single layer. If the data layers is a timeseries dataset, you will be able to move back and forth through time using the time slider at the bottom of the inset map.

Some data layers in the catalog have more than one variable associated with them. In these cases, a thumbnail image will appear below the data layer in the catalog and in the metadata view. To learn more about each of the data layer variables, click on the title below the thumbnail image. You will be taken to a metadata page that shows the URL to the source data, the data description, and any usage notes. The variable will also appear in the inset map where you can explore the data as a single layer.

****************
NetCDF Resources
****************

`NetCDF <https://www.unidata.ucar.edu/software/netcdf/>`_ is the name of a file format as well as a grouping of software libraries that describe that format. The files have the ability to contain multidimensional data in a wide variety of data types, and they are highly optimized for file I/O. This makes them excellent at storing extremely large datasets because they can be quickly and easily sliced without putting the entire dataset into RAM.

In addition, NetCDF files can contain metadata attributes that describe any time components, dimensions, units, history, etc. Because of this, NetCDF is often called a "self-describing" data format and they are excellent for holding archived data, and they are the primary format preferred by the National Centers for Environmental Information (NCEI, formerly NODC).

NetCDF libraries are available for every common scientific programming language including Python, R, Matlab, ODV, Java, and more. Unidata maintains `a list of free software for manipulating or displaying NetCDF data <https://www.unidata.ucar.edu/software/>`_. A good, simple program to start exploring NetCDF data is Unidata's ncdump, which runs on the command line and can quickly output netCDF data to your screen as ASCII. Unidata's `Integrated Data Viewer <https://www.unidata.ucar.edu/software/idv/>`_ or NASA's `Panoply <https://www.giss.nasa.gov/tools/panoply/>`_ are free, relatively easy programs to use that will display gridded data, though they are not as straightforward to use as a scientific programming language.

*************
NetCDF Subset
*************

The NetCDF Subset protocol looks through all the datasets NetCDF files stored on our server, and provides an human-readable or machine-readable interface to subset the data by time, geography, or variable.

#. Select "THREDDS NetCDF Subset" under the ``Download`` button to start the service.
#. Your browser will wait for a response from the server, which builds a library of all the files and metadata in the complete dataset so it can display up-to-date information.
#. The response page will have a list of available variables — check the variables you want to download.
#. Subset the dataset by latitude and longitude, and time range with a stride (the default  stride is 1, which downloads all time slices; a stride of 2 will download every second time slice, etc.) Add lat/lon variables if needed in your output, but in most cases this is unnecessary.
#. The output format will be a single NetCDF file that contains the complete dataset.

.. tip::
	When you initially request a dataset via NetCDF Subset, the server may take a long time to respond if dataset is large (i.e., thousands of files). Be patient, it's not broken! If your web browser times out (e.g., after 10 minutes of waiting), you can try reloading or just giving it a few more minutes and then reload. This won't restart the server process, and once it's indexed all the files things will go pretty fast.

.. note::
	All THREDDS servers have a bandwidth limit, and it will not allow you to download more than the cap in one go. So you won't be able to download 1 Tb of data with a single request. If you need a lot of data, you will need to break up your requests to download the dataset incrementally (e.g., one month at a time; one variable at a time, etc.). If you're grabbing a lot of data programmatically, sometimes it's easiest to grab just one time slice at a time using a loop.

*******
OPeNDAP
*******

OPeNDAP is a simpler THREDDS protocol that can provide ASCII (human-readable) or binary files. It loads very quickly, but doesn't do any interpretation for you at all and you will need to be able to calculate or surmise the indices you need to subset the data. For example, if there are 20,000 dates listed in the file, it will give you the option of selecting 0-20,000, but it won't tell you what those dates are. Therefore, OPeNDAP is best in cases where you are already familiar with the dataset's bounds and speed is more important, or in cases where you just want to download the whole thing and don't care much about subsetting.

#. Select ``THREDDS OPeNDAP`` under the ``Download`` button to start the service.
#. Your browser should get a response from the server almost instantaneously.
#. The response page will have a list of available variables — check the variables you want to download.
#. If you want, subset each variable by indices. The numbers are minimum:stride:maximum (the default  stride is 1, which downloads all time slices; a stride of 2 will download every second time slice, etc.). Add lat/lon variables if needed in your output, but in most cases this is unnecessary.
#. Scroll back up to the top of the page and select Get ASCII or Get Binary. ASCII is the most popular from this interface.

.. note::
	All THREDDS servers have a bandwidth limit, and it will not allow you to download more than the cap in one go. So you won't be able to download 1 Tb of data with a single request. If you need a lot of data, you will need to break up your requests to download the dataset incrementally (e.g., try downloading half a variable first, then the second half, or one variable at a time, etc.).

*******
THREDDS
*******

Thematic Realtime Environmental Distributed Data Services (THREDDS) is a set of services provided by `Unidata <http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html>`_ that allows for machine and human access to raster data stored in NetCDF formats. THREDDS provides spatial, vertical, and temporal subsetting, as well as the ability to select individual dimension or data variables to reduce file transfer sizes. The most commonly used THREDDS services for AOOS users are NetCDF Subset, and Open-source Project for a Network Data Access Protocol (OpenDAP).

***
WMS
***

Web mapping services (WMS) are used to provide machine access to images used by remote mapping programs (e.g., tiling services). Accessing programs use GetCapabilities requests to ask for image data in whatever format they require, which allows them to gather image tiles over specific areas with the projections, styles, scales and formats (PNG, JPG, etc.) that fits their needs.

#. Select "WMS (Web Mapping Service)" under the ``Download`` button to start the service.
#. The returned image will be projected according to the parameters set in the URL. For example:

.. parsed-literal::
	`http://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=AQWRFSFC/PSFC&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20983724.014532067,8598321.56555337,-13914936.349159194,13370447.645073326&WIDTH=500&HEIGHT=338&COLORSCALERANGE=846.5,1128 <http://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=AQWRFSFC/PSFC&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20983724.014532067,8598321.56555337,-13914936.349159194,13370447.645073326&WIDTH=500&HEIGHT=338&COLORSCALERANGE=846.5,1128>`_

3. Modifying the parameters (e.g., changing the ``WIDTH``, ``COLORSCALERANGE`` values, or the projection and reloading the page will redraw the image for your mapping service.

***************
Historical Data
***************

Historical data are data that are one month old or older. Historical data available through the portal were sometimes collected in real-time and subsequently archived; other historical data are ingested from local or national archives upon stakeholder request.


