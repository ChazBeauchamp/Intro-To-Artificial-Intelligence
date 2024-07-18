#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

import random

class CleanFloor(btl.Task):
    """
    Implementation of the Task "Clean Floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning Floor")
        
        # get random number (low probability to return failure)
        num = random.randrange(1, 10)
        
        if num == 1:
            return self.report_failed(blackboard)
        
        return self.report_succeeded(blackboard)
    
    
    