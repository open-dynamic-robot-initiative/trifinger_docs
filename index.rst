***********************
TriFinger Documentation
***********************

.. warning::

   This documentation is still work in progress and thus does not cover everything yet.


The TriFinger Robots
====================

.. container:: flex-row

   .. figure:: images/trifingerpro.jpg
      :alt: TriFingerPro robot holding a cube
      :width: 80%

      TriFingerPro

   .. figure:: images/trifingeredu.jpg
      :alt: TriFingerEdu robot
      :width: 80%

      TriFingerEdu


The TriFinger robots have been developed and built at the `Max Planck Institute for
Intelligent Systems`_ (MPI-IS) in Tübingen, Germany.
There are currently eight **TriFingerPro** robots hosted at MPI-IS which can be accessed
remotely and were used for the `Real Robot Challenge`_.

The **TriFingerEdu** is an open-source version of the challenge robot, with identical
actuators, almost identical kinematics, and identical software.
Compared to the challenge platform, the "Edu"-version is easier to construct, such that
researchers are able to build it themselves.


About this Documentation
========================

Documentation of the usage of the TriFinger robots and of the various software packages
that are involved is a bit distributed over several places.  The documentation you are
currently reading serves as a main entry point that covers the overarching aspects and
points to more specific documentations (e.g. of individual packages) where appropriate.


Content
=======

.. toctree::
   :caption: How-to Guides
   :maxdepth: 1

   howto/installation

.. toctree::
   :caption: References
   :maxdepth: 1

   package_overview.rst
   other_resources



.. _Max Planck Institute for Intelligent Systems: https://is.mpg.de
.. _Real Robot Challenge: https://www.real-robot-challenge.com
.. _TriFingerEdu hardware documentation: https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/mechanics/tri_finger_edu_v1/README.md
.. _ODRI forum: https://odri.discourse.group
