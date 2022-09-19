PyWaveSurfer
============


|Build Status| |PyPI version| |Updates| |Cover|


PyWaveSurfer is a Python package for reading data acquired using WaveSurfer.


See the `official site <http://wavesurfer.janelia.org/>`_ for more information about WaveSurfer.


Example usage
-------------

.. code-block:: python

    from pywavesurfer import ws
    # to get analog channels scaled in float64 :
    data_as_dict = ws.loadDataFile(filename='path/to/file.h5', format_string='double' )
    # to get analog channels scaled in float32:
    data_as_dict = ws.loadDataFile(filename='path/to/file.h5', format_string='single' )
    # to get the raw analog channels in int16:
    data_as_dict = ws.loadDataFile(filename='path/to/file.h5', format_string='raw' )


Description of the content can be found in the documentation
`here <http://wavesurfer.janelia.org/manual/index.html#reading-acquired-data>`_.

Copyright
---------

Except where noted, all code, documentation, images, and anything else
in PyWaveSurfer is copyright 2017 by the Howard Hughes Medical 
Institute.


License
-------

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

* Neither the name of HHMI nor the names of its contributors may be
  used to endorse or promote products derived from this software
  without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Authors
-------

PyWaveSurfer was developed at the HHMI Janelia Research Campus, by 
Adam L. Taylor and Boaz Mohar.


Maintainers
-----------

Adam L. Taylor 
Scientific Computing
HHMI Janelia Research Campus


Version History
---------------

0.0.1    Oct 11, 2017    Initial release.

0.0.2    Oct 14, 2017    Added a check for WS version.

0.0.3    Aug 23, 2018    Added test for WS 0.97 data files, changed an exception to a warning, updated dependencies.

0.0.5    Oct 22, 2020  

0.0.6    Oct 14, 2021 Updated dependencies, drop python 3.6, added 3.9. Moved CI/CD to Github Actions.

0.0.7    Oct 14, 2021 Updated dependencies, added context manager to h5py open.

0.0.8    Sep 19, 2022 Updated dependencies, drop python 3.7, added 3.10.

.. |Updates| image:: https://pyup.io/repos/github/JaneliaSciComp/PyWaveSurfer/shield.svg
   :target: https://pyup.io/repos/github/JaneliaSciComp/PyWaveSurfer/
.. |Build Status| image:: https://github.com/JaneliaSciComp/PyWaveSurfer/actions/workflows/main.yml/badge.svg
   :target: https://github.com/JaneliaSciComp/PyWaveSurfer/actions/workflows/main.yml
.. |PyPI version| image:: https://badge.fury.io/py/pywavesurfer.svg
   :target: https://badge.fury.io/py/pywavesurfer
.. |Cover| image:: https://coveralls.io/repos/github/JaneliaSciComp/PyWaveSurfer/badge.svg?branch=master
   :target: https://coveralls.io/github/JaneliaSciComp/PyWaveSurfer?branch=master
