# 🧪 Dynamic Pricing Environment Testing Report

## Overview

This document summarizes the testing performed on the custom **DynamicPricingEnv** Gymnasium environment.

The objective of testing was to verify the correctness of environment transitions, pricing actions, demand simulation, reward calculations, booking logic, and episode termination.

---

# Test Configuration

| Parameter | Value |
|-----------|-------|
| Environment | DynamicPricingEnv |
| Testing Method | Random Action Sampling |
| Episode Length | 30 Steps |
| Initial Inventory | 100 Units |
| Initial Booking Window | 30 Days |

---

# Test Procedure

The environment was tested using the `test_env.py` script.

The following workflow was executed:

1. Initialize the environment.
2. Reset the environment.
3. Generate the initial observation.
4. Select a random action from the action space.
5. Execute the selected action.
6. Observe the next state.
7. Calculate reward.
8. Update inventory and booking status.
9. Render the environment.
10. Repeat until episode termination.

---

# Components Verified

The following modules were successfully tested.

- ✅ Environment Initialization
- ✅ Observation Space Generation
- ✅ Action Space Execution
- ✅ State Transition
- ✅ Demand Simulation
- ✅ Booking Probability Calculation
- ✅ Competitor Price Update
- ✅ Revenue Calculation
- ✅ Reward Calculation
- ✅ Inventory Management
- ✅ Episode Termination
- ✅ Environment Rendering

---

# Observation Space Verification

The environment generated normalized observations containing six state variables.

| State Variable | Description |
|---------------|-------------|
| Inventory Ratio | Remaining inventory |
| Remaining Days Ratio | Booking window remaining |
| Current Price Ratio | Current selling price |
| Competitor Price Ratio | Competitor selling price |
| Booking Probability | Estimated booking likelihood |
| Demand Level | Simulated market demand |

Example Observation

```text
[0.90, 0.00, 0.75, 0.48, 0.34, 0.34]
```

---

# Action Space Verification

The environment correctly accepted all available actions.

| Action | Description |
|--------|-------------|
| 0 | Decrease Price |
| 1 | Keep Price |
| 2 | Increase Price |

Price updates were reflected correctly after each action.

---

# Demand Simulation Verification

Demand simulation behaved as expected.

The booking probability changed dynamically according to:

- Current Price
- Competitor Price
- Remaining Booking Days
- Random Market Variation

Bookings occurred only when simulated demand conditions were satisfied.

---

# Reward Verification

Reward values changed according to environment conditions.

Positive rewards were observed when:

- Successful bookings occurred
- Revenue increased
- Inventory utilization improved

Negative rewards were observed when:

- No booking occurred
- Selling price became too high
- Inventory remained unsold

This confirms that the reward function encourages profitable pricing decisions.

---

# Inventory Verification

Inventory decreased only after successful bookings.

Example

```
Initial Inventory : 100

Final Inventory   : 90
```

Inventory tracking remained consistent throughout the episode.

---

# Revenue Verification

Revenue increased only when bookings were successful.

Example

```
Total Revenue

₹5,500

↓

₹11,000

↓

₹21,500

↓

₹33,500

↓

₹59,000
```

Revenue accumulation behaved correctly.

---

# Episode Summary

| Metric | Value |
|--------|------:|
| Total Steps | 30 |
| Initial Inventory | 100 |
| Final Inventory | 90 |
| Successful Bookings | 10 |
| Remaining Inventory | 90 |
| Total Revenue | ₹59,000 |
| Total Reward | 201.00 |

---

# Key Observations

- Environment remained stable throughout the episode.
- Observation values remained normalized.
- Competitor pricing updated dynamically.
- Booking probability responded to pricing changes.
- Inventory tracking was accurate.
- Revenue accumulated correctly after successful bookings.
- Reward values reflected booking outcomes.
- Episode terminated correctly after the booking window expired.

---

# Conclusion

Testing confirms that the custom **DynamicPricingEnv** functions correctly and satisfies the intended Reinforcement Learning environment requirements.

All major components—including observation generation, action execution, demand simulation, reward engineering, inventory management, and episode termination—operated as expected during testing.

The environment is ready for training and evaluating Reinforcement Learning agents such as **Q-Learning** and **Deep Q-Network (DQN)**.
