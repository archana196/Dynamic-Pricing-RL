# Q-Learning Notes

## Project: AI Dynamic Pricing System using Reinforcement Learning

---

# Introduction

Q-Learning is a model-free Reinforcement Learning (RL) algorithm that enables an agent to learn the best action to take in a given state by interacting with an environment. Instead of relying on labeled data, the agent learns through trial and error by receiving rewards for its actions.

In this project, the Q-Learning agent learns the optimal pricing strategy for hotel rooms or airline tickets. The objective is to maximize the total revenue while ensuring that all available inventory is sold before the booking period ends.

---

# What is Reinforcement Learning?

Reinforcement Learning (RL) is a branch of Machine Learning where an agent learns to make decisions by interacting with an environment.

The learning process follows these steps:

1. Observe the current state.
2. Select an action.
3. Receive a reward.
4. Move to the next state.
5. Repeat until the episode ends.

The agent continuously improves its strategy based on the rewards it receives.

---

# Components of Reinforcement Learning

## Agent

The Agent is the decision-maker.

For this project:

**Agent = Dynamic Pricing AI**

It decides the price to charge for each hotel room or airline ticket.

---

## Environment

The Environment represents the booking system where the agent interacts.

It includes:

- Remaining inventory
- Remaining booking days
- Customer demand
- Purchase probability

---

## State

A State represents the current condition of the environment.

For this project:

```
State = [Remaining Inventory, Days Until Departure]
```

Example:

```
State = [80,15]
```

Meaning:

- 80 rooms are available
- 15 booking days remain

---

## Action

An Action is the pricing decision made by the agent.

Example:

| Action | Price |
|---------|--------|
| 0 | ₹3000 |
| 1 | ₹4000 |
| 2 | ₹5000 |
| 3 | ₹6000 |
| 4 | ₹7000 |

The agent selects one price level during every time step.

---

## Reward

A Reward indicates how good the selected action was.

If a customer purchases:

```
Reward = Selected Price
```

Example:

```
Price = ₹5000

Customer Purchased

Reward = 5000
```

If the customer does not purchase:

```
Reward = 0
```

The objective is to maximize the cumulative reward.

---

## Episode

An Episode represents one complete booking season.

The episode ends when:

- Inventory becomes zero

OR

- Booking days become zero

---

# What is Q-Learning?

Q-Learning is a Reinforcement Learning algorithm that learns the best action for every possible state.

It stores the expected future reward inside a table called the **Q-Table**.

After repeated interactions with the environment, the Q-values become more accurate, allowing the agent to make better pricing decisions.

---

# Q-Table

The Q-Table stores the expected reward for each state-action pair.

Example:

| State | ₹3000 | ₹4000 | ₹5000 | ₹6000 | ₹7000 |
|--------|-------|-------|-------|-------|-------|
| (100,30) | 250 | 320 | 410 | 380 | 300 |
| (80,20) | 280 | 350 | 430 | 400 | 310 |

The agent selects the action with the highest Q-value.

---

# Bellman Equation

The Bellman Equation updates the Q-value after every action.

```
Q(s,a) = Q(s,a) + α [ R + γ max Q(s',a') - Q(s,a) ]
```

Where:

- Q(s,a) = Current Q-value
- α = Learning Rate
- R = Reward
- γ = Discount Factor
- s' = Next State
- a' = Next Action

The Bellman Equation helps the agent improve its decisions after every interaction.

---

# Learning Rate (α)

The Learning Rate determines how much newly learned information replaces old knowledge.

Typical value:

```
α = 0.1
```

Higher value:

- Faster learning
- Less stable

Lower value:

- Slower learning
- More stable

---

# Discount Factor (γ)

The Discount Factor determines the importance of future rewards.

Typical value:

```
γ = 0.95
```

Higher value:

- Considers future rewards

Lower value:

- Focuses on immediate rewards

---

# Exploration vs Exploitation

A Reinforcement Learning agent has two choices.

## Exploration

Try new actions to gain more knowledge.

Example:

Trying a new price of ₹6000 even though it has never been selected before.

---

## Exploitation

Use the action that currently provides the highest reward.

Example:

Choosing ₹5000 because it previously generated the maximum revenue.

A good RL agent balances both exploration and exploitation.

---

# Epsilon-Greedy Strategy

The Epsilon-Greedy strategy balances exploration and exploitation.

Example:

```
ε = 0.1
```

Meaning:

- 10% probability → Explore
- 90% probability → Exploit

Initially, exploration is high.

As training progresses, exploration decreases and exploitation increases.

---

# Advantages of Q-Learning

- Simple to implement
- Does not require labeled data
- Learns through interaction
- Finds an optimal policy over time
- Suitable for discrete state and action spaces

---

# Limitations of Q-Learning

- Large Q-Tables consume more memory.
- Slow learning for large environments.
- Difficult to use with continuous state spaces.
- Performance decreases as the number of states increases.

For large problems, Deep Q-Networks (DQN) are preferred.

---

# Application in Our Project

In this project, the Q-Learning agent will:

- Observe the remaining inventory and remaining booking days.
- Select the best price level.
- Receive revenue as the reward.
- Update the Q-Table using the Bellman Equation.
- Learn an optimal pricing policy over multiple booking seasons.

The trained agent will then be compared with traditional pricing strategies such as Fixed Pricing and Time-Based Pricing.

---

# Summary

| Component | Description |
|-----------|-------------|
| Agent | Dynamic Pricing AI |
| Environment | Hotel/Airline Booking System |
| State | Remaining Inventory, Days Left |
| Action | Select Price Level |
| Reward | Revenue Earned |
| Algorithm | Q-Learning |
| Learning Method | Bellman Equation |
| Goal | Maximize Total Revenue |

---

# Next Steps

- Implement the Q-Learning algorithm.
- Train the agent using the Gymnasium environment.
- Evaluate performance against baseline pricing strategies.
- Upgrade the model to a Deep Q-Network (DQN).
- Integrate the trained model with the Flask dashboard.
