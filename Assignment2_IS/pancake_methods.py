import random
from collections import deque
from node import Node

def generate_random_stack (n):
    pancake_stack = list(range(1, n+1))
    random.shuffle(pancake_stack)
    return pancake_stack

def print_stack(stack):
    if isinstance(stack, Node):
        stack = stack.state
    print("Top ", " ".join(str(pancake) for pancake in stack), " Bottom")
        
def check_goal(stack):
    return stack == sorted(stack)

def calculate_heuristic(stack):
    gaps = 0
    for i in range(len(stack) - 1):
        if abs(stack[i] - stack[i+1]) > 1:
            gaps += 1
    return gaps

def flip_pancakes(stack, k):
    d = deque(stack[:k])
    d.reverse()
    return list(d) + stack[k:]

# Flip cost = backward cost
def flip_cost(k):
    return k