# 📘 Project Documentation

## Project Overview

This document provides a comprehensive overview of the **Dynamic Pricing using Reinforcement Learning (RL)** project developed during the Artificial Intelligence & Machine Learning Internship at **Infotact Solutions Pvt. Ltd.**

The objective of this project is to simulate a dynamic pricing environment for the travel and hospitality industry using Reinforcement Learning. A custom Gymnasium environment was developed to model pricing decisions, customer demand, inventory management, and reward optimization.

---

# Project Architecture

The project consists of the following major components:

- Custom Gymnasium Environment
- Demand Simulation Module
- Reward Engineering Module
- Reinforcement Learning Agent
- Model Comparison Module
- Testing & Verification
- Flask Backend (In Progress)

---

# Project Workflow

```
Project Planning
        │
        ▼
Environment Design
        │
        ▼
Observation Space Design
        │
        ▼
Action Space Design
        │
        ▼
Demand Simulation
        │
        ▼
Reward Engineering
        │
        ▼
Environment Testing
        │
        ▼
Model Comparison
        │
        ▼
Documentation
```

---

# Environment Design

A custom Gymnasium environment named **DynamicPricingEnv** was developed.

## Observation Space

The environment returns six normalized state variables.

| State | Description |
|--------|-------------|
| Inventory Ratio | Remaining inventory |
| Remaining Days Ratio | Remaining booking days |
| Current Price Ratio | Current selling price |
| Competitor Price Ratio | Competitor price |
| Booking Probability | Estimated booking probability |
| Demand Level | Current demand intensity |

---

## Action Space

The agent can perform three pricing actions.

| Action | Description |
|--------|-------------|
| 0 | Decrease Price |
| 1 | Keep Price |
| 2 | Increase Price |

---

# Demand Simulation

Customer demand is simulated using multiple pricing factors.

Demand depends on

- Current Price
- Competitor Price
- Remaining Booking Days
- Market Randomness

The simulator estimates booking probability and generates realistic booking decisions for every environment step.

---

# Reward Engineering

The reward function is designed to maximize long-term revenue instead of short-term profit.

Reward considers

- Revenue generated
- Successful bookings
- Inventory utilization
- Remaining booking days
- High price penalty
- Unsold inventory penalty

This reward shaping encourages balanced pricing strategies.

---

# Environment Testing

The environment was tested after implementation.

The following components were verified.

- Environment Reset
- Observation Generation
- State Transition
- Price Update
- Demand Simulation
- Reward Calculation
- Revenue Calculation
- Inventory Update
- Booking Update
- Episode Termination

Testing confirmed that all core modules function correctly.

---

# Model Comparison

The project includes a comparison framework for evaluating multiple pricing strategies.

| Strategy | Revenue | Reward | Bookings |
|----------|---------:|--------:|---------:|
| Fixed Price | 103990.0 | 846.7600 | 20.798 |
| Daily Discount | 96503.5 | 849.4075 | 21.932 |
| Q-Learning | 95408.5 | 898.7065 | 23.797 |
| Deep Q-Network (DQN) | **108045.0** | **1065.9850** | **27.246** |

---

# Performance Summary

### Fixed Price

- Simple pricing policy
- Stable revenue
- No adaptation to market conditions

### Daily Discount

- Improves occupancy
- Lower overall revenue due to continuous discounts

### Q-Learning

- Learns pricing strategy from experience
- Better booking performance than rule-based methods

### Deep Q-Network (DQN)

- Highest revenue
- Highest cumulative reward
- Highest booking rate
- Best adaptability to changing market conditions

---

# Verification Report

The following modules were verified successfully.

- pricing_env.py
- demand.py
- reward.py
- compare_models.py
- model_comparison.csv
- README.md

Verification confirmed

- Correct observation space
- Correct action space
- Stable reward calculation
- Proper environment reset
- Correct episode termination
- Logical booking simulation
- Correct revenue calculation

No major runtime issues were identified during verification.

---

# Folder Structure

```
Dynamic-Pricing-RL/

├── docs/
├── gym_environment/
│   ├── pricing_env.py
│   ├── demand.py
│   └── reward.py
│
├── rl_agent/
├── saved_models/
├── results/
├── compare_models.py
├── test_env.py
├── README.md
└── requirements.txt
```

---

# Technologies Used

- Python
- Gymnasium
- NumPy
- Pandas
- Flask
- Stable-Baselines3
- Matplotlib
- Reinforcement Learning

---

# Current Status

| Module | Status |
|---------|--------|
| Project Planning | ✅ Completed |
| Environment Design | ✅ Completed |
| Gymnasium Environment | ✅ Completed |
| Demand Simulation | ✅ Completed |
| Reward Engineering | ✅ Completed |
| Environment Testing | ✅ Completed |
| Model Comparison | ✅ Completed |
| Documentation | ✅ Completed |
| Flask Backend | 🔄 In Progress |

---

# Future Improvements

- Hyperparameter tuning
- Additional RL algorithms (PPO, SAC)
- Real-world hotel datasets
- Seasonal demand modeling
- Holiday-aware pricing
- Interactive analytics dashboard
- Cloud deployment
- REST API integration

---

# Conclusion

This project successfully demonstrates the application of Reinforcement Learning to dynamic pricing. A custom Gymnasium environment was developed to simulate pricing decisions, customer demand, inventory utilization, and revenue optimization.

The implemented demand simulation, reward engineering, testing framework, and model comparison provide a solid foundation for intelligent pricing systems. Among the evaluated strategies, the **Deep Q-Network (DQN)** achieved the highest revenue, cumulative reward, and booking performance in the current implementation, indicating its effectiveness for the simulated dynamic pricing environment.

---

# Author

**Ajay Verma**

Artificial Intelligence & Machine Learning Intern

**Infotact Solutions Pvt. Ltd.**
