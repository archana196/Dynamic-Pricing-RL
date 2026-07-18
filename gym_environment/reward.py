class RewardCalculator:
    """
    Reward shaping for Dynamic Pricing RL.

    Objectives:
    - Maximize revenue
    - Encourage successful bookings
    - Sell inventory before deadline
    - Avoid excessive pricing
    - Reduce unsold inventory
    """

    def __init__(self):

        self.booking_bonus = 20
        self.no_booking_penalty = -10

    # -------------------------------------------------

    def calculate_reward(
        self,
        revenue,
        booking,
        inventory,
        remaining_days,
        current_price,
    ):

        reward = 0.0

        # -----------------------------
        # Revenue Reward
        # -----------------------------
        # Balanced scaling for DQN

        reward += revenue / 200.0

        # -----------------------------
        # Booking Reward
        # -----------------------------

        if booking:
            reward += self.booking_bonus
        else:
            reward += self.no_booking_penalty

        # -----------------------------
        # Inventory Utilization
        # -----------------------------

        inventory_ratio = inventory / 100

        if inventory_ratio < 0.30:
            reward += 10

        elif inventory_ratio < 0.60:
            reward += 5

        # -----------------------------
        # Last Minute Selling Bonus
        # -----------------------------

        if booking and remaining_days <= 5:
            reward += 10

        # -----------------------------
        # High Price Penalty
        # -----------------------------

        if current_price > 7000:
            reward -= 12

        elif current_price > 6000:
            reward -= 6

        # -----------------------------
        # Unsold Inventory Penalty
        # -----------------------------

        if (
            remaining_days <= 5
            and inventory > 20
        ):
            reward -= 8

        return float(reward)


reward_calculator = RewardCalculator()


def calculate_reward(
    revenue,
    booking,
    inventory,
    remaining_days,
    current_price,
):

    return reward_calculator.calculate_reward(
        revenue,
        booking,
        inventory,
        remaining_days,
        current_price,
    )