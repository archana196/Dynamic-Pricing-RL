def calculate_reward(revenue, booking_success):
    """
    Calculate reward for the RL agent.

    Parameters
    ----------
    revenue : float
        Revenue earned from booking.

    booking_success : bool
        Whether booking was successful.

    Returns
    -------
    float
        Reward value.
    """

    reward = 0.0

    # Revenue-based reward
    reward += revenue / 100.0

    # Bonus for successful booking
    if booking_success:
        reward += 20

        # Extra bonus for high revenue
        if revenue >= 6000:
            reward += 15
        elif revenue >= 5000:
            reward += 10
        elif revenue >= 4000:
            reward += 5

    else:
        # Penalty if no booking
        reward -= 15

    return reward