ASM2d reactor module
====================

Import
------

.. code-block:: python

   from asm2dmodel import asm2d

Class
-----

``ASM2D(XINIT3, PAR3, VOL3, SOSAT3, DECAY, TEMPMODEL, ACTIVATE)``

Parameters
----------

- ``XINIT3``: initial ASM2d state vector
- ``PAR3``: ASM2d parameter vector
- ``VOL3``: reactor volume
- ``SOSAT3``: oxygen saturation value
- ``DECAY``: decay-mode flag
- ``TEMPMODEL``: temperature model flag
- ``ACTIVATE``: dummy-state activation flag

Notes
-----

This page documents the module-level interface intended for future flowsheet construction.
