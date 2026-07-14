import random


def customer_purchase_probability(price, remaining_days):
    """
    Calculate customer purchase probability based on:
    - Price
    - Remaining booking days

    Higher price -> Lower probability
    Fewer remaining days -> Higher urgency
    """

    # Base probability based on price
    if price <= 3000:
        base_probability = 0.90
    elif price <= 4000:
        base_probability = 0.75
    elif price <= 5000:
        base_probability = 0.60
    elif price <= 6000:
        base_probability = 0.45
    elif price <= 7000:
        base_probability = 0.30
    else:
        base_probability = 0.15

    # Urgency factor (booking deadline approaching)
    if remaining_days <= 5:
        urgency_bonus = 0.20
    elif remaining_days <= 10:
        urgency_bonus = 0.15
    elif remaining_days <= 20:
        urgency_bonus = 0.08
    else:
        urgency_bonus = 0.00

    probability = base_probability + urgency_bonus

    # Keep probability within valid range
    probability = max(0.05, min(probability, 0.98))

    return probability


def simulate_booking(price, remaining_days):
    """
    Simulate whether a customer books the room.

    Returns:
        True  -> Booking Successful
        False -> No Booking
    """

    probability = customer_purchase_probability(
        price,
        remaining_days
    )

    random_value = random.random()

    return random_value < probability