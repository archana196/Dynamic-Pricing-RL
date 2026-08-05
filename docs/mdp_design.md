# Dynamic Pricing as a Markov Decision Process (MDP)

## Project Overview

The objective of this project is to build an AI-powered Dynamic Pricing System for the travel and hospitality industry using Reinforcement Learning (RL). The RL agent will learn the optimal pricing strategy by interacting with a simulated market environment. The goal is to maximize total revenue while ensuring that all available inventory (hotel rooms or airline seats) is sold before the booking period ends.

---

# Markov Decision Process (MDP)

The Dynamic Pricing problem can be modeled as a Markov Decision Process (MDP), where an intelligent agent learns the best pricing strategy through continuous interaction with the environment.

---

## Agent

The Agent is the Reinforcement Learning model responsible for selecting the best price level at every time step to maximize total revenue.

Example:
- Q-Learning Agent
- Deep Q-Network (DQN) Agent

---

## Environment

The Environment represents the simulated hotel or airline booking system. It receives the price selected by the agent and determines whether customers purchase based on market demand.

The environment maintains:
- Remaining inventory
- Days remaining until departure
- Customer demand
- Revenue generated

---

## State

The State represents the current status of the booking process.

For this project, the state is defined as:

```
State = [Remaining Inventory, Days Until Departure]
```

Example:

```
State = [80, 15]

Remaining Inventory = 80
Days Until Departure = 15
```

The RL agent observes this state before making every pricing decision.

---

## Action

The Action is the price selected by the RL agent.

Initially, the pricing decisions are represented as discrete price levels.

Example:

| Action | Price |
|--------|--------|
| 0 | ₹3000 |
| 1 | ₹4000 |
| 2 | ₹5000 |
| 3 | ₹6000 |
| 4 | ₹7000 |

At every time step, the agent chooses one action.

---

## Reward

The Reward measures the success of the selected pricing strategy.

If a customer purchases the ticket or room,

```
Reward = Selected Price
```

Example:

```
Selected Price = ₹5000

Customer Purchased

Reward = 5000
```

If no customer purchases,

```
Reward = 0
```

The objective is to maximize the cumulative reward over the entire booking season.

---

## Transition

After selecting a price,

- Remaining inventory may decrease if a purchase occurs.
- Days remaining decrease by one.
- The environment moves to the next state.

Example:

Current State

```
[80,15]
```

Action

```
Price = ₹5000
```

Next State

```
[79,14]
```

---

## Episode

One Episode represents one complete booking season.

The episode terminates when either:

```
Remaining Inventory = 0
```

OR

```
Days Until Departure = 0
```

---

## Objective

The objective of the RL agent is to learn an optimal pricing policy that maximizes total revenue throughout the booking season while efficiently selling the available inventory.

Mathematically,

```
Maximize Total Revenue
```

---

## Summary

| Component | Description |
|-----------|-------------|
| Agent | Q-Learning / DQN Agent |
| Environment | Simulated Hotel/Airline Booking System |
| State | Remaining Inventory, Days Until Departure |
| Action | Select Price Level |
| Reward | Revenue Earned |
| Episode Ends | Inventory Sold Out or Days Reach Zero |
| Goal | Maximize Total Revenue |

---

## Next Steps

- Design the custom Gymnasium environment.
- Implement the stochastic demand function.
- Develop the Q-Learning agent.
- Upgrade the agent to a Deep Q-Network (DQN).
- Compare RL performance with baseline pricing strategies.
- Integrate the trained model into the Flask dashboard.
