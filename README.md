# TurtleBot3 Navigation

## Project Overview
This project demonstrates the autonomous navigation of the TurtleBot3 robot in a modified stage_4 arena using ROS and smach. The robot visits predetermined locations in sequence, utilizing a custom map and the ROS navigation stack.

## Setup and Configuration
### Prerequisites
- ROS Noetic
- Gmapping
- Navigation stack
- Smach ROS

### Directory Structure
- **/maps**: Contains the map files used for navigation.
- **/src**: Contains source files and ROS packages.
- **/models**: Contains modified environment models.
- **/docs**: Additional project documentation.

## Usage
1. **Setting up the ROS environment**
   - Clone this repository into your catkin workspace src folder.
   - Build the workspace with `catkin_make`.
   - Source the setup files with `source devel/setup.bash`.
2. **Launching the Simulation**
   - Run `roslaunch [package_name] [launch_file.launch]` to start the simulation and navigation.
3. **Running the Smach State Machine**
   - Execute the state machine script to start the autonomous navigation.

## Authors
- Muhammad Siddique Khatri

