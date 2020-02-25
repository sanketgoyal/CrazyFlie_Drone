# CrazyFlie_Drone

Jan 28, 2020 - Feb 4th, 2020

## Assembling the Drone

The steps to assemble the drone were followed through the given link.
https://www.bitcraze.io/getting-started-with-the-crazyflie-2-0/

One important thing to be kept in mind is the differentiation between the CW and CCW propellers. The propeller with the marking of A are attached on the side of the base with the marking M2 and M4 and simillarly marking B on M1 and M3. Note: All the four propellers are to be attached such that the markings A and B are facing you.

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/CrazyFlie_motors.jpeg" width="300">

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/Assembled%20Drone.jpeg" width="300">

### Testing
Switch on the power and all the propellers will spin in a sequence, completing the power on self-test. The link has a good description to understand the LED lights.

## Crazyflie Radio setting 

The crazyflie radio PA needs to be connected with our laptop to be used with the CfClient GUI and ROS. 
The issue faced here was after connecting while we tried to scan for crazyflie, we got an error of LIBSUB. 
The below link helped us to configure our crazyflie radio to our computer(Ubuntu) and eliminate the error. 
- We had to update udev permissions to make usb radio to work. The key point to be noted here was to create a file at - /etc/udev/rules.d/99-crazyradio.rules
Link: https://github.com/bitcraze/crazyflie-lib-python#setting-udev-permissions

## Mobile App and CFclient

The crazyflie app can be used to control the drone. 

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/CrazyFlie_Mobile_App.gif" width="300">


To install the cfclient the link given below was used. It was pretty easy without any error or confusion. 
Link: https://github.com/bitcraze/crazyflie-clients-python

The only issue here is a lot of functions are not yet active cause the flowdeck is not yet connected to the drone. 

Feb 4th, 2020 - Feb 11th, 2020

## Attaching the expansion decks

Flowdeck and Multiranger were attached according to the given procedure. Keeping in mind the front of the crazyflie matches both the decks. Link - https://www.bitcraze.io/getting-started-with-expansion-decks/

Once the decks are connected we check if everything is working correctly or not using a python script which makes the crazyflie go in the opposite direction of the detected obstacle. 
Link - https://www.bitcraze.io/getting-started-with-stem-ranging-bundle/

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/multiranger.gif" width="500">

This ensures that both our expansion decks are working perfectly. 

## Moving the crazyflie around

To check various movements for the crazyflie, the drone is made to hover around in a circle in the followingg video. 
Link - https://www.bitcraze.io/getting-started-with-stem-drone-bundle/
<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/one_drone_circle.gif" width="500">


## Mapping of the environment using single crazyflie 
The initial image is of the enivironment 

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/obstacle_boxes.jpeg" width="300">

The next image is what we could map using the multiranger.

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/point_cloud.png" width="300">

## Multiple crazyflie using single crazyradio
### Connection
To attach multiple crazyflie to single crazyradio, we had to change the uri of the crazyflies. We did so using the cfclinent and going to configure 2.0 and writing the new uri by changing the last two digits. The proper process has been explained in 5.1 of the book on the following link. 
Link - http://act.usc.edu/publications/Hoenig_Springer_ROS2017.pdf
### Running them using single script
<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/two_drone_circle.gif" width="500">

## Wall Follower
A left wall follower using the Crazyflie was achieved. 

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/wall_follower.gif" width="500">

## Multi Robot videos

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/multi_1.gif" width="500">

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/multi_2.gif" width="500">

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/multi_3.gif" width="500">

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/multi_4.gif" width="500">

## ROS Configuration 

The link for ROS configuration is - https://github.com/whoenig/crazyflie_ros
rosrun crazyflie_tools scan 
This command helps to scan the uri of the drone which we will need to add in the crazyflie_server to initially connect the crazyflie.

### Ros Control  
Now succesfully 
-taking off

-Landing

-Sending to any x,y,z location. 

-Controlling all the drones seperately simultaniously i.e at 1 point all drones can go in different directions and can follow their own differnt path. 

### Rviz Configuration 
Got the model in Rviz, need to look into how to get multiranger data in rviz to develope map. 
