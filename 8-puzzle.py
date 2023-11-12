import queue
import copy as c
import time

# Define the goal state and the initial state (start)
goal = [[1, 3, 4], [8, 6, 2], [7, 0, 5]]
start = [[5, 6, 7], [4, 0, 8], [3, 2, 1]]

# Define movement directions (up, down, left, right)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# Function to check if a move is valid
def valid(i, j):
    if i < 0 or i > 2 or j < 0 or j > 2:
        return False
    return True

# Function to find the (x, y) coordinates of the empty location (0)
def getZero(grid):
    i = 0
    j = 0
    for row in grid:
        j = 0
        for element in row:
            if element == 0:
                return [i, j]
            j += 1
        i += 1

# Function to perform a move by swapping two squares
def do_operation(x, y, tox, toy, state):
    state[x][y], state[tox][toy] = state[tox][toy], state[x][y]
    return state

# Initialize a queue for breadth-first search
q = queue.Queue()
q.put(1)

# Store states by their unique IDs
getting_state_by_id = {1: start}

# Convert goal and start states to tuples for efficient comparison
tgoal = tuple(tuple(row) for row in goal)
tstart = tuple(tuple(row) for row in start)

# Initialize dictionaries to store cost and parent information
cost = {}
cost[1] = 0
parent = {}
parent[1] = 1
getting_id_by_state = {}
getting_id_by_state[tstart] = 1
id = 2

# Perform breadth-first search
while q.qsize()>= 1:
    curr = q.get()
    # Check if the current state matches the goal state
    if list(list(row) for row in getting_state_by_id[curr]) == goal:
        print(cost[curr])
        break

    x, y = getZero(getting_state_by_id[curr])

    # Try each possible move (up, down, left, right)
    for i in range(4):
        tox = x + dx[i]
        toy = y + dy[i]

        if valid(tox, toy):
            cpy = do_operation(x, y, tox, toy, list(list(row) for row in getting_state_by_id[curr]))
            tcpy = tuple(tuple(row) for row in cpy)

            if tcpy not in getting_id_by_state:
                q.put(id)
                getting_state_by_id[id] = tcpy
                getting_id_by_state[tcpy] = id
                cost[id] = cost[curr] + 1
                parent[id] = curr
                id += 1

# Reconstruct the path from the goal state to the start state
ans = []

# Function to build the path
def build(i):
    if parent[i] == i:
        ans.append(i)
        return
    ans.append(i)
    build(parent[i])

# Start building the path from the goal state
build(getting_id_by_state[tgoal])
ans.reverse()

# Print the states along the shortest path
for i in ans:
    print(getting_state_by_id[i])