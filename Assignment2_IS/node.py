class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.heuristic_cost = None
        
    # less than
    def __lt__(self, other):
        if self.total_cost() == other.total_cost():
            return self.path_cost < other.path_cost
        return self.total_cost() < other.total_cost()

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def set_heuristic_cost(self, heuristic_cost):
        self.heuristic_cost = heuristic_cost

    def total_cost(self):
        return self.path_cost + (self.heuristic_cost or 0)

    def __str__(self):
        return f"State: {self.state}, Path Cost: {self.path_cost}, Heuristic: {self.heuristic_cost}"

    def get_path(self):
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))