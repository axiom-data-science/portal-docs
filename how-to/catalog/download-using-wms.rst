.. _download-using-wms-how-to:

##################
Download Using WMS
##################

|catalog_download_data_wms_gif|

#. Click on the Download button |catalog_data_download_icon|.
#. Select ``WMS (Web Mapping Service)``.
#. The service will open in a new browser tab and the results will display.

The returned image will be projected according to the parameters set in the URL. For example:

	https://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=MUR2/analysed_sst&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20036395.759359274,-7.081154551613622e-10,20037508.342789244,19971868.880408563&WIDTH=500&HEIGHT=249&COLORSCALERANGE=271.15,311.15

Modifying the parameters (e.g., changing the WIDTH, COLORSCALERANGE values, or the projection and reloading the page will redraw the image for your mapping service.

For more information, please see the :ref:`Gridded Data <gridded-data-overview>` section.
