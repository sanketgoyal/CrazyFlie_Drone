# CrazyFlie_Drone

Jan 28, 2020 - Feb 4th, 2020

## Assembling the Drone

The steps to assemble the drone were followed through the given link.
https://www.bitcraze.io/getting-started-with-the-crazyflie-2-0/

One important thing to be kept in mind is the differentiation between the CW and CCW propellers. The propeller with the marking of A are attached on the side of the base with the marking M2 and M4 and simillarly marking B on M1 and M3. Note: All the four propellers are to be attached such that the markings A and B are facing you.

### Testing
Switch on the power and all the propellers will spin in a sequence, completing the power on self-test. The link has a good description to understand the LED lights.

## Crazyflie Radio setting 

The crazyflie radio PA needs to be connected with our laptop to be used with the CfClient GUI and ROS. 
The issue faced here was after connecting while we tried to scan for crazyflie, we got an error of LIBSUB. 
The below link helped us to configure our crazyflie radio to our computer(Ubuntu) and eliminate the error. 

