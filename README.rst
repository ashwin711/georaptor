GeoRaptor: Python Geohash Compression Tool
===========================================

Geohash is a geocoding system invented by Gustavo Niemeyer and placed into the public domain. It is a hierarchical spatial data structure which subdivides space into buckets of grid shape, which is one of the many applications of what is known as a Z-order curve, and generally space-filling curves.

Geohash creation for a polygon at a given precision level could result in a huge set of geohashes.

**GeoRaptor** creates the best combination of geohashes across various levels to represent a polygon, by starting from the highest level and iterating till the optimal blend is brewed. Result accuracy remains the same as that of the starting geohash level, but data size reduces considerably for large polygons, thereby improving speed and performance.

Following is a sample of what georaptor does

.. image:: https://raw.github.com/ashwin711/georaptor/master/images/sgp_input.png
   :width: 480
   :height: 320
.. image:: https://raw.github.com/ashwin711/georaptor/master/images/sgp_output.png
   :width: 480
   :height: 320


*Input:* 1096 geohashes at precision 6 for Singapore.

*Output:* 414 geohashes with a mix of precision 5 and 6.

Performance
-----------

**Input sample size:** 18,992,425

**Output:** 220,375

**Total execution time:** 35.8013219833 seconds

Usage
-----

$ georaptor <input> --output <output>


Example
-------

$ georaptor sample.csv

OR

$ georaptor sample.csv --output sample_out.csv


Installation
------------

To install georaptor, simply: ::

    $ pip install georaptor


License:
--------

MIT License. ::

    Copyright (c) 2016, Ashwin Nair <https://www.linkedin.com/in/nairashwin7>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
    deal in the Software without restriction, including without limitation the
    rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
    sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
    IN THE SOFTWARE.
