# 📊 Model Comparison Results

## Overview

To evaluate the effectiveness of different pricing strategies, four approaches were tested in the Dynamic Pricing Reinforcement Learning environment over **1000 evaluation episodes**.

The objective of this comparison was to identify the strategy that maximizes revenue, increases successful bookings, and achieves the highest cumulative reward while adapting to changing market conditions.

---

## Evaluated Strategies

| Strategy | Description |
|----------|-------------|
| **Fixed Price** | Keeps the product price constant throughout the booking period without any adjustments. |
| **Daily Discount** | Applies a simple rule-based pricing strategy by reducing the price during the final booking days to increase demand. |
| **Q-Learning** | Uses a tabular reinforcement learning algorithm with a discretized state space to learn pricing decisions. |
| **Deep Q-Network (DQN)** | Uses a Deep Neural Network to approximate the optimal Q-values and make adaptive pricing decisions in continuous state spaces. |

---

# Evaluation Metrics

The following metrics were used to compare each strategy:

- **Average Revenue** – Total revenue generated per episode.
- **Average Reward** – Average cumulative reinforcement learning reward.
- **Average Bookings** – Average number of successful bookings per episode.

---

# Experimental Results

| Strategy | Average Revenue (₹) | Average Reward | Average Bookings |
|----------|--------------------:|---------------:|-----------------:|
| Fixed Price | 103,990.00 | 846.76 | 20.80 |
| Daily Discount | 96,503.50 | 849.41 | 21.93 |
| Q-Learning | 95,408.50 | 898.71 | 23.80 |
| **Deep Q-Network (DQN)** | **108,045.00** | **1065.99** | **27.25** |

---

# Best Performing Strategy

| Metric | Best Strategy | Value |
|---------|---------------|------:|
| Highest Revenue | **DQN** | ₹108,045.00 |
| Highest Reward | **DQN** | 1065.99 |
| Highest Bookings | **DQN** | 27.25 |

---

# Performance Analysis

### Fixed Price

The Fixed Price strategy maintains the same price throughout the booking window. Although simple to implement, it cannot adapt to changes in demand, competitor pricing, or booking urgency. As a result, its performance remains moderate.

---

### Daily Discount

The Daily Discount strategy lowers prices during the final booking days to encourage additional bookings. While this increases booking frequency slightly, the lower selling prices reduce overall revenue, making it less effective than adaptive reinforcement learning methods.

---

### Q-Learning

The Q-Learning agent learns pricing policies using a discretized state representation. It achieves higher rewards and booking counts than the rule-based strategies but is limited by the size of its Q-table and reduced ability to generalize across unseen states.

---

### Deep Q-Network (DQN)

The Deep Q-Network consistently outperformed all other strategies across every evaluation metric. By approximating the action-value function using a neural network, DQN effectively learns dynamic pricing policies for continuous state spaces. It generated the highest revenue, accumulated the largest rewards, and achieved the greatest number of successful bookings.

---

# Overall Ranking

| Rank | Strategy |
|------|----------|
| 🥇 1 | Deep Q-Network (DQN) |
| 🥈 2 | Fixed Price |
| 🥉 3 | Daily Discount |
| 4 | Q-Learning |

---

# Conclusion

The experimental evaluation demonstrates that **Deep Q-Network (DQN)** is the most effective pricing strategy among all evaluated approaches.

Compared with rule-based pricing methods and tabular reinforcement learning, DQN achieved:

- Highest average revenue
- Highest cumulative reward
- Highest average bookings
- Better adaptability to changing market conditions
- More effective dynamic pricing decisions

These results highlight the advantage of Deep Reinforcement Learning for solving dynamic pricing problems where demand, competitor pricing, and booking urgency continuously change.

---

# Output Files

The evaluation process automatically generates the following output:

```text
results/
└── model_comparison.csv
```

The CSV file contains the average performance of all evaluated pricing strategies and can be used for further visualization, reporting, or analysis.

---

# Evaluation Configuration

| Parameter | Value |
|-----------|------:|
| Environment | Dynamic Pricing RL Environment |
| Total Episodes | 1000 |
| Action Space | 3 Actions (Decrease, Maintain, Increase Price) |
| State Representation | 6-dimensional normalized state |
| Evaluation Mode | No Exploration (ε = 0) |
| Compared Strategies | Fixed Price, Daily Discount, Q-Learning, DQN |

---

## Final Observation

The evaluation confirms that **Deep Q-Network (DQN)** provides the most robust and profitable pricing strategy for the Dynamic Pricing Reinforcement Learning environment, making it the recommended model for deployment in intelligent revenue management systems.