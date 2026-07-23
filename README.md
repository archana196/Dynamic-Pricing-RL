# 🚀 Dynamic Pricing using Reinforcement Learning (RL)

## 📌 Overview

Dynamic Pricing is a revenue optimization strategy where product or service prices are adjusted based on market conditions such as customer demand, competitor pricing, inventory, and booking windows.

This project implements a **custom Reinforcement Learning environment** using **Gymnasium** for dynamic pricing in the travel and hospitality domain. The environment simulates customer booking behavior, competitor pricing, inventory management, and reward optimization, providing a foundation for training Reinforcement Learning agents such as **Q-Learning** and **Deep Q-Network (DQN)**.

---

# 🎓 Internship Details

**Organization:** Infotact Solutions Pvt. Ltd.

**Internship Domain:** Artificial Intelligence & Machine Learning

**Project Title:** Dynamic Pricing using Reinforcement Learning

**Duration:** 45 Days

---

# 🛠️ Technology Stack

- Python
- Gymnasium
- NumPy
- Pandas
- Flask
- Stable-Baselines3 (Planned)
- Matplotlib

---

# 📂 Project Structure

```
Dynamic-Pricing-RL/
│
├── docs/
│   └── compare_models_results.md
│
├── gym_environment/
│   ├── __init__.py
│   ├── pricing_env.py
│   ├── demand.py
│   └── reward.py
│
├── rl_agent/
│
├── saved_models/
│
├── results/
│
├── compare_models.py
├── test_env.py
├── requirements.txt
└── README.md
```

---

# ✅ Completed Work

## 1. Custom Gymnasium Environment

A custom environment named **DynamicPricingEnv** has been implemented using the Gymnasium framework.

### Features

- Configurable inventory
- Configurable booking window
- Configurable pricing limits
- Dynamic competitor pricing
- Inventory tracking
- Booking tracking
- Revenue calculation
- Episode termination
- Environment reset
- Environment rendering

---

## 2. Observation Space

The environment uses six normalized state variables.

| State | Description |
|--------|-------------|
| Inventory Ratio | Remaining inventory |
| Remaining Days Ratio | Remaining booking window |
| Current Price Ratio | Current selling price |
| Competitor Price Ratio | Competitor pricing |
| Booking Probability | Estimated booking probability |
| Demand Level | Current market demand |

---

## 3. Action Space

The RL agent can perform three pricing actions.

| Action | Description |
|--------|-------------|
| 0 | Decrease Price |
| 1 | Keep Price |
| 2 | Increase Price |

---

## 4. Demand Simulation

A stochastic demand simulator has been implemented.

The booking probability depends on:

- Current Price
- Competitor Price
- Remaining Booking Days
- Market Randomness

The simulator returns:

- Booking Decision
- Booking Probability

---

## 5. Reward Function

A custom reward function has been implemented to encourage long-term revenue optimization.

The reward considers:

- Revenue generated
- Successful bookings
- Inventory utilization
- Remaining booking days
- High-price penalties
- Unsold inventory penalties

Reward shaping helps guide the RL agent toward balanced pricing decisions instead of simply maximizing price.

---

## 6. Environment Testing

The custom environment has been tested using a standalone testing script.

The following components were verified:

- Environment reset
- Observation generation
- State transitions
- Price updates
- Booking simulation
- Revenue calculation
- Reward calculation
- Episode termination

---

## 7. Model Comparison

A comparison framework has been added for evaluating different pricing strategies.

Current comparison includes:

- Fixed Price
- Daily Discount
- Q-Learning (Framework)
- DQN (Framework)

Comparison results are stored separately inside the **docs** directory.

---

## 8. Flask Backend

Basic Flask backend development has been initiated.

Current progress includes:

- Flask application structure
- Route planning
- Backend API planning

---

# 📊 Reinforcement Learning Workflow

```
Reset Environment

↓

Observe Current State

↓

RL Agent Selects Action

↓

Update Price

↓

Demand Simulation

↓

Booking Decision

↓

Revenue Calculation

↓

Reward Calculation

↓

Next State

↓

Episode Ends
```

---

# 📈 Current Project Status

| Module | Status |
|---------|--------|
| Project Planning | ✅ Completed |
| Gymnasium Environment | ✅ Completed |
| Demand Simulation | ✅ Completed |
| Reward Engineering | ✅ Completed |
| Environment Testing | ✅ Completed |
| Model Comparison Framework | ✅ Completed |
| Flask Backend Structure | ✅ In Progress |
| DQN Training | 🔄 Pending |
| Dashboard Development | 🔄 Pending |

---

# 🚀 Future Work

- Train Q-Learning agent
- Train Deep Q-Network (DQN)
- Hyperparameter tuning
- Performance evaluation
- Interactive Flask dashboard
- Visualization of pricing strategies
- Deployment

---

# 👨‍💻 Author

**Ajay Verma**

Artificial Intelligence & Machine Learning Intern

Infotact Solutions Pvt. Ltd.
