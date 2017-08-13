=========
defogging
=========


.. image:: https://img.shields.io/pypi/v/defogging.svg
        :target: https://pypi.python.org/pypi/defogging/

.. image:: https://img.shields.io/travis/scloudyy/Defogging.svg
        :target: https://travis-ci.org/scloudyy/Defogging

Implement a robust and efficient defogging method with Python


Features
--------

* Defogging a single foggy image

install
-------

Use ``pip`` to install: ::

    $ pip install defogging

Or you can install from source: ::

    $ git clone git@github.com:scloudyy/Defogging.git
    $ cd Defogging
    $ python setup.py build
    $ pip install .

Usage
-----

Use ``defogging`` through command line: ::

   $ defogging your_img.bmp

the result will be saved as ``your_img_defogging.bmp``

And you can also use ``defogging`` in your own code:

.. code-block:: python

   from defogging import Defog

   in_name = "foggy.bmp"
   out_name = "defogged.bmp"

   df = Defog()
   df.read_img(in_name)
   df.defog()
   df.save_img(out_name)

you can directly input a foggy object in the form of ``numpy.array`` :

.. code-block:: python

   df.read_array(your_array, range)

where ``range`` indicates the value range of your array.The range has two options:
the first is ``1``, which means the value range of your array is [0,1],
and the second is ``255``, which means the value range is [0,255]

If you want to process the defogged object further, you can also get defogged array:

.. code-block:: python

   dst = df.get_array(range)

also, ``range`` indicates the value range of returned array, either ``1`` or ``255``.
If you choose ``1``, the range will lie in [0,1], and the type of it is ``float``.
Or if you choose ``255``, the range will be [0,255], and the type will be ``uint8``.

