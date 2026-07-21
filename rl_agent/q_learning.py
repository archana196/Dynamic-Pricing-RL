import os
import random
import numpy as np


class QLearningAgent:
    """Q-Learning Agent for Dynamic Pricing"""

    def __init__(
        self,
        learning_rate=0.1,
        discount_factor=0.95,
        epsilon=1.0,
        epsilon_decay=0.995,
        min_epsilon=0.01,
        action_size=3,
    ):

        # Hyperparameters
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon

        self.action_size = action_size

        # Q Table
        self.q_table = {}

    # --------------------------------------------------
    # Convert continuous state to discrete state
    # --------------------------------------------------

    def discretize_state(self, state):
        """Convert normalized float values into integers.

        Example:
        [1.0, 0.93, 0.55, 0.61, 0.72, 0.69]
        becomes
        (10, 9, 5, 6, 7, 7)
        """
        state = np.array(state)
        state = (state * 10).astype(int)
        return tuple(state)

    # --------------------------------------------------
    # Initialize State
    # --------------------------------------------------

    def initialize_state(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.action_size)

    # --------------------------------------------------
    # Choose Action
    # --------------------------------------------------

    def choose_action(self, state):
        state = self.discretize_state(state)
        self.initialize_state(state)

        # Exploration
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_size - 1)

        # Exploitation
        return int(np.argmax(self.q_table[state]))

    # --------------------------------------------------
    # Bellman Update
    # --------------------------------------------------

    def update_q_table(self, state, action, reward, next_state):
        state = self.discretize_state(state)
        next_state = self.discretize_state(next_state)

        self.initialize_state(state)
        self.initialize_state(next_state)

        current_q = self.q_table[state][action]
        best_next_q = np.max(self.q_table[next_state])

        updated_q = current_q + self.learning_rate * (
            reward + self.discount_factor * best_next_q - current_q
        )

        self.q_table[state][action] = updated_q

    # --------------------------------------------------
    # Epsilon Decay
    # --------------------------------------------------

    def decay_epsilon(self):
        self.epsilon = max(
            self.min_epsilon,
            self.epsilon * self.epsilon_decay,
        )

    # --------------------------------------------------
    # Get Best Action
    # --------------------------------------------------

    def predict(self, state):
        state = self.discretize_state(state)
        self.initialize_state(state)
        return int(np.argmax(self.q_table[state]))

    # --------------------------------------------------
    # Save Model
    # --------------------------------------------------

    def save_q_table(self, filename="saved_models/q_table.npy"):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        np.save(
            filename,
            self.q_table,
            allow_pickle=True,
        )
        print(f"Q-table saved to {filename}")

    # --------------------------------------------------
    # Load Model
    # --------------------------------------------------

    def load_q_table(self, filename="saved_models/q_table.npy"):
        self.q_table = np.load(
            filename,
            allow_pickle=True,
        ).item()
        print(f"Q-table loaded from {filename}")