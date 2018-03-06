#######
OPeNDAP
#######

OPeNDAP is a simpler THREDDS protocol that can provide ASCII (human-readable) or binary files. It loads very quickly, but doesn't do any interpretation for you at all and you will need to be able to calculate or surmise the indices you need to subset the data. For example, if there are 20,000 dates listed in the file, it will give you the option of selecting 0-20,000, but it won't tell you what those dates are. Therefore, OPeNDAP is best in cases where you are already familiar with the dataset's bounds and speed is more important, or in cases where you just want to download the whole thing and don't care much about subsetting.

#. Select ``THREDDS OPeNDAP`` under the ``Download`` button to start the service.
#. Your browser should get a response from the server almost instantaneously.
#. The response page will have a list of available variables — check the variables you want to download.
#. If you want, subset each variable by indices. The numbers are minimum:stride:maximum (the default  stride is 1, which downloads all time slices; a stride of 2 will download every second time slice, etc.). Add lat/lon variables if needed in your output, but in most cases this is unnecessary.
#. Scroll back up to the top of the page and select Get ASCII or Get Binary. ASCII is the most popular from this interface.

.. note::
	All THREDDS servers have a bandwidth limit, and it will not allow you to download more than the cap in one go. So you won't be able to download 1 Tb of data with a single request. If you need a lot of data, you will need to break up your requests to download the dataset incrementally (e.g., try downloading half a variable first, then the second half, or one variable at a time, etc.).

