import random
import numpy as np

actions = [1, 2, 0]

def state(data, t, n):
    d = t - n + 1
    block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1]
    res = []
    for i in range(n - 1):
        res.append(block[i + 1] - block[i])
    return np.array([res])

def QLearning(data, n, episodes, a, b, g, eta):
    Q = {}
    for episode in range(episodes):
        t = 0
        total_profit = 0
        state_t = state(data, t, n)
        action = np.argmax([Q.get(str(state_t) + str(a), 0) for a in actions])
        while t < len(data) - 1:
            t += 1
            state_t1 = state(data, t, n)
            if random.uniform(0, 1) < eta:
                action = random.choice(actions)
            else:
                action = np.argmax([Q.get(str(state_t1) + str(a), 0) for a in actions])
            reward = data[t] - data[t - 1] if action == 1 else 0
            reward = -data[t] + data[t - 1] if action == 2 else reward
            total_profit += reward
            a = Q.get(str(state_t) + str(action), None)
            if a is None:
                a = 0
            b = max([Q.get(str(state_t1) + str(a), 0) for a in actions])
            Q[str(state_t) + str(action)] = a + eta * (reward + g * b - a)
            state_t = state_t1
    return Q

def backtesting(data, Q, n, eta):
    t = 0
    state_t = state(data, t, n)
    actions = [1, 2, 0]
    action = np.argmax([Q.get(str(state_t) + str(a), 0) for a in actions])
    buy = []
    sell = []
    hold = []
    while t < len(data) - 1:
        if action == 1:
            buy.append(t)
        elif action == 2:
            sell.append(t)
        else:
            hold.append(t)
        t += 1
        state_t = state(data, t, n)
        action = np.argmax([Q.get(str(state_t) + str(a), 0) for a in actions])
    return buy, sell, hold
