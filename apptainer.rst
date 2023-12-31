.. _about_apptainer:

***************************
About Apptainer/Singularity
***************************

.. todo::

   - Briefly discuss the different images that are provided (refer to
     trifinger_singularity README for details)


What is Apptainer?
==================

Apptainer_ (formerly called "Singularity") is a tool to run software inside
containers, similar to Docker. Compared to Docker it has a higher focus on
security and can be used without root permission.  Also programs in the
container are executed as the user of the host system which makes it much more
convenient when touching files of the host system (as it is happening when
building a mounted workspace).


Apptainer vs SingularityCE
==========================

Apptainer_ and SingularityCE_ both emerged from the original Singularity project. While
their features may diverge more significantly over time, they are currently (state end
of 2023) still mostly compatible.

This documentation assumes you are using Apptainer, however, it should work the same
with SingularityCE.  Just replace "apptainer" with "singularity" in all the commands (or
create an alias).


Install Apptainer
=================

You can download pre-build packages of recent releases from the `Apptainer
GitHub repository <https://github.com/apptainer/apptainer/releases/>`_.

For example on Ubuntu, download the deb package (called
"apptainer_X.Y.Z_amd64.deb") and install it with:

.. code-block:: sh

    $ sudo apt install ./apptainer_X.Y.Z_amd64.deb

In the following, we provide some basic information on how to use
Apptainer.  For more detailed information, please see the `official
documentation`_.


Get our Apptainer Image
=======================

We provide an Apptainer image with all dependencies needed to build and run the software
here.  You can download the latest version using:

.. code-block:: sh

    apptainer pull oras://ghcr.io/open-dynamic-robot-initiative/trifinger_singularity/trifinger_base:latest


In case you prefer to build the image yourself, see the trifinger_singularity_
repository on GitHub.


Run Something in the Container
==============================

To run the container in shell mode (i.e. opening a shell inside the container),
the following is often enough:

.. code-block:: sh

    apptainer shell path/to/image.sif

This will, however, be influenced by your local setup as environment variables
are exported and the home directory is mounted by default.  Further the current
working directory from which Apptainer is run is also bound inside the
container.

This default behaviour is often convenient but can cause issues in some cases.
A typical example would be a Python package installed in your home directory
(which will then be available in the container) which is not compatible with
versions of other packages inside the container.  To avoid these kind of issues
it is recommended to use the following command to run the container in a more
isolated way:

.. code-block:: sh

    export APPTAINERENV_DISPLAY=$DISPLAY  # <- you may want to put this line in your .bashrc
    apptainer shell -e --no-home --bind=$(pwd) path/to/image.sif

The arguments explained:

- The first line makes sure the DISPLAY environment variable is set correctly
  inside the container (only needed if you want to run GUI-based applications).
- ``-e`` (short for ``--cleanenv``) prevents environment variables to be
  exported.
- ``--no-home`` prevents your home directory from being bound.
- ``--bind=$(pwd)`` explicitly binds the current working directory.  This is
  needed if the working directory is inside your home directory as otherwise it
  is excluded by the ``--no-home``.

Note that with the above the current working directory is still bound in the
image, so it is possible to build/modify the workspace from the host-system when
Apptainer is run from the root directory of the workspace.


Compatibility with Nvidia Drivers
---------------------------------

When you are using Nvidia drivers and want to run a GUI-based application in the
container, you may need to add the ``--nv`` flag:

.. code-block:: sh

    apptainer shell --nv ... path/to/image.sif


Add Custom Dependencies to the Container
========================================

The image we provide already includes everything needed to run the robot
and the simulation. However, you may need additional libraries to use
them in our own code, which are not yet present. In this case, you can
create your own image which is based on our standard image but extends
it with your additional dependencies.

To extend the image, create *definition file* like the following:

.. code-block:: singularity

    # Specify the name of the base image below
    Bootstrap: localimage
    From: ./base_image.sif

    %post
        # Put commands to install additional dependencies here.
        # Make sure everything runs automatically without human input (e.g. add
        # `-y` to automatically say "yes" below).
        apt-get install -y package_name

See the official `Documentation for Definition Files`_ for all options in the
definition file.

Assuming you called your definition file ``user_image.def``, use the
following command to build the image. Note that the base image
(specified in the ``From:`` line) needs to be present in the directory in
which you call the command.

.. code-block:: sh

    $ apptainer build user_image.sif path/to/user_image.def


.. _Apptainer: https://apptainer.org
.. _SingularityCE: https://sylabs.io/singularity
.. _official documentation: https://apptainer.org/docs/
.. _Documentation for Definition Files: https://apptainer.org/docs/user/1.0/definition_files.html
.. _trifinger_singularity: https://github.com/open-dynamic-robot-initiative/trifinger_singularity
