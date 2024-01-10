.. _install_software:

***************************
How to Install the Software
***************************

.. todo::

   - This page can probably be restructured a bit.


There are two options to use the TriFinger software:

1. Use the provided container with everything installed inside.
2. Build from source


Use Container with Pre-build Packages
=====================================

The "trifinger_robot" image from trifinger_singularity_ contains all packages
needed to use the robot.  This is the easiest way if you just want to use the
robots.

.. todo:: Add more information here.


Build from Source
=================

We provide a Apptainer image with all required dependencies to build and run
the software.  See :ref:`about_apptainer`.

We highly recommend to use that container to make sure you have all the
dependencies with proper versions. However, you can of course also build the
packages without Apptainer.  In this case you need to install all dependencies
manually, though (see trifinger_base.def in trifinger_singularity_ for
guidance).


Real-Time Requirements
----------------------

To ensure reliable communication with the robot hardware, a real-time Linux
kernel is needed.  See :doc:`Real Time Setup in the documentation of
robot_interfaces <robot_interfaces:doc/real_time>`


Get the Source with treep
-------------------------

The software for the TriFinger robots is organised as a collection of multiple packages,
each in its own git repository.  We therefore use a workspace management
tool called treep_ which allows easy cloning of multi-repository projects.

treep can be installed via pip:

.. code-block:: sh

    pip install treep

Clone the treep configuration containing the "ROBOT_FINGERS" project:

.. code-block:: sh

    git clone git@github.com:machines-in-motion/treep_machines_in_motion.git

**Note:**  treep searches for a configuration directory from the current working
directory upwards.  So you can use treep in the directory in which you invoked
the ``git clone`` command above or any subdirectory.

Now clone the project:

.. code-block:: sh

    treep --clone ROBOT_FINGERS
    # or use --clone-https to use https instead of ssh for cloning

.. important::

    By default treep uses SSH to clone from GitHub.  So for the above command to
    work, you need a GitHub account with a registered SSH key.  Further this key
    needs to work without asking for a password everytime.  To achieve this, run
    ::

        ssh-add

    first.

    If you don't want to use SSH, you can also use ``--clone-https`` instead of
    ``--clone``.


If the cloning was successful, your workspace should now have the following
structure:

.. code-block:: text

    /path/to/your/workspace
    ├── treep_machines_in_motion
    └── workspace
        └── src
            ├── blmc_drivers
            ├── cli_utils
            ├── googletest
            ├── mpi_cmake_modules
            ├── pybind11
            ├── pybind11_opencv
            ├── real_time_tools
            ├── robot_fingers
            ├── robot_interfaces
            ├── robot_properties_fingers
            ├── serialization_utils
            ├── shared_memory
            ├── signal_handler
            ├── time_series
            ├── trifinger_cameras
            ├── trifinger_object_tracking
            ├── trifinger_simulation
            └── yaml_utils



Build
-----

With Apptainer
~~~~~~~~~~~~~~

Go to the ``workspace`` directory (the one containing the ``src`` directory, see
above) and run the container in shell mode (see :ref:`about_apptainer`):

.. code-block:: sh

    apptainer shell -e --no-home --bind=$(pwd) path/to/image.sif

The current working directory gets automatically mounted into the container so
you can edit all the files from outside the container using your preferred
editor or IDE and all changes will directly be visible inside the container.
Vice versa modifications done from inside the container will modify the files on
the host system!

Inside the container first set up the environment:

.. code-block:: sh

    Apptainer> source /setup.bash

This will source the ROS `setup.bash` and do some other environment setup.

Now you can build with:

.. code-block:: sh

    Apptainer> colcon build


Without Apptainer
~~~~~~~~~~~~~~~~~

Go to the ``workspace`` directory (the one containing the ``src`` directory, see
above) and run

.. code-block:: sh

    colcon build

This assumes that ``colcon`` and all build dependencies are installed.


Real-Time-Capable Build
~~~~~~~~~~~~~~~~~~~~~~~

When running a PREEMPT_RT Linux kernel, this is automatically detected at
build-time and build flags are set accordingly.  If you want to make a real-time-capable
build while running a different kernel (e.g. when cross-compiling), you need to
explicitly set the ``OS_VERSION``:

.. code-block:: sh

    colcon build --cmake-args -DOS_VERSION=preempt-rt


.. note::

    If you see the following output during initialisation of the robot, this
    means you are running a non-real-time build.

    .. code-block:: text

        Warning this thread is not going to be real time.


Run Demo
--------

When the build finished successfully, you can run one of the demos to see if
everything works.

Before running anything, you need to source the ``setup.bash`` of the
workspace (this needs to be done every time you open a new terminal):

.. code-block:: sh

    source ./install/setup.bash


As a first test, you can run the "fake robot" demo (which doesn't need an actual
robot to be connected):

.. code-block:: sh

    ros2 run robot_fingers demo_fake_finger

It should produce output like this::

    Position: [299. 598. 897.]
    Position: [ 599. 1198. 1797.]
    Position: [ 899. 1798. 2697.]
    Position: [1199. 2398. 3597.]
    Position: [1499. 2998. 4497.]
    Position: [1799. 3598. 5397.]
    Position: [2099. 4198. 6297.]

You can cancel it with Ctrl+C.

For more demos (including the actual robot), see
:doc:`robot_fingers:doc/getting_started`.



.. _treep: https://pypi.org/project/treep/
.. _trifinger_singularity: https://github.com/open-dynamic-robot-initiative/trifinger_singularity
