*************************
Software Package Overview
*************************

Below the main software packages used for to the TriFinger robots are listed.  See
:ref:`install_software` on how to install them.  Note that the installation will include
some additional utility packages from the ODRI project.  Below are only the packages
that are specifically written for the TriFinger robots.


- **robot_interfaces** --- [`source <https://github.com/open-dynamic-robot-initiative/robot_interfaces>`__ | :doc:`docs <robot_interfaces:index>`]
      Generic interface for the frontend-backend-system through which the user
      communicates with the robot.

- **robot_fingers** --- [`source <https://github.com/open-dynamic-robot-initiative/robot_fingers>`__ | :doc:`docs <robot_fingers:index>`]
      Robot-specific driver implementations for using the TriFinger robots with
      the robot_interfaces framework.

- **robot_properties_fingers** --- [`source <https://github.com/open-dynamic-robot-initiative/robot_properties_fingers>`__ | :doc:`docs <robot_properties_fingers:index>`]
      Contains the robot models (URDF and meshes) of all (Tri-)Finger robots.

- **blmc_drivers** --- [`source <https://github.com/open-dynamic-robot-initiative/blmc_drivers>`__ | :doc:`docs <blmc_drivers:index>`]
      Low-level drivers for communicating with CAN-based robots of the ODRI project.

- **trifinger_simulation** --- [`source <https://github.com/open-dynamic-robot-initiative/trifinger_simulation>`__ | :doc:`docs <trifinger_simulation:index>`]
      PyBullet simulation of the robots.  This can also be used as stand-alone
      Python package.  It provides an interface that is mostly identical to the
      one of the real robot (there are some differences, see the package
      documentation).

- **trifinger_cameras** --- [`source <https://github.com/open-dynamic-robot-initiative/trifinger_cameras>`__ | :doc:`docs <trifinger_cameras:index>`]
      Driver for the Basler cameras that are used in the TriFingerPro boxes.
      Using the sensor interface of robot_interfaces.

- **trifinger_object_tracking** --- [`source <https://github.com/open-dynamic-robot-initiative/trifinger_object_tracking>`__ | :doc:`docs <trifinger_object_tracking:index>`]
      Object tracking for the coloured cuboids that are, for example, used in
      the Real Robot Challenge.
      The object tracking is integrated into the camera driver, so this package
      contains a drop-in replacement for the driver of trifinger_cameras, which
      also provides the object pose in its observations.

- **trifinger_singularity** --- [`source <https://github.com/open-dynamic-robot-initiative/trifinger_singularity>`__]
      Contains the definition files for the :ref:`Apptainer/Singularity
      <about_apptainer>` images which can be used for building/running the software.

.. todo::

   probably not list the below ones, just mention that there are more packages which are
   all cloned via treep.

   - cli_utils --- [`source <https://github.com/MPI-IS/cli_utils>`__]
   - googletest --- [`source <https://github.com/google/googletest>`__]
   - mpi_cmake_modules --- [`source <https://github.com/machines-in-motion/mpi_cmake_modules>`__]
   - pybind11 --- [`source <https://github.com/pybind/pybind11>`__]
   - pybind11_opencv --- [`source <https://github.com/open-dynamic-robot-initiative/pybind11_opencv>`__]
   - real_time_tools --- [`source <https://github.com/machines-in-motion/real_time_tools>`__]
   - serialization_utils --- [`source <https://github.com/MPI-IS/serialization_utils>`__]
   - shared_memory --- [`source <https://github.com/machines-in-motion/shared_memory>`__]
   - signal_handler --- [`source <https://github.com/MPI-IS/signal_handler>`__]
   - time_series --- [`source <https://github.com/machines-in-motion/time_series>`__]
   - yaml_utils --- [`source <https://github.com/machines-in-motion/yaml_utils>`__]
