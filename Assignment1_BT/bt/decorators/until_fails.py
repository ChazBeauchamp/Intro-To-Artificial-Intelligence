#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 2.0.1 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

class UntilFails(btl.Decorator): 
    """
    Specific implementation of the until fails decorator.
    """

    def __init__(self, child: btl.TreeNode):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(child)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum: 
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        result_child = self.child.run(blackboard)
        if result_child == btl.ResultEnum.FAILED:
            return self.report_succeeded(blackboard, 0)

        return self.report_running(blackboard, 0)