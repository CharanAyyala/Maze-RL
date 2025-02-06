import numpy as np
import random

maze = [
    ["S", ".", "#", ".", ".", ".", "#", ".", "G"],
    [".", "#", ".", "#", "#", ".", "#", ".", "#"],
    [".", ".", ".", "#", ".", ".", ".", ".", "."],
    ["#", ".", "#", "#", ".", "#", "#", ".", "#"],
    [".", ".", ".", ".", ".", ".", "#", ".", "."],
    [".", "#", "#", "#", "#", ".", "#", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

actions = ["up", "down", "left", "right"]


alpha = 0.1  # Mark the path
gamma = 0.9  
epsilon = 1.0  
epsilon_decay = 0.995  
min_epsilon = 0.01  
num_rows = len(maze)
num_cols = len(maze[0])
q_table = np.zeros((num_rows, num_cols, len(actions)))

def get_state_index(state):
    """Convert (row, col) to a unique state index."""
    return state[0] * num_cols + state[1]

def get_next_state(state, action):
    """Get the next state based on the current state and action."""
    row, col = state
    if action == "up":
        row = max(row - 1, 0)
    elif action == "down":
        row = min(row + 1, num_rows - 1)
    elif action == "left":
        col = max(col - 1, 0)
    elif action == "right":
        col = min(col + 1, num_cols - 1)
    return (row, col)

def get_reward(state):
    """Get the reward for reaching a state."""
    row, col = state
    if maze[row][col] == "G":
        return 100  
    elif maze[row][col] == "#":
        return -10  
    else:
        return -1  

def choose_action(state):
    """Choose an action using epsilon-greedy policy."""
    if random.uniform(0, 1) < epsilon:
        return random.choice(actions)  
    else:
        return actions[np.argmax(q_table[state[0], state[1]])]  

def update_q_table(state, action, reward, next_state):
    """Update the Q-table using the Bellman equation."""
    row, col = state
    next_row, next_col = next_state
    best_next_action = np.argmax(q_table[next_row, next_col])
    q_table[row, col, actions.index(action)] += alpha * (
        reward + gamma * q_table[next_row, next_col, best_next_action] - q_table[row, col, actions.index(action)]
    )

num_episodes = 1000
for episode in range(num_episodes):
    state = (0, 0)  
    total_reward = 0

    while maze[state[0]][state[1]] != "G":
        action = choose_action(state)
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)
        update_q_table(state, action, reward, next_state)
        state = next_state
        total_reward += reward

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}, Total Reward: {total_reward}, Epsilon: {epsilon:.2f}")

state = (0, 0)
path = [state]
while maze[state[0]][state[1]] != "G":
    action = actions[np.argmax(q_table[state[0], state[1]])]
    state = get_next_state(state, action)
    path.append(state)

print("\nOptimal Path:")
for row in range(num_rows):
    for col in range(num_cols):
        if (row, col) in path:
            print("X", end=" ")  
        else:
            print(maze[row][col], end=" ")
    print()
