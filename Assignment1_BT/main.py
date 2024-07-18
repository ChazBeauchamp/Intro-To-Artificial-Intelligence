#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from bt.behavior_tree import tree_root
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, \
DUSTY_SPOT_SENSOR, HOME_PATH

# Main body of the assignment

done = False
docked = False
clean = ""
dusty = ""
cycles = 0

battery = int(input("How much battery do I have?: "))

if battery > 100 or battery < 0:
    battery = 50

while not done:
    # Each cycle in this while-loop is equivalent to 1 second time

    # Step 1: Change the environment
    #   - Change the battery level
    #   - Simulate the response of the dusty spot sensor
    #   - Simulate user input commands

    current_blackboard = btl.Blackboard()
    
    current_blackboard.set_in_environment(HOME_PATH, "")
    
    if battery < 30:
        
        current_blackboard.set_in_environment(BATTERY_LEVEL, battery)
        
        docked = True
        print("I need to go charge then.")
    else:
        
        current_blackboard.set_in_environment(BATTERY_LEVEL, battery)

        clean = input("Enter 'spot' for spot cleaning, 'general' for general "
                    "cleaning, or 'nothing' to do nothing: ")

        if clean == "spot":
            current_blackboard.set_in_environment(SPOT_CLEANING, True)
            current_blackboard.set_in_environment(GENERAL_CLEANING, False)
        elif clean == "general":
            current_blackboard.set_in_environment(SPOT_CLEANING, False)
            current_blackboard.set_in_environment(GENERAL_CLEANING, True)
            dusty = input("Type 'yes' if there is a dusty spot here: ")
            if dusty == "yes":
                current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
            else:
                current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
        elif clean == "nothing":
            current_blackboard.set_in_environment(SPOT_CLEANING, False)
            current_blackboard.set_in_environment(GENERAL_CLEANING, False)
        else:
            print("Invalid command, doing nothing")
            current_blackboard.set_in_environment(SPOT_CLEANING, False)
            current_blackboard.set_in_environment(GENERAL_CLEANING, False)

    # Step 2: Evaluating the tree
    result = tree_root.run(current_blackboard)
    
    if clean == "spot":
        i = 0
        while i < 20:
            tree_root.run(current_blackboard)
            i += 1
    if dusty == "yes":
        i = 0
        while i < 35:
            tree_root.run(current_blackboard)
            i += 1
    if docked:
        battery = 100
        docked = False

    # Step 3: Determine if your solution must terminate
    cycles += 1
    done_cleaning = input("Type 'done' to finish cleaning, or anything else "
                      "to continue: ")
    
    if done_cleaning == "done":
        print("Thanks for using me!")
        done = True
        
    if cycles == 30:
        print("Sorry, it's been 30 cycles, I need to stop now.")
        done = True