# Dynamic Pricing using Reinforcement Learning

## Project Overview

Dynamic pricing is a strategy used in industries such as airlines, hotels, and online booking platforms to maximize revenue by adjusting prices based on changing market conditions. Traditional fixed-price methods cannot effectively respond to variations in customer demand, remaining inventory, or booking time.

This project implements a Reinforcement Learning (RL) based Dynamic Pricing System that learns optimal pricing strategies through interaction with a simulated booking environment. The agent aims to maximize total revenue while minimizing unsold inventory.

---

# Objectives

* Develop a custom Gymnasium environment for hotel/airline booking simulation.
* Implement Q-Learning as the baseline reinforcement learning algorithm.
* Implement a Deep Q-Network (DQN) for improved decision-making.
* Compare DQN with traditional pricing strategies.
* Evaluate the trained models over multiple simulated booking seasons.
* Visualize model performance using graphs and analytics.

---

# Features

* Custom Gymnasium environment
* Dynamic pricing simulation
* Q-Learning implementation
* Deep Q-Network (DQN)
* Experience Replay Buffer
* Epsilon-Greedy Exploration
* Automated model evaluation
* Performance comparison with baseline strategies
* CSV result generation
* Performance visualization
* Flask-based dashboard integration

---

# Project Structure

```text
Dynamic-Pricing-RL/
│
├── gym_environment/
├── rl_agent/
├── saved_models/
├── results/
├── graphs/
├── templates/
├── static/
├── docs/
│
├── compare_models.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* Gymnasium
* PyTorch
* NumPy
* Pandas
* Matplotlib
* Flask
* Git & GitHub

---

# Reinforcement Learning Workflow

1. Initialize the booking environment.
2. Observe the current state.
3. Select a pricing action using the RL agent.
4. Simulate customer demand.
5. Calculate reward based on revenue.
6. Update the learning model.
7. Repeat for multiple booking seasons.
8. Evaluate performance and generate analytics.

---

# State Space

The RL agent considers the following information:

* Remaining Inventory
* Remaining Days
* Current Price
* Competitor Price
* Demand Level
* Booking Probability

---

# Action Space

The agent can perform three pricing actions:

* Decrease Price
* Keep Price
* Increase Price

---

# Reward Function

The reward is based on revenue generated during the booking process. The RL agent learns to maximize cumulative reward while ensuring efficient inventory utilization.

---

# Model Comparison

The project compares the following pricing strategies:

* Fixed Price
* Daily Discount
* Q-Learning
* Deep Q-Network (DQN)

The comparison results are stored in:

```text
results/model_comparison.csv
```

---

# Evaluation

The trained DQN model is evaluated over 1000 simulated booking seasons.

The following metrics are collected:

* Average Revenue
* Average Reward
* Average Bookings
* Average Remaining Inventory

Results are stored in:

```text
results/evaluation_results.csv
```

---

# Generated Outputs

## Saved Models

* `saved_models/q_table.npy`
* `saved_models/dqn_model.pth`

## Result Files

* `evaluation_results.csv`
* `model_comparison.csv`
* `price_trajectory.csv`

## Graphs

* Revenue vs Episode
* Reward vs Episode
* Bookings vs Episode
* Remaining Inventory vs Episode

---



---

# Future Scope

* Real-time booking data integration
* Live competitor pricing
* Advanced RL algorithms (e.g., PPO)
* Cloud deployment
* Multi-hotel pricing optimization
* Real-time business dashboard

---

# Conclusion

This project demonstrates how Reinforcement Learning can be applied to solve real-world dynamic pricing problems. By learning from continuous interaction with a simulated booking environment, the DQN agent can make intelligent pricing decisions that improve revenue compared to traditional pricing strategies.
