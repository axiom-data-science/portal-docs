.. _netcdf-subset-how-to:

############################
Download Using NetCDF Subset
############################

#. Select "THREDDS NetCDF Subset" under the ``Download`` button to start the service.
#. Your browser will wait for a response from the server, which builds a library of all the files and metadata in the complete dataset so it can display up-to-date information.
#. The response page will have a list of available variables — check the variables you want to download.
#. Subset the dataset by latitude and longitude, and time range with a stride (the default  stride is 1, which downloads all time slices; a stride of 2 will download every second time slice, etc.) Add lat/lon variables if needed in your output, but in most cases this is unnecessary.
#. The output format will be a single NetCDF file that contains the complete dataset.

For more information about NetCDF Subset, please see the :ref:`gridded-data-overview` section.
