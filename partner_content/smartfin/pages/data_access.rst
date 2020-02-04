###########
Data Access
###########

Fins transmit binary data when the fin encounters a cellular signal. A list of fins, sessions per fin, and count of 'pass' observations (wet, within temperature bounds, etc.) is available via a RESTful API:

* https://smartfin.axds.co/data_api/fins
* https://smartfin.axds.co/data_api/sessions

To filter or sort results, refer to the API documentation at https://smartfin.axds.co/data_api.

To view observations for a given session, first identify the sessions `uuid` from the list of sessions. For example:

.. code-block:: JSON

      {
         device_id: "3a0025001047373333353132",
         fin_session_id: "Sfin-3a0025001047373333353132-191220-004805",
         start_time: "2019-12-20T00:48:05",
         uuid: "8620e391-413e-5840-991a-8ee6f21c6f66",
         qc_pass: 168
      }

Use this `uuid` in the a url request for data from the Smartfin GeoServer instance::

 http://servomatic9000.axiomalaska.com/geoserver/moving_platforms/ows?service=WFS
 &version=1.0.0
 &request=GetFeature
 &outputFormat=application%2Fjson
 &typeName=moving_platforms:uuid

In this example, replace `uuid` with `8620e391-413e-5840-991a-8ee6f21c6f66`, as follows:

http://servomatic9000.axiomalaska.com/geoserver/moving_platforms/ows?service=WFS&version=1.0.0&request=GetFeature&outputFormat=application%2Fjson&typeName=moving_platforms:8620e391-413e-5840-991a-8ee6f21c6f66

Other available data formats include:

* `&outputFormat=csv`
* `&outputFormat=SHAPE-ZIP`

Refer to the `GeoServer documentation <https://docs.geoserver.org/latest/en/user/services/wfs/outputformats.html>`_ for more information.

