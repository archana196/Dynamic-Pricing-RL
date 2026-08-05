# Dynamic Pricing using Reinforcement Learning

## Overview

Dynamic pricing is a pricing strategy where the price of a product or service changes based on factors such as demand, inventory, time, and market conditions. Industries like airlines, hotels, and online booking platforms use dynamic pricing to maximize revenue while efficiently utilizing available inventory.

This project implements a **Reinforcement Learning (RL)** based Dynamic Pricing System for the Travel & Hospitality domain. A custom Gymnasium environment simulates the booking process, and an RL agent learns the optimal pricing strategy through continuous interaction with the environment. The project compares traditional pricing strategies with Q-Learning and Deep Q-Network (DQN) algorithms to identify the most effective pricing policy.

---

# Problem Statement

Static pricing strategies fail to adapt to changing customer demand, competitor pricing, and limited inventory. This often leads to either unsold inventory or selling inventory too early at suboptimal prices.

The objective of this project is to build an autonomous pricing agent that learns optimal pricing decisions to maximize revenue while efficiently managing available inventory.

---

# Objectives

* Design a custom Gymnasium environment for dynamic pricing.
* Implement baseline pricing strategies.
* Develop a Q-Learning agent.
* Implement a Deep Q-Network (DQN) agent.
* Compare different pricing strategies.
* Evaluate model performance using multiple simulation episodes.
* Visualize evaluation results through graphs.
* Integrate the results into a Flask dashboard.

---

# Features

* Custom Gymnasium environment
* Dynamic pricing simulation
* Baseline pricing strategies
* Q-Learning implementation
* Deep Q-Network (DQN)
* Experience Replay Buffer
* Epsilon-Greedy Exploration
* Automated model evaluation
* Performance comparison
* CSV-based result generation
* Performance visualization
* Flask dashboard integration

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

# Project Structure

```text
Dynamic-Pricing-RL/
│
├── gym_environment/
│   ├── pricing_env.py
│   └── demand_simulator.py
│
├── rl_agent/
│   ├── q_learning.py
│   ├── dqn_agent.py
│   ├── replay_buffer.py
│   ├── network.py
│   ├── train.py
│   ├── train_dqn.py
│   ├── evaluate_dqn.py
│   └── plot_results.py
│
├── saved_models/
│   ├── q_table.npy
│   └── dqn_model.pth
│
├── results/
│   ├── evaluation_results.csv
│   ├── model_comparison.csv
│   └── price_trajectory.csv
│
├── graphs/
│   ├── revenue_vs_episode.png
│   ├── reward_vs_episode.png
│   ├── bookings_vs_episode.png
│   └── inventory_vs_episode.png
│
├── templates/
├── static/
├── compare_models.py
├── app.py
├── requirements.txt
└── README.md
```

---

# Reinforcement Learning Workflow

1. Initialize the booking environment.
2. Observe the current state.
3. Select a pricing action.
4. Simulate customer demand.
5. Calculate reward based on revenue.
6. Update the learning model.
7. Repeat for multiple booking seasons.
8. Evaluate model performance.
9. Compare pricing strategies.
10. Display results through graphs and dashboard.

---

# State Space

The RL agent makes decisions using:

* Remaining Inventory
* Remaining Days
* Current Price
* Competitor Price
* Demand Level
* Booking Probability

---

# Action Space

The agent can perform three actions:

* Decrease Price
* Keep Price
* Increase Price

---

# Reward Function

The reward is calculated based on the revenue generated after each pricing decision. The objective of the agent is to maximize cumulative reward while minimizing unsold inventory.

---

# Pricing Strategies Compared

* Fixed Price
* Daily Discount
* Q-Learning
* Deep Q-Network (DQN)

Comparison results are stored in:

```
results/model_comparison.csv
```

---

# Model Evaluation

The trained DQN model is evaluated over **1000 simulation episodes**.

Performance metrics include:

* Average Revenue
* Average Reward
* Average Bookings
* Average Remaining Inventory

Evaluation results are stored in:

```
results/evaluation_results.csv
```

---

# Generated Outputs

### Saved Models

* `saved_models/q_table.npy`
* `saved_models/dqn_model.pth`

### Result Files

* `evaluation_results.csv`
* `model_comparison.csv`
* `price_trajectory.csv`

### Graphs

* Revenue vs Episode
* Reward vs Episode
* Bookings vs Episode
* Remaining Inventory vs Episode

---

# How to Run the Project

### Clone the Repository

```bash
git clone <repository-url>
cd Dynamic-Pricing-RL
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Q-Learning Model

```bash
python -m rl_agent.train
```

### Train the DQN Model

```bash
python -m rl_agent.train_dqn
```

### Evaluate the DQN Model

```bash
python -m rl_agent.evaluate_dqn
```

### Generate Performance Graphs

```bash
python -m rl_agent.plot_results
```

### Compare Pricing Strategies

```bash
python compare_models.py
```

### Run the Flask Dashboard

```bash
python app.py
```

---

# Results

The Reinforcement Learning models learn pricing strategies that adapt to changing booking conditions. Performance is evaluated using multiple simulation episodes, and comparison with baseline pricing strategies demonstrates the effectiveness of Reinforcement Learning for dynamic pricing.


# Future Enhancements

* Real-time hotel and airline booking data integration
* Live competitor pricing analysis
* Advanced Reinforcement Learning algorithms (PPO, A3C)
* Cloud deployment
* Multi-property pricing optimization
* Interactive analytics dashboard
* Real-time demand forecasting

---

# Conclusion

This project demonstrates the application of Reinforcement Learning to solve real-world dynamic pricing problems in the travel and hospitality industry. By combining Q-Learning, Deep Q-Networks, evaluation analytics, and dashboard visualization, the system provides an intelligent pricing solution capable of maximizing revenue while efficiently managing inventory.
