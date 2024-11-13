import numpy as np

# Initialize Q-table with zeros
states = ['Green', 'Yellow', 'Red']
actions = ['Switch', 'Hold']
Q_table = np.zeros((len(states), len(actions)))

# Rewards for actions in different states
rewards = {
    ('Green', 'Switch'): -10, # Switching away from green causes congestion
    ('Green', 'Hold'): 10,    # Holding green maintains traffic flow
    ('Yellow', 'Switch'): 5,  # Switching to green from yellow is beneficial
    ('Yellow', 'Hold'): -5,   # Holding yellow increases risk of accidents
    ('Red', 'Switch'): 0,     # Switching from red doesn't cause harm
    ('Red', 'Hold'): 5        # Holding red prevents unnecessary delays
}

# Function to update Q-values
def update_q_value(state, action, reward, learning_rate=0.1, discount_factor=0.9):
    current_q = Q_table[states.index(state), actions.index(action)]
    max_future_q = np.max(Q_table[states.index(state), :])
    Q_table[states.index(state), actions.index(action)] = current_q + learning_rate * (reward + discount_factor * max_future_q - current_q)

# Example update
update_q_value('Green', 'Hold', rewards[('Green', 'Hold')])