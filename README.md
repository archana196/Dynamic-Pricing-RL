# 🚀 Dynamic Pricing using Reinforcement Learning (RL)

A custom **Gymnasium-based Reinforcement Learning environment** for Dynamic Pricing in the **Travel & Hospitality** domain. The project simulates customer demand, competitor pricing, inventory management, and reward optimization to provide a foundation for training intelligent pricing agents such as **Q-Learning** and **Deep Q-Network (DQN)**.

---

## 🎓 Internship Details

| Field | Details |
|-------|---------|
| Organization | Infotact Solutions Pvt. Ltd. |
| Domain | Artificial Intelligence & Machine Learning |
| Duration | **60 Days** |
| Project | Dynamic Pricing using Reinforcement Learning |

---

## 👥 Team Members

- **Ajay Verma** – Gymnasium Environment, Testing & Documentation
- **Archana** – Project Lead & RL Model Integration
- **Abhay** – Frontend & Flask Backend

---

## ✨ Features

- Custom Gymnasium Environment
- Dynamic Pricing Simulation
- Observation & Action Space
- Demand Simulation
- Reward Engineering
- Dynamic Competitor Pricing
- Inventory Management
- Revenue Tracking
- Environment Testing
- Model Comparison Framework
- Flask Backend (In Progress)

---

## 🛠️ Tech Stack

- Python
- Gymnasium
- NumPy
- Pandas
- Flask
- Matplotlib
- Stable-Baselines3 *(Planned)*

---

## 📂 Project Structure

```text
Dynamic-Pricing-RL/

├── docs/
├── gym_environment/
│   ├── pricing_env.py
│   ├── demand.py
│   ├── reward.py
│   └── __init__.py
│
├── results/
├── rl_agent/
├── saved_models/
├── static/
├── templates/
│
├── app.py
├── compare_models.py
├── test_env.py
├── requirements.txt
└── README.md
```

---

## 🏗️ Environment Design

### Observation Space

- Inventory Ratio
- Remaining Days Ratio
- Current Price Ratio
- Competitor Price Ratio
- Booking Probability
- Demand Level

### Action Space

| Action | Description |
|--------|-------------|
| 0 | Decrease Price |
| 1 | Keep Price |
| 2 | Increase Price |

---

## 🔄 Workflow

```text
Reset Environment
        ↓
Observe State
        ↓
Select Action
        ↓
Update Price
        ↓
Demand Simulation
        ↓
Booking Decision
        ↓
Reward Calculation
        ↓
Next State
        ↓
Episode Ends
```
## 📚 Documentation

Detailed documentation is available in the **docs/** folder.

- Project Documentation
- Environment Test Report
- Model Comparison Results
- Implementation Summary

---

## 🚀 Future Work

- Train Q-Learning Agent
- Train Deep Q-Network (DQN)
- Hyperparameter Tuning
- Interactive Flask Dashboard
- Performance Evaluation
- Deployment

---

## 👨‍💻 Author

**Ajay Verma**

Artificial Intelligence & Machine Learning Intern

**Infotact Solutions Pvt. Ltd.**

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.
