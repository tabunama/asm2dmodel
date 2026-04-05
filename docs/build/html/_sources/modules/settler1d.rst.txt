One-dimensional settler module
==============================

Import
------

.. code-block:: python

   from asm2dmodel import settler1d

Class
-----

``Settler1D(SETTLERINIT2D, SETTLERPAR2D, DIM2D, LAYER2D, ASM2DPAR, DECAY, SETTLER, TEMPMODEL)``

Parameters
----------

- ``SETTLERINIT2D``: initial settler state vector
- ``SETTLERPAR2D``: settler parameter vector
- ``DIM2D``: settler dimensions
- ``LAYER2D``: settler layer definition
- ``ASM2DPAR``: ASM2d parameter vector
- ``DECAY``: decay-mode flag
- ``SETTLER``: reactive-settler flag
- ``TEMPMODEL``: temperature model flag

Notes
-----

This page documents the module-level interface intended for future flowsheet construction.
