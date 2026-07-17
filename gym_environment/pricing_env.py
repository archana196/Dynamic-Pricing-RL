import gymnasium as gym
from gymnasium import spaces
import numpy as np

from gym_environment.demand import simulate_booking
from gym_environment.reward import calculate_reward


class DynamicPricingEnv(gym.Env):
    """
    Dynamic Pricing Environment for Reinforcement Learning.

    State:
        [
            inventory_ratio,
            remaining_days_ratio,
            current_price_ratio,
            competitor_price_ratio,
            booking_probability,
            demand_level
        ]

    Actions:
        0 -> Decrease Price
        1 -> Keep Price
        2 -> Increase Price

    Reward:
        Calculated using reward.py

    Episode Ends:
        - Inventory becomes zero
        - Booking window expires
    """

    metadata = {"render_modes": ["human"]}

    def __init__(
        self,
        inventory=100,
        booking_days=30,
        base_price=5000,
        min_price=2000,
        max_price=8000,
        price_step=500,
        competitor_price=5200,
    ):

        super().__init__()

        # -----------------------------
        # Environment Configuration
        # -----------------------------

        self.max_inventory = inventory
        self.max_days = booking_days

        self.base_price = base_price
        self.min_price = min_price
        self.max_price = max_price

        self.price_step = price_step

        self.default_competitor_price = competitor_price

        # -----------------------------
        # Observation Space
        # -----------------------------
        # All values are normalized to [0,1]
        #
        # [
        # inventory_ratio,
        # remaining_days_ratio,
        # current_price_ratio,
        # competitor_price_ratio,
        # booking_probability,
        # demand_level
        # ]
        # -----------------------------

        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(6,),
            dtype=np.float32,
        )

        # -----------------------------
        # Action Space
        # -----------------------------

        self.action_space = spaces.Discrete(3)

        # -----------------------------
        # Runtime Variables
        # -----------------------------

        self.inventory = None
        self.remaining_days = None

        self.current_price = None
        self.competitor_price = None

        self.booking_probability = 0.0
        self.demand_level = 0.0

        self.total_revenue = 0
        self.total_bookings = 0

        # Initialize Environment
        self.reset()



    # -------------------------------------------------
    # Internal State Representation
    # -------------------------------------------------

    def _get_state(self):
        """
        Returns the normalized observation.
        """

        inventory_ratio = self.inventory / self.max_inventory

        remaining_days_ratio = (
            self.remaining_days / self.max_days
        )

        current_price_ratio = (
            (self.current_price - self.min_price)
            / (self.max_price - self.min_price)
        )

        competitor_price_ratio = (
            (self.competitor_price - self.min_price)
            / (self.max_price - self.min_price)
        )

        state = np.array(
            [
                inventory_ratio,
                remaining_days_ratio,
                current_price_ratio,
                competitor_price_ratio,
                self.booking_probability,
                self.demand_level,
            ],
            dtype=np.float32,
        )

        return state

    # -------------------------------------------------
    # Reset Environment
    # -------------------------------------------------

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        # Reset inventory and booking window
        self.inventory = self.max_inventory
        self.remaining_days = self.max_days

        # Reset prices
        self.current_price = self.base_price
        self.competitor_price = (
            self.default_competitor_price
        )

        # Reset statistics
        self.total_revenue = 0
        self.total_bookings = 0

        # Initial values
        self.booking_probability = 0.0
        self.demand_level = 0.5

        observation = self._get_state()

        info = {
            "inventory": self.inventory,
            "remaining_days": self.remaining_days,
            "current_price": self.current_price,
            "competitor_price": self.competitor_price,
            "booking_probability": self.booking_probability,
            "demand_level": self.demand_level,
            "total_revenue": self.total_revenue,
            "total_bookings": self.total_bookings,
        }

        return observation, info
    

    # -------------------------------------------------
    # Environment Step
    # -------------------------------------------------

    def step(self, action):
        """
        Execute one environment step.
        """

        # -----------------------------
        # Apply Action
        # -----------------------------

        if action == 0:
            self.current_price -= self.price_step

        elif action == 2:
            self.current_price += self.price_step

        # Keep price within limits
        self.current_price = np.clip(
            self.current_price,
            self.min_price,
            self.max_price,
        )

        # -----------------------------
        # Simulate Competitor Price
        # -----------------------------

        competitor_change = self.np_random.integers(-200, 201)

        self.competitor_price = np.clip(
            self.competitor_price + competitor_change,
            self.min_price,
            self.max_price,
        )

        # -----------------------------
        # Demand Simulation
        # -----------------------------

        booking, probability = simulate_booking(
            current_price=self.current_price,
            competitor_price=self.competitor_price,
            remaining_days=self.remaining_days,
        )

        self.booking_probability = probability
        self.demand_level = probability

        # -----------------------------
        # Revenue
        # -----------------------------

        revenue = 0

        if booking and self.inventory > 0:

            self.inventory -= 1

            revenue = self.current_price

            self.total_bookings += 1
            self.total_revenue += revenue

        # -----------------------------
        # Reward
        # -----------------------------

        reward = calculate_reward(
            revenue=revenue,
            booking=booking,
            inventory=self.inventory,
            remaining_days=self.remaining_days,
            current_price=self.current_price,
        )

        # -----------------------------
        # One Day Passes
        # -----------------------------

        self.remaining_days -= 1

        # -----------------------------
        # Episode Termination
        # -----------------------------

        terminated = (
            self.inventory <= 0
            or self.remaining_days <= 0
        )

        truncated = False

        # -----------------------------
        # Next Observation
        # -----------------------------

        observation = self._get_state()

        # -----------------------------
        # Debug Information
        # -----------------------------

        info = {
            "booking": booking,
            "booking_probability": probability,
            "inventory": self.inventory,
            "remaining_days": self.remaining_days,
            "current_price": self.current_price,
            "competitor_price": self.competitor_price,
            "revenue": revenue,
            "reward": reward,
            "total_revenue": self.total_revenue,
            "total_bookings": self.total_bookings,
        }

        return (
            observation,
            reward,
            terminated,
            truncated,
            info,
        )
    

    # -------------------------------------------------
    # Render Environment
    # -------------------------------------------------

    def render(self):
        """
        Display the current environment state.
        """

        print("\n========== Dynamic Pricing Environment ==========")
        print(f"Inventory            : {self.inventory}/{self.max_inventory}")
        print(f"Remaining Days       : {self.remaining_days}/{self.max_days}")
        print(f"Current Price        : ₹{self.current_price}")
        print(f"Competitor Price     : ₹{self.competitor_price}")
        print(f"Booking Probability  : {self.booking_probability:.2f}")
        print(f"Demand Level         : {self.demand_level:.2f}")
        print(f"Total Bookings       : {self.total_bookings}")
        print(f"Total Revenue        : ₹{self.total_revenue}")
        print("=================================================\n")

    # -------------------------------------------------
    # Close Environment
    # -------------------------------------------------

    def close(self):
        """
        Cleanup resources.
        """
        pass