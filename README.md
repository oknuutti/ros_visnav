# Setup

If using Windows Subsystem for Linux (WSL) on Windows 10, follow this to get the graphics working:
https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde

- Install ROS Noetic (I use Ubuntu 20.04): http://wiki.ros.org/noetic/Installation/Ubuntu
- Setup Catkin workspace
- Clone https://github.com/oknuutti/VINS-Fusion into the `src` folder (for rviz and hw config files)
- Install `visnav` package using `sudo pip install --no-deps git+https://github.com/oknuutti/hw_visnav`,
  and install dependencies with `sudo pip install "numpy>=1.18,<1.19" numba numpy-quaternion scipy`
- Clone `nokia_navint` repo into the `src` folder
- Clone this repo into the `src` folder
- Run `catkin_make`

If you have problems with connecting from WSL to your x-server, check that the following is unticked:
  - Windows defender firewall > advanced > windows defender firewall properties
    \> public profile > protected network connections > customize... > vEthernet (WSL)

# Running

Using VINS visualization:
```
roslaunch vins vins_rviz.launch &
rosrun pyvio vio_node.py ~/catkin_ws/src/VINS-Fusion/config/nokiapl/main_lr.yaml 
```

Using alternative visualization:
```
roslaunch &
rosrun pyvio vio_node.py ~/catkin_ws/src/VINS-Fusion/config/nokiapl/main_lr.yaml --verbosity=2
```

Irrespective of chosen visualization, feed input data using e.g.:
```
rosrun nokia_navint storage.py --imu-conf=~/catkin_ws/src/VINS-Fusion/config/nokiapl/imu.yaml --type=jouko \
                               --path=~/path/to/flight/39 --skip=350 --adj-dt=-0.73
```

To list possible arguments, run `rosrun pyvio vio_node.py --help`
