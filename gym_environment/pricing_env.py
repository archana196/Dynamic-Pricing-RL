import gymnasium as gym
from gymnasium import spaces
import numpy as np

from gym_environment.demand import simulate_booking
from gym_environment.reward import calculate_reward


class DynamicPricingEnv(gym.Env):
    """
    Custom Gymnasium Environment for Dynamic Pricing
    """

    metadata = {"render_modes": ["human"]}

    def __init__(
        self,
        inventory=100,
        booking_days=30,
        base_price=5000,
        price_step=500,
    ):

        super().__init__()

        # Configurable Parameters
        self.max_inventory = inventory
        self.max_days = booking_days
        self.base_price = base_price
        self.price_step = price_step

        # Observation:
        # [Inventory, Remaining Days, Current Price]
        self.observation_space = spaces.Box(
            low=np.array([0, 0, 1000], dtype=np.float32),
            high=np.array(
                [
                    inventory,
                    booking_days,
                    10000,
                ],
                dtype=np.float32,
            ),
            dtype=np.float32,
        )

        # Actions
        # 0 -> Decrease Price
        # 1 -> Keep Same
        # 2 -> Increase Price
        self.action_space = spaces.Discrete(3)

        self.reset()

    # -------------------------------------------------

    def _get_state(self):

        return np.array(
            [
                self.inventory,
                self.remaining_days,
                self.current_price,
            ],
            dtype=np.float32,
        )

    # -------------------------------------------------

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.inventory = self.max_inventory
        self.remaining_days = self.max_days
        self.current_price = self.base_price

        observation = self._get_state()

        info = {
            "inventory": self.inventory,
            "remaining_days": self.remaining_days,
            "price": self.current_price,
        }

        return observation, info

    # -------------------------------------------------

    def step(self, action):

        # Update Price

        if action == 0:
            self.current_price -= self.price_step

        elif action == 2:
            self.current_price += self.price_step

        self.current_price = max(1000, self.current_price)

        # -------------------------

        booking = simulate_booking(
            self.current_price,
            self.remaining_days,
        )

        revenue = 0

        if booking and self.inventory > 0:

            self.inventory -= 1
            revenue = self.current_price

        reward = calculate_reward(
            revenue,
            booking,
        )

        # One day passes

        self.remaining_days -= 1

        terminated = False

        if self.inventory <= 0:
            terminated = True

        if self.remaining_days <= 0:
            terminated = True

        truncated = False

        observation = self._get_state()

        info = {
            "booking": booking,
            "inventory": self.inventory,
            "remaining_days": self.remaining_days,
            "price": self.current_price,
            "revenue": revenue,
        }

        return (
            observation,
            reward,
            terminated,
            truncated,
            info,
        )

    # -------------------------------------------------

    def render(self):

        print("\n===== Dynamic Pricing Environment =====")
        print(f"Inventory       : {self.inventory}")
        print(f"Remaining Days  : {self.remaining_days}")
        print(f"Current Price   : ₹{self.current_price}")
        print("=======================================\n")

    # -------------------------------------------------

    def close(self):
        pass