#!/usr/bin/env python
"""
Description:
    Create a simple 3-state state machine.

Usage:
    $> ./state_machine.py

Output:
    [INFO] : State machine starting in initial state 'FOO' with userdata: 
            []
    [INFO] : State machine transitioning 'FOO':'done'-->'BAR'
    [INFO] : State machine transitioning 'BAR':'done'-->'BAZ'
    [INFO] : State machine terminating 'BAZ':'done':'succeeded'

"""

import smach
import logging
import sys
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils.multiranger import Multiranger

URI = 'radio://0/80/2M/E7E7E7E701'

if len(sys.argv) > 1:
    URI = sys.argv[1]

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

cflib.crtp.init_drivers(enable_debug_driver=False)
cf = Crazyflie(rw_cache='./cache')
######################################################################################################################

# class keep_flying(smach.State):
#     def __init__(self):
#         smach.State.__init__(self, outcomes = ['done','outcome'])
#         self.counter=0
#     def execute(self):
#         if self.counter < 1000000000:
#                 #print("dfg")
#                 self.counter += 1
#                 print("this",Multiranger.front.)
#                 return 'done'
#         else:
#                return 'outcome'

class front(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome1','outcome2'])
        self.range=0.4
    def execute(self,ud):    
                    #self.range=multiranger.front
                    print("this",type(Multiranger(SyncCrazyflie(URI, cf=cf)).front))
                    if self.range < 0.3:
                        return 'outcome2'
                    else:
                        vel_x=0.2
                        vel_y=0.0
                        vel_z=0.0
                        MotionCommander(SyncCrazyflie(URI, cf=cf)).start_linear_motion(0.2,0.0,0.0)
                        time.sleep(0.1)
                        return 'outcome1'


def main():
    #MotionCommander M1
    #M1.start_linear_motion(x,y,z)

    #cflib.crtp.init_drivers(enable_debug_driver=False)
    #cf = Crazyflie(rw_cache='./cache')
    # with SyncCrazyflie(URI, cf=cf) as scf:
    #     with MotionCommander(scf) as motion_commander:
    #         with Multiranger(scf) as multiranger:


    # Create a SMACH state machine
                sm = smach.StateMachine(outcomes=['succeeded','aborted'])

                # Open the container
                with sm:
                    # Add states to the container
                    #smach.StateMachine.add('keep_flying', keep_flying(), {'done':'keep_flying','outcome':'aborted'})
                    smach.StateMachine.add('front', front(), {'outcome1':'front','outcome2':'aborted'})
                    #smach.StateMachine.add('BAR', ExampleState(), {'done':'BAZ'})
                    #smach.StateMachine.add('BAZ',ExampleState(),{'done':'succeeded'})

                # Execute SMACH plan
                outcome = sm.execute()

if __name__ == '__main__':
    main()
