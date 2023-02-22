import numpy as np
import random
from kaggle_environments import make, evaluate

# Define the Q-learning agent
class QLearningAgent:
    def __init__(self, config, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.config = config
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate
        self.q_table = np.zeros((config.rows, config.columns, config.columns))  # Q-table

    def get_action(self, obs):
        # Use epsilon-greedy strategy to choose an action
        if random.random() < self.epsilon:
            return random.randint(0, self.config.columns - 1)
        else:
            state = np.array(obs['board']).reshape(self.config.rows, self.config.columns)
            valid_moves = [col for col in range(self.config.columns) if state[0][col] == 0]
            if not valid_moves:
                return random.randint(0, self.config.columns - 1)
            q_values = self.q_table[state[0], :, valid_moves]
            max_q_value = np.max(q_values)
            actions = [move for move, q_value in zip(valid_moves, q_values) if q_value == max_q_value]
            return random.choice(actions)

    def update(self, obs, action, reward, next_obs):
        state = np.array(obs['board']).reshape(self.config.rows, self.config.columns)
        next_state = np.array(next_obs['board']).reshape(self.config.rows, self.config.columns)
        next_valid_moves = [col for col in range(self.config.columns) if next_state[0][col] == 0]
        next_q_values = self.q_table[next_state[0], :, next_valid_moves]
        if not next_valid_moves:
            next_max_q_value = 0
        else:
            next_max_q_value = np.max(next_q_values)
        self.q_table[state[0], action, action] += self.alpha * (reward + self.gamma * next_max_q_value - self.q_table[state[0], action, action])

# Define the game environment
env = make("connectx", debug=True)

# Initialize the Q-learning agent
agent = QLearningAgent(env.configuration)

# Train the agent for 100 episodes
for i in range(100):
    obs = env.reset()
    done = False
    while not done:
        action = agent.get_action(obs)
        next_obs, reward, done, info = env.step(action)
        agent.update(obs, action, reward, next_obs)
        obs = next_obs

# Test the agent against a random agent
scores = evaluate("connectx", [agent.get_action, "random"], num_episodes=10)
print(scores)
