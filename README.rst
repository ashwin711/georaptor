.. image:: http://donatecoins.org/btc/1HeMeMU2qUFDRZpRQMJ2v27Dw3h3gShJ5b.svg
   :target: http://donatecoins.org/btc/1HeMeMU2qUFDRZpRQMJ2v27Dw3h3gShJ5b

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

$ georaptor <input> --output <output> --minlevel <minlevel> --maxlevel <maxlevel>


Example
-------

$ georaptor sample.csv

OR

$ georaptor sample.csv --output sample_out.csv --minlevel 3 --maxlevel 4


Installation
------------

To install georaptor, simply: ::

    $ pip install georaptor


License:
--------


Licensed under the Apache License, Version 2.0. ::

    Copyright 2017 Ashwin Nair <https://www.linkedin.com/in/nairashwin7>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.