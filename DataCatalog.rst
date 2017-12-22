.. include:: globals.txt

############
Data Catalog
############

*This feature is under development. Check back soon for updates.*

**************
Search Catalog
**************

*This feature is under development. Check back soon for updates.*

****
Tags
****

*This feature is under development. Check back soon for updates.*

**************
Search Filters
**************

*This feature is under development. Check back soon for updates.*

********************
About the Data Layer
********************

*This feature is under development. Check back soon for updates.*

********
Metadata
********

*This feature is under development. Check back soon for updates.*

*********
Data DOIs
*********

*This feature is under development. Check back soon for updates.*

***************************
Downloading Visualized Data
***************************

Gridded Data
============

Thematic Realtime Environmental Distributed Data Services (THREDDS)
-------------------------------------------------------------------

Thematic Realtime Environmental Distributed Data Services (THREDDS) is a set of services provided by `Unidata <http://www.unidata.ucar.edu/software/thredds/current/tds/TDS.html>`_ that allows for machine and human access to raster data stored in NetCDF formats. THREDDS provides spatial, vertical, and temporal subsetting, as well as the ability to select individual dimension or data variables to reduce file transfer sizes. The most commonly used THREDDS services for AOOS users are NetCDF Subset, and Open-source Project for a Network Data Access Protocol (OpenDAP).

NetCDF Subset
"""""""""""""

The NetCDF Subset protocol looks through all the datasets NetCDF files stored on our server, and provides an human-readable or machine-readable interface to subset the data by time, geography, or variable.

#. Select "THREDDS NetCDF Subset" under the "Download" button to start the service.
#. Your browser will wait for a response from the server, which builds a library of all the files and metadata in the complete dataset so it can display up-to-date information.
#. The response page will have a list of available variables — check the variables you want to download.
#. Subset the dataset by latitude and longitude, and time range with a stride (the default  stride is 1, which downloads all time slices; a stride of 2 will download every second time slice, etc.) Add lat/lon variables if needed in your output, but in most cases this is unnecessary.
#. The output format will be a single NetCDF file that contains the complete dataset.

.. tip::
	When you initially request a dataset via NetCDF Subset, the server may take a long time to respond if dataset is large (i.e., thousands of files). Be patient, it's not broken! If your web browser times out (e.g., after 10 minutes of waiting), you can try reloading or just giving it a few more minutes and then reloading. This won't restart the server process, and once it's indexed all the files things will go pretty fast.

.. note::
	All THREDDS servers have a bandwidth limit, and it will not allow you to download more than the cap in one go. So you won't be able to download 1 Tb of data with a single request. If you need a lot of data, you will need to break up your requests to download the dataset incrementally (e.g., one month at a time; one variable at a time, etc.). If you're grabbing a lot of data programmatically, sometimes it's easiest to grab just one time slice at a time using a loop.

Open-source Project for a Network Data Access Protocol (OPeNDAP)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

OPeNDAP is a simpler THREDDS protocol that can provide ASCII (human-readable) or binary files. It loads very quickly, but doesn't do any interpretation for you at all and you will need to be able to calculate or surmise the indices you need to subset the data. For example, if there are 20,000 dates listed in the file, it will give you the option of selecting 0-20,000, but it won't tell you what those dates are. Therefore, OPeNDAP is best in cases where you are already familiar with the dataset's bounds and speed is more important, or in cases where you just want to download the whole thing and don't care much about subsetting.

#. Select "THREDDS OPeNDAP" under the "Download" button to start the service.
#. Your browser should get a response from the server almost instantaneously.
#. The response page will have a list of available variables — check the variables you want to download.
#. If you want, subset each variable by indices. The numbers are minimum:stride:maximum (the default  stride is 1, which downloads all time slices; a stride of 2 will download every second time slice, etc.). Add lat/lon variables if needed in your output, but in most cases this is unnecessary.
#. Scroll back up to the top of the page and select Get ASCII or Get Binary. ASCII is the most popular from this interface.

.. note::
	All THREDDS servers have a bandwidth limit, and it will not allow you to download more than the cap in one go. So you won't be able to download 1 Tb of data with a single request. If you need a lot of data, you will need to break up your requests to download the dataset incrementally (e.g., try downloading half a variable first, then the second half, or one variable at a time, etc.).

Web Mapping Services (WMS)
--------------------------

Web mapping services (WMS) are used to provide machine access to images used by remote mapping programs (e.g., tiling services). Accessing programs use GetCapabilities requests to ask for image data in whatever format they require, which allows them to gather image tiles over specific areas with the projections, styles, scales and formats (PNG, JPG, etc.) that fits their needs.

#. Select "WMS (Web Mapping Service)" under the "Download" button to start the service.
#. The returned image will be projected according to the parameters set in the URL. For example:

.. parsed-literal::
	`http://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=AQWRFSFC/PSFC&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20983724.014532067,8598321.56555337,-13914936.349159194,13370447.645073326&WIDTH=500&HEIGHT=338&COLORSCALERANGE=846.5,1128 <http://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=AQWRFSFC/PSFC&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20983724.014532067,8598321.56555337,-13914936.349159194,13370447.645073326&WIDTH=500&HEIGHT=338&COLORSCALERANGE=846.5,1128>`_

3. Modifying the parameters (e.g., changing the ``WIDTH``, ``COLORSCALERANGE`` values, or the projection) and reloading the page will redraw the image for your mapping service.

Environmental Research Division Data Access Program (ERDDAP)
------------------------------------------------------------

The Environmental Research Division Data Access Program (ERDDAP) is a NOAA-sponsored common data server that provides access to gridded and device (e.g., weather sensor) data. AOOS hosts an ERDDAP server that provides access to gridded data in a multitude of formats including CSV, TSV, htmlTable, json, .mat, and more).

#. Go to http://erddap.aoos.org
#. Search for a topic (e.g., in the examples above we searched for "CBHAR")
#. Select the links listed under GrId DAP
#. Select the range in each dimension (e.g., start time, stride, end time), and uncheck all unneeded variables.
#. Select the output file type desired and submit the request to the server. When the data is bundled, it will download automatically.

Downloading a Time Series
-------------------------

The portal provides access to time-series extraction of gridded data, also known as a "Virtual Sensor."

#. Click on an area of interest in the map.
#. A symbol at the location will appear, and a window will launch requesting all the data at that latitude and longitude throughout the dataset.
#. Select ``Download`` to receive a zip file containing data.csv and metadata.txt for that station and sensor.

Station Data
============

Historical Sensor Catalog
-------------------------

Historical sensor catalogs aggregate and show all relevant station data. Data can be downloaded by selecting an individual station and then choosing ``Download``.

#. Visit the the historical sensor catalog's website.
#. Use the station filters to show stations by parameter, source, or platform.
#. Use the map to zoom to an area of interest, select an individual station, and the data for that station and sensor.

ERDDAP Sensor Catalog
---------------------

ERDDAP is a NOAA-sponsored common data server that provides access to gridded and device (e.g., weather sensor) data. The portal hosts an ERDDAP server that provides access to gridded data in a multitude of formats including CSV, TSV, htmlTable, json, .mat, and more).

#. Go to the ERDDAP sensor catalog's website.
#. Search for a station name (e.g., "Wiseman").
#. Select the data link under Table DAP.
#. Select the range in each dimension (e.g., start time, stride, end time) and what variables you want to download.
#. Select the output file type desired and submit the request to the server. When the data are bundled, they will download automatically.

Queried/Parsed Data
===================

This section of our documentation is still under development. For assistance, please contact us at noaa.ioos.webmaster@noaa.gov.

NetCDF Resources
================

`NetCDF <https://www.unidata.ucar.edu/software/netcdf/>`_ is the name of a file format as well as a grouping of software libraries that describe that format. The files have the ability to contain multidimensional data in a wide variety of data types, and they are highly optimized for file I/O. This makes them excellent at storing extremely large datasets because they can be quickly and easily sliced without putting the entire dataset into RAM.

In addition, NetCDF files can contain metadata attributes that describe any time components, dimensions, units, history, etc. Because of this, NetCDF is often called a "self-describing" data format and they are excellent for holding archived data, and they are the primary format preferred by the National Centers for Environmental Information (NCEI, formerly NODC).

NetCDF libraries are available for every common scientific programming language including Python, R, Matlab, ODV, Java, and more. Unidata maintains a list of free software for manipulating or displaying NetCDF data. A good, simple program to start exploring NetCDF data is Unidata's ncdump, which runs on the command line and can quickly output netCDF data to your screen as ASCII. Panoply, hosted by NASA, is a free, relatively easy way to display gridded data, though it's not as straightforward to use as a scientific programming language.

*******************************
Downloading Non-visualized Data
*******************************
*This feature is under development. Check back soon for updates.*
