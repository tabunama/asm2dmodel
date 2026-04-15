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

- ``SETTLERINIT2D``: initial settler state vector, length 250
- ``SETTLERPAR2D``: settler sedimentation parameter vector, length 6
- ``DIM2D``: settler dimensions, length 2
- ``LAYER2D``: settler layer definition, length 2
- ``ASM2DPAR``: ASM2d parameter vector, length 73
- ``DECAY``: decay-mode flag
- ``SETTLER``: reactive-settler flag
- ``TEMPMODEL``: temperature model flag

Functions
---------

``init(XINIT)``
   Initialize the internal 250-state settler vector.

``outputs(x, u, tempmodel)``
   Return the 316-output vector from the current settler state and 28-input feed vector.

``rhs(t, x, u, SEDPAR, DIM, LAYER, ASMPAR, decay_switch, reactive_settler, tempmodel)``
   Return the 250-state derivative vector.

Notes
-----

This module represents the dynamic 10-layer secondary/final clarifier used after the ASM2d biological reactors.
It is not intended for primary clarification. For the primary clarifier, use the separate ``primclar`` module.
