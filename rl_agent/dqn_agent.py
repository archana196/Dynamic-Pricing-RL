import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from rl_agent.neural_network import DQN
from rl_agent.replay_buffer import ReplayBuffer


class DQNAgent:

    def __init__(self):

        self.state_size = 6
        self.action_size = 3

        self.learning_rate = 0.001
        self.gamma = 0.99

        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.01

        self.batch_size = 64

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        # Main Network
        self.model = DQN(
            self.state_size,
            self.action_size
        ).to(self.device)

        # Target Network
        self.target_model = DQN(
            self.state_size,
            self.action_size
        ).to(self.device)

        self.target_model.load_state_dict(
            self.model.state_dict()
        )

        self.optimizer = optim.Adam(
            self.model.parameters(),
            lr=self.learning_rate,
        )

        self.criterion = nn.MSELoss()

        self.memory = ReplayBuffer(
            capacity=10000
        )

    # -----------------------------------------------------
    # Choose Action (Epsilon Greedy)
    # -----------------------------------------------------

    def choose_action(self, state):

        if random.random() < self.epsilon:
            return random.randint(
                0,
                self.action_size - 1,
            )

        state = torch.FloatTensor(state).unsqueeze(0).to(
            self.device
        )

        with torch.no_grad():
            q_values = self.model(state)

        return torch.argmax(q_values).item()

    # -----------------------------------------------------
    # Store Experience
    # -----------------------------------------------------

    def remember(
        self,
        state,
        action,
        reward,
        next_state,
        done,
    ):

        self.memory.push(
            state,
            action,
            reward,
            next_state,
            done,
        )

    # -----------------------------------------------------
    # Train Network
    # -----------------------------------------------------

    def train(self):

        if len(self.memory) < self.batch_size:
            return

        batch = self.memory.sample(
            self.batch_size
        )

        states, actions, rewards, next_states, dones = zip(
            *batch
        )

        states = torch.FloatTensor(
            np.array(states)
        ).to(self.device)

        actions = torch.LongTensor(
            actions
        ).unsqueeze(1).to(self.device)

        rewards = torch.FloatTensor(
            rewards
        ).unsqueeze(1).to(self.device)

        next_states = torch.FloatTensor(
            np.array(next_states)
        ).to(self.device)

        dones = torch.FloatTensor(
            dones
        ).unsqueeze(1).to(self.device)

        # Current Q Values

        current_q = self.model(states).gather(
            1,
            actions,
        )

        # Target Q Values

        with torch.no_grad():

            max_next_q = self.target_model(
                next_states
            ).max(
                1,
                keepdim=True,
            )[0]

            target_q = rewards + (
                self.gamma
                * max_next_q
                * (1 - dones)
            )

        loss = self.criterion(
            current_q,
            target_q,
        )

        self.optimizer.zero_grad()

        loss.backward()

        self.optimizer.step()

        # Epsilon Decay

        if self.epsilon > self.min_epsilon:

            self.epsilon *= self.epsilon_decay

            self.epsilon = max(
                self.min_epsilon,
                self.epsilon,
            )

    # -----------------------------------------------------
    # Update Target Network
    # -----------------------------------------------------

    def update_target_network(self):

        self.target_model.load_state_dict(
            self.model.state_dict()
        )

    # -----------------------------------------------------
    # Save Model
    # -----------------------------------------------------

    def save_model(self, path):

        torch.save(
            self.model.state_dict(),
            path,
        )

    # -----------------------------------------------------
    # Load Model
    # -----------------------------------------------------

    def load_model(self, path):

        self.model.load_state_dict(
            torch.load(
                path,
                map_location=self.device,
            )
        )

        self.target_model.load_state_dict(
            self.model.state_dict()
        )