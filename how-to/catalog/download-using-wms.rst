.. _download-using-wms-how-to:

##################
Download Using WMS
##################

#. Select “WMS (Web Mapping Service)” under the Download button to start the service.
#. The returned image will be projected according to the parameters set in the URL. For example:

.. parsed-literal::
	`http://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=AQWRFSFC/PSFC&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20983724.014532067,8598321.56555337,-13914936.349159194,13370447.645073326&WIDTH=500&HEIGHT=338&COLORSCALERANGE=846.5,1128 <http://data.axds.co/ncWMS/wms?SERVICE=WMS&REQUEST=GetMap&LAYERS=AQWRFSFC/PSFC&VERSION=1.1.1&FORMAT=image/png&STYLES=boxfill/rainbow&SRS=EPSG:3857&BBOX=-20983724.014532067,8598321.56555337,-13914936.349159194,13370447.645073326&WIDTH=500&HEIGHT=338&COLORSCALERANGE=846.5,1128>`_

#. Modifying the parameters (e.g., changing the WIDTH, COLORSCALERANGE values, or the projection and reloading the page will redraw the image for your mapping service.

For more information, please see the :ref:`gridded-data-overview` section.
