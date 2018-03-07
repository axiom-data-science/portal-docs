################
NetCDF Resources
################

`NetCDF <https://www.unidata.ucar.edu/software/netcdf/>`_ is the name of a file format as well as a grouping of software libraries that describe that format. The files have the ability to contain multidimensional data in a wide variety of data types, and they are highly optimized for file I/O. This makes them excellent at storing extremely large datasets because they can be quickly and easily sliced without putting the entire dataset into RAM.

In addition, NetCDF files can contain metadata attributes that describe any time components, dimensions, units, history, etc. Because of this, NetCDF is often called a "self-describing" data format and they are excellent for holding archived data, and they are the primary format preferred by the National Centers for Environmental Information (NCEI, formerly NODC).

NetCDF libraries are available for every common scientific programming language including Python, R, Matlab, ODV, Java, and more. Unidata maintains `a list of free software for manipulating or displaying NetCDF data <https://www.unidata.ucar.edu/software/>`_. A good, simple program to start exploring NetCDF data is Unidata's ncdump, which runs on the command line and can quickly output netCDF data to your screen as ASCII. Unidata's `Integrated Data Viewer <https://www.unidata.ucar.edu/software/idv/>`_ or NASA's `Panoply <https://www.giss.nasa.gov/tools/panoply/>`_ are free, relatively easy programs to use that will display gridded data, though they are not as straightforward to use as a scientific programming language.

