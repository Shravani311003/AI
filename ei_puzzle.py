import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define possible moves
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_heuristic(state):
    """Calculate the Manhattan distance heuristic."""
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_x = (state[i][j] - 1) // 3
                target_y = (state[i][j] - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance


def is_valid_move(x, y):
    """Check if a move is valid."""
    return 0 <= x < 3 and 0 <= y < 3


def get_children(state):
    """Generate possible moves from current state."""
    children = []
    x, y = find_zero(state)
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(new_x, new_y):
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            children.append(new_state)
    return children


def find_zero(state):
    """Find the position of the empty tile."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def a_star(start_state):
    """A* algorithm to solve the 8-puzzle."""
    heap = [(get_heuristic(start_state), 0, start_state)]
    heapq.heapify(heap)
    visited = set()

    while heap:
        _, cost, current_state = heapq.heappop(heap)

        if current_state == goal_state:
            return cost

        visited.add(str(current_state))

        print("Current State:")
        print_state(current_state)

        for child in get_children(current_state):
            if str(child) not in visited:
                print("Child State:")
                print_state(child)
                heapq.heappush(heap, (cost + get_heuristic(child), cost + 1, child))

    return -1  # No solution found


def print_state(state):
    """Print the state."""
    for row in state:
        print(row)
    print()


# Example usage
start_state = [[1, 2, 3],
               [4, 5, 6],
               [7, 0, 8]]

steps = a_star(start_state)
if steps != -1:
    print(f"Number of steps to reach the goal state: {steps}")
else:
    print("No solution found.")