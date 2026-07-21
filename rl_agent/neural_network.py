import torch
import torch.nn as nn


class DQN(nn.Module):

    def __init__(self, state_size=6, action_size=3):

        super(DQN, self).__init__()

        self.network = nn.Sequential(

            nn.Linear(state_size, 64),

            nn.ReLU(),

            nn.Linear(64, 64),

            nn.ReLU(),

            nn.Linear(64, action_size)

        )

    def forward(self, x):

        return self.network(x)