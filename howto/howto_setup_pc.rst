**************************************
How to set up a Computer for the Robot
**************************************


This guide shows you how to set up a computer to control a TriFinger robot.


Hardware Requirements
=====================

There are no special requirements for the computer. In principle any desktop PC
should work, as long as you can equip them with enough CAN interfaces. For the
TriFinger robot, 6 CAN interfaces are needed (2 per finger).

We use the dual-channel PCI Express CAN cards from PEAK (model number
IPEH-003027, not the FD version!) [1]_.
Since the robot requires 6 ports, 3 cards
are needed.  See also the `ODRI hardware documentation
<https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware/blob/master/electronics/ti_electronics/README.md#can-control>`_.

.. [1] We also tried the CAN FD cards from PEAK but `had problems with them
   <https://forum.peak-system.com/viewtopic.php?f=203&t=6587>`_, so they are not
   recommended.  Cards from other manufacturers may work if they support
   SocketCAN, but we haven't tested them, so we can't make a definite statement.


Real Time Operating System
==========================

For stable control of the robot, a real-time capable operating system is needed.
We are using a standard Ubuntu 22.04 but install a kernel with better real-time
capability (either the "lowlatency" kernel or the "preempt_rt" patch), see
:doc:`Real Time Setup in the documentation of robot_interfaces
<robot_interfaces:doc/real_time>`

Other Linux distributions will likely work as well but the installation steps
may differ there.  All our documentation assumes you are using Ubuntu.


Configure the CAN Interfaces
============================

Automatically initialise CAN interfaces
---------------------------------------

We are using SocketCAN to access the CAN buses, so they are handled like network
interfaces.  By default, the CAN interfaces are disabled when you start the
computer.  To have them initialised automatically, create a file
``/etc/systemd/network/80-can.network`` with this content:

.. code-block:: ini

    [Match]
    Name=can*

    [CAN]
    BitRate=1000000


Then enable the systemd-networkd service to enable them automatically at boot
time:

.. code-block:: text

    sudo systemctl enable systemd-networkd

You can also (re-)start the systemd-networkd service to enable the interfaces
without rebooting:

.. code-block:: text

    sudo systemctl restart systemd-networkd

Once activated, the CAN interfaces should be listed as network interfaces
"can0", ..., "can5" when running

.. code-block:: text

   ip link


Determine which physical CAN port corresponds to which interface
----------------------------------------------------------------

Unfortunately it is usually not obvious which interface name corresponds to
which physical port, so you have to determine this empirically, for example with
the following procedure:

1. Remove all CAN connectors and potentially restart the computer to reset all
   connections.
2. Run the following command see the activity of the CAN interfaces (to install
   ``netstat`` run ``sudo apt install net-tools``):

   .. code-block:: sh

      watch -n 1 netstat -i

   This should show all zeros in the beginning.

3. Turn on the robot and take one of its CAN connectors (doesn't matter which,
   it just needs to be active).
4. Plug the connector into one of the sockets and watch the output of netstat.
   The RX-OK value of one of the ports should start increasing now.  This is the
   port to which you just connected.
5. Label the port with the corresponding interface name.
6. Unplug the connector and repeat from step 4 with the next port.  RX-OK
   should always only increase for the one that is currently connected.



Connect the robot to the computer
---------------------------------

Once you determined the mapping of physical ports to interface names, you can
connect all the CAN connectors of the robots.

While it is possible to specify which part of the robot is connected to which
interface in the robot configuration, we recommend that you connect them in
the following order (then you don't need to modify the default configuration):

.. list-table::

   * - can0
     - Finger0, CAN A
   * - can1
     - Finger0, CAN B
   * - can2
     - Finger120, CAN A
   * - can3
     - Finger120, CAN B
   * - can4
     - Finger240, CAN A
   * - can5
     - Finger240, CAN B

See :ref:`finger_and_camera_names` on which finger is which.
Each finger is controlled by two motor boards A and B, where A controls the
middle and lower joint while B controls the upper joint.

.. todo:: 

   - Link to robot_fingers config reference
   - Is A/B actually good nomenclature for the boards or better use numbers (0/1
     or 1/2)?
