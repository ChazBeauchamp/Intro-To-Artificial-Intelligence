from priority import PriorityQueue
from node import Node
from pancake_methods import flip_pancakes, flip_cost, check_goal, calculate_heuristic

def a_star(initial_state):
    start_node = Node(initial_state)
    start_node.set_heuristic_cost(calculate_heuristic(initial_state))
    frontier = PriorityQueue()
    frontier.push(start_node, start_node.total_cost())
    visited = set()

    while not frontier.is_empty():
        current_node = frontier.pop()

        if check_goal(current_node.state):
            return current_node.get_path(), current_node.path_cost, len(visited)

        visited.add(tuple(current_node.state))

        for k in range(2, len(current_node.state) + 1):
            child_state = flip_pancakes(current_node.state, k)
            child_cost = current_node.path_cost + flip_cost(k)
            child_node = Node(child_state, current_node, path_cost=child_cost)
            child_node.set_heuristic_cost(calculate_heuristic(child_state))
            
            if tuple(child_state) not in visited and child_node not in frontier:
                frontier.push(child_node, child_node.total_cost())
            elif child_node in frontier:
                existing_node = next(node for _, _, node in frontier._queue if node == child_node)
                if child_node.total_cost() < existing_node.total_cost():
                    frontier.remove(existing_node)
                    frontier.push(child_node, child_node.total_cost())
    # no solution
    return None, None, len(visited)

def uniform_cost(initial_state):
    start_node = Node(initial_state)
    frontier = PriorityQueue()
    frontier.push(start_node, start_node.path_cost)
    visited = set()

    while not frontier.is_empty():
        current_node = frontier.pop()

        if check_goal(current_node.state):
            return current_node.get_path(), current_node.path_cost, len(visited)

        visited.add(tuple(current_node.state))

        for k in range(2, len(current_node.state) + 1):
            child_state = flip_pancakes(current_node.state, k)
            child_cost = current_node.path_cost + flip_cost(k)
            child_node = Node(child_state, current_node, path_cost=child_cost)
            
            if tuple(child_state) not in visited and child_node not in frontier:
                frontier.push(child_node, child_node.path_cost)
            elif child_node in frontier:
                existing_node = next(node for _, _, node in frontier._queue if node == child_node)
                if child_node.path_cost < existing_node.path_cost:
                    frontier.remove(existing_node)
                    frontier.push(child_node, child_node.path_cost)
    # no solution
    return None, None, len(visited)