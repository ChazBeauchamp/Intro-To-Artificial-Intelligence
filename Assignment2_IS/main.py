from pancake_methods import generate_random_stack, print_stack
from search_algorithms import a_star, uniform_cost

# Initialize
n = int(input("Enter the number of pancakes: "))
initial_state = generate_random_stack(n)
print("Initial state:")
print_stack(initial_state)

# User choice
algorithm = input("Choose algorithm (AStar or UCS): ").lower()

if algorithm == 'astar':
    solution, cost, nodes_explored = a_star(initial_state)
elif algorithm == 'ucs':
    solution, cost, nodes_explored = uniform_cost(initial_state)
else:
    print("Invalid algorithm. Please run the program again.")
    exit()

# Print results
if solution:
    print("Solution found!")
    print("Sequence of stack configurations:")
    for state in solution:
        print_stack(state)
    print(f"Total cost: {cost}")
    print(f"Number of nodes explored: {nodes_explored}")
else:
    print("No solution found.")
    print(f"Number of nodes explored: {nodes_explored}")