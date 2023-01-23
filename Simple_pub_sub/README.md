<h2>Design a ROS code for the following Scenario: There are two publishers 
namely Pub1 and Pub2 and there are three subscribers Sub1, sub2 and Sub3.</h2>

CASE 1 : Pub1 Publishes a topic called \CSE3102 and Sub1 subscribed to it.

CASE 2 : Pub2 publishes a topic called \cse2034 and, sub2, sub3 are subscribed to it. 
Design a python script for ROS and submit the following details.

<h3>Robotic Operating System (ROS)</h3>
ROS1 - Noetic 

OS: Ubuntu 20.04 

some of the commands are 
rosrun, roscore, rosnode, roslaunch, rqt_graph, rosgraph, etc. 

Prerequisites:
1. Ubuntu OS (basic commands)
2. PATH Setting information 
3. basic knowledge of Unix and Linux Family.
4. Programming knowledge (C++ and Python)

Examples or exercises
0. Basic ROS exercise
1. Publisher, Subscriber
2. Turtlesim 
3. TurtleBot 
4. Gazebo
etc.

To begin with, open a terminal and run the follolwing command 

<h4>$ roscore</h4>

Open another Terminal and run the first.py using 
<h4>$ python3 first.py</h4>

ROS has a build system called catkin which supports
* easier deployment 
* cross compilation
etc.

some commands related to catkin is 
<h4>$ catkin_make</h4> 
<h4>$ catkin_init_workspace</h4> 
<h4>$ catkin_create_pkg</h4>


Step 1:
Create a folder in the /home/{your_machine_name} directory using the command 

<h4>$ mkdir -p chaitanya_ws/src</h4>
<h4>$ cd chaitanya_ws/</h4>

<h4>$ catkin_make</h4>
after the above command, two folder namely build/ and devel/ might have created. 

Now we need to set the PATH for this file 
devel/setup.bash 

One method is to use , source command when opening a new terminal every time, the command is 

<h4>$ source /home/chaitanya/chaitanya_ws/devel/setup.bash</h4>

Second method is include the command in the /home/chaitanya/.bashrc file, so that command will run without any issues when a new terminal is opened.
after the second step, logout and login back to get the command working and activated else run the command 
<h4>$ source .bashrc</h4>

Step 2 : 
Go to chaitanya_ws/src folder and create a catkin package using the following command 

<h4>$ cd chaitanya_ws/src</h4>

<h4>$ catkin_create_pkg ros_tutorial rospy std_msgs</h4>
<h4>$ cd ..</h4>

<h4>$ catkin_make</h4>
(this time, the make will include the ros_tutorial also in to the devel and build libraries)

Step3 - We will be creating two files namely 
1. pub1.py
2. sub1.py

Create the above files in the folder 
chaitanya_ws/src/ros_tutorial/script

And give full permission to run 

<h4>$ chmod 777 *.py</h4> 

Step 4 - running the publisher and subscriber, we need to open two windows one for pub and another for sub.

In Terminal 1 
Go to 
<h4>$ cd chaitanya_ws/</h4>
<h4>$ source ./devel/setup.bash </h4>

<h4>$ rosrun ros_tutorial1 pub1.py</h4>

in Terminal 2 
Go to 
<h4>$ cd chaitanya_ws/</h4>
<h4>$ source ./devel/setup.bash </h4>
<h4>$ rosrun ros_tutorial sub1.py</h4>

You can see the output of "I took ROS Knowledge" by the Subscriber and "ROS Knowledge" by the publisher.

<h4>$ rqt_graph </h4>
will open the graph of all the nodes running under the ROS.
