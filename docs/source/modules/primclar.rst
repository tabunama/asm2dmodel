Primary clarifier module
========================

Import
------

.. code-block:: python

   from asm2dmodel import primclar

Class
-----

``PrimClar(PAR)``

Parameters
----------

- ``PAR``: primary-clarifier parameter vector, length 4

  - ``PAR[0]``: ``sec2_perc``
  - ``PAR[1]``: ``TSS_removal_perc``
  - ``PAR[2]``: ``inorganic_factor``
  - ``PAR[3]``: ``inorganic_factor_P``

Functions
---------

``outputs(u, PAR)``
   Split a 26-state ASM2d influent vector into a 52-state output vector.

Output structure
----------------

The returned vector has length 52:

- ``y[0:26]``: overflow / primary effluent
- ``y[26:52]``: underflow / primary sludge

Notes
-----

This module is an algebraic primary clarifier for the 26-state ASM2d stream interface.
Soluble states are passed through, while particulate states are separated according to the clarifier parameters.
It is intended for use before the biological reactors.
