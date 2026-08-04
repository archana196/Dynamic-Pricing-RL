import random


class DemandSimulator:
    """
    Simulates customer demand for Dynamic Pricing.

    Demand depends on:
    - Current Price
    - Competitor Price
    - Remaining Booking Days
    - Market Randomness
    """

    def __init__(self):

        self.base_demand = 0.70

    # -------------------------------------------------

    def demand_multiplier(self, remaining_days):
        """
        Demand increases as booking deadline approaches.
        """

        if remaining_days <= 3:
            return 1.30

        elif remaining_days <= 7:
            return 1.15

        elif remaining_days <= 15:
            return 1.00

        return 0.85

    # -------------------------------------------------

    def price_multiplier(self, current_price):
        """
        Lower prices generally attract more bookings.
        """

        if current_price <= 3000:
            return 1.30

        elif current_price <= 4000:
            return 1.15

        elif current_price <= 5000:
            return 1.00

        elif current_price <= 6000:
            return 0.80

        elif current_price <= 7000:
            return 0.60

        return 0.40

    # -------------------------------------------------

    def competitor_multiplier(
        self,
        current_price,
        competitor_price,
    ):
        """
        Compare our price with competitor.
        """

        difference = competitor_price - current_price

        if difference >= 1000:
            return 1.30

        elif difference >= 500:
            return 1.15

        elif difference >= 0:
            return 1.05

        elif difference >= -500:
            return 0.90

        elif difference >= -1000:
            return 0.75

        return 0.60

    # -------------------------------------------------

    def market_noise(self):
        """
        Random market fluctuations.
        """

        return random.uniform(0.90, 1.10)

    # -------------------------------------------------

    def booking_probability(
        self,
        current_price,
        competitor_price,
        remaining_days,
    ):

        probability = (
            self.base_demand
            * self.demand_multiplier(remaining_days)
            * self.price_multiplier(current_price)
            * self.competitor_multiplier(
                current_price,
                competitor_price,
            )
            * self.market_noise()
        )

        probability = max(
            0.05,
            min(probability, 0.98),
        )

        return probability

    # -------------------------------------------------

    def simulate_booking(
        self,
        current_price,
        competitor_price,
        remaining_days,
    ):

        probability = self.booking_probability(
            current_price,
            competitor_price,
            remaining_days,
        )

        booking = random.random() < probability

        return booking, probability


# Singleton
simulator = DemandSimulator()


def simulate_booking(
    current_price,
    competitor_price,
    remaining_days,
):

    return simulator.simulate_booking(
        current_price,
        competitor_price,
        remaining_days,
    )