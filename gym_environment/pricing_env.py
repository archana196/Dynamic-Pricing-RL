import gymnasium as gym
from gymnasium import spaces


class DynamicPricingEnv(gym.Env):
    """
    Custom Gymnasium Environment for Dynamic Pricing
    Week 1: Environment Skeleton
    """

    metadata = {"render_modes": ["human"]}

    def __init__(self):
        super().__init__()

        # Observation Space (Placeholder)
        self.observation_space = spaces.Box(
            low=0,
            high=100,
            shape=(5,),
            dtype=float
        )

        # Action Space
        # 0 = Decrease Price
        # 1 = Keep Price Same
        # 2 = Increase Price
        self.action_space = spaces.Discrete(3)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        observation = [0, 0, 0, 0, 0]
        info = {}

        return observation, info

    def step(self, action):
        observation = [0, 0, 0, 0, 0]
        reward = 0
        terminated = False
        truncated = False
        info = {}

        return observation, reward, terminated, truncated, info

    def render(self):
        pass

    def close(self):
        pass