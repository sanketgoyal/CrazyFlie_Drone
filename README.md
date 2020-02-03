# CrazyFlie_Drone

Jan 28, 2020 - Feb 4th, 2020

## Assembling the Drone

The steps to assemble the drone were followed through the given link.
https://www.bitcraze.io/getting-started-with-the-crazyflie-2-0/

One important thing to be kept in mind is the differentiation between the CW and CCW propellers. The propeller with the marking of A are attached on the side of the base with the marking M2 and M4 and simillarly marking B on M1 and M3. Note: All the four propellers are to be attached such that the markings A and B are facing you.

![](/Images:Videos/CrazyFlie_motors.jpeg | width=100px)

<img src="https://github.com/sanketgoyal/CrazyFlie_Drone/blob/master/Images:Videos/Assembled%20Drone.jpeg" width="48">

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
![](Images:Videos/Video1.mp4)
To install the cfclient the link given below was used. It was pretty easy without any error or confusion. 
Link: https://github.com/bitcraze/crazyflie-clients-python

The only issue here is a lot of functions are not yet active cause the flowdeck is not yet connected to the drone. 

## ROS Configuration 

The link for ROS configuration is - https://github.com/whoenig/crazyflie_ros
rosrun crazyflie_tools scan 
This command helps to scan the uri of the drone which we will need to add in the crazyflie_server to initially connect the crazyflie.
