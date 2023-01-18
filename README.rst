python GetIDs
=============

This is a Python port of the GetIDs engine that calculates the date of
creation for Telegram accounts using known creation dates.

The original repository can be found
`here <https://github.com/wjclub/telegram-bot-getids>`__.

Installation
------------

.. code:: bash

   $ pip install -U getids

Usage
-----

You can use the package in two ways:

Interactively
~~~~~~~~~~~~~

.. code:: bash

   $ python -m getids 1234567 200097591 2000000000

Expected output:
^^^^^^^^^^^^^^^^

.. code:: text

   1234567: older_than 10/2013
   200097591: aprox 5/2016
   2000000000: newer_than 10/2021

From python code
~~~~~~~~~~~~~~~~

.. code:: python

   >>> from getids import get_date_as_string, get_date_as_datetime
   >>>
   >>> get_date_as_string(1234567)
   ('older_than', '10/2013')
   >>> get_date_as_string(200097591)
   ('aprox', '5/2016')
   >>> get_date_as_string(2000000000)
   ('newer_than', '10/2021')
   >>>
   >>> get_date_as_datetime(1234567)
   (-1, datetime.datetime(2013, 10, 31, 22, 0))
   >>> get_date_as_datetime(200097591)
   (0, datetime.datetime(2016, 5, 6, 17, 25, 6))
   >>> get_date_as_datetime(2000000000)
   (1, datetime.datetime(2021, 10, 11, 21, 53, 20))

Note: The ``get_date_as_datetime`` function is seen as a low-level
function, since it returns a specific date, which is not wanted in
most cases, since the date is not accurate.
