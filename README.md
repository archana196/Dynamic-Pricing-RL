# Dynamic Pricing using Reinforcement Learning

## Overview

Dynamic pricing is a pricing strategy where the price of a product or service changes based on real-time factors such as demand, inventory, time, and market conditions. Industries like airlines, hotels, and online booking platforms use dynamic pricing to maximize revenue while efficiently utilizing available inventory.

This project implements a **Reinforcement Learning (RL)** based Dynamic Pricing System for the **Travel & Hospitality domain**. A custom Gymnasium environment simulates the booking process, and an RL agent learns the optimal pricing strategy through continuous interaction with the environment. The project compares traditional pricing strategies with **Q-Learning** and **Deep Q-Network (DQN)** algorithms to identify the most effective pricing policy.

---

## Problem Statement

Static pricing strategies fail to adapt to changing customer demand, competitor pricing, and limited inventory. This often leads to either unsold inventory or selling inventory too early at suboptimal prices.

The objective of this project is to build an **autonomous pricing agent** that learns optimal pricing decisions to maximize revenue while efficiently managing available inventory over a 30-day booking window.

---

## Objectives

- Design a custom Gymnasium environment for dynamic pricing simulation.
- Implement baseline pricing strategies (Fixed Price, Daily Discount).
- Develop a tabular Q-Learning agent.
- Implement a Deep Q-Network (DQN) agent using PyTorch.
- Compare all pricing strategies across 1000 simulation episodes.
- Evaluate model performance using multiple metrics (revenue, reward, bookings).
- Visualize evaluation results through performance graphs.
- Integrate results into a Flask web dashboard.

---

## Features

- **Custom Gymnasium Environment** — Simulates a real-world hotel/airline booking scenario
- **Dynamic Pricing Simulation** — Prices adjust based on demand, inventory, and competition
- **Demand Simulator** — Multi-factor demand modeling (price, competitor, urgency, noise)
- **Reward Shaping** — Custom reward function encouraging revenue maximization and inventory efficiency
- **Baseline Strategies** — Fixed Price and Daily Discount for performance benchmarking
- **Q-Learning Agent** — Tabular RL with state discretization and epsilon-greedy exploration
- **DQN Agent** — Neural network-based RL with experience replay and target network
- **Experience Replay Buffer** — Stores and samples past transitions (capacity: 10,000)
- **Epsilon-Greedy Exploration** — Balances exploration vs. exploitation during training
- **Target Network** — Stabilizes DQN training (updated every 20 episodes)
- **Model Evaluation** — 1000-episode evaluation with detailed metrics
- **Performance Comparison** — Side-by-side comparison of all four strategies
- **CSV-Based Result Generation** — Structured output for downstream analysis
- **Performance Visualization** — Graphs for revenue, reward, bookings, and inventory
- **Flask Web Dashboard** — Interactive web interface for exploring results

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Gymnasium | Custom RL environment framework |
| PyTorch | Deep Q-Network implementation |
| NumPy | Numerical computations and array operations |
| Pandas | Data manipulation and CSV handling |
| Matplotlib | Performance graph generation |
| Flask | Web dashboard and REST API |
| Git & GitHub | Version control |

---

## Project Structure

```
Dynamic-Pricing-RL/
|
|-- gym_environment/
|   |-- __init__.py
|   |-- pricing_env.py          # Custom Gymnasium environment
|   |-- demand.py               # Multi-factor demand simulator
|   `-- reward.py               # Reward shaping and calculation
|
|-- rl_agent/
|   |-- __init__.py
|   |-- q_learning.py           # Tabular Q-Learning agent
|   |-- dqn_agent.py            # Deep Q-Network agent
|   |-- neural_network.py       # DQN network architecture (6->64->64->3)
|   |-- replay_buffer.py        # Experience replay buffer (capacity=10000)
|   |-- train.py                # Q-Learning training loop (1000 episodes)
|   |-- train_dqn.py            # DQN training loop (1000 episodes)
|   |-- plot_results.py         # Performance graph generation
|   |-- dqn.py                  # DQN module entry point
|   |-- network.py              # Network module alias
|   `-- utils.py                # Utility functions
|
|-- flask_app/
|   |-- app.py                  # Flask app with all route definitions
|   |-- routes.py               # Additional route handlers
|   |-- static/
|   |   `-- css/
|   |       `-- style.css       # Dashboard stylesheet
|   `-- templates/
|       |-- base.html           # Base layout template
|       |-- index.html          # Home / landing page
|       |-- dashboard.html      # Key metrics dashboard
|       |-- simulation.html     # Episode simulation results
|       |-- comparison.html     # Strategy comparison page
|       |-- graphs.html         # Performance graphs page
|       `-- results.html        # Detailed results page
|
|-- baseline/
|   |-- __init__.py
|   |-- fixed_price.py          # Fixed price baseline strategy
|   |-- daily_discount.py       # Daily discount baseline strategy
|   `-- evaluate_baselines.py   # Baseline evaluation script
|
|-- saved_models/
|   |-- q_table.npy             # Trained Q-Learning table
|   `-- dqn_model.pth           # Trained DQN model weights
|
|-- results/
|   |-- evaluation_results.csv  # DQN evaluation output (1000 episodes)
|   |-- model_comparison.csv    # Side-by-side strategy comparison
|   `-- price_trajectory.csv    # Price decision history
|
|-- graphs/
|   |-- revenue_vs_episode.png
|   |-- reward_vs_episode.png
|   |-- bookings_vs_episode.png
|   `-- inventory_vs_episode.png
|
|-- docs/
|   |-- mdp_design.md
|   |-- q_learning_notes.md
|   |-- project_documentation.md
|   |-- compare_models_results.md
|   |-- Sprint4_Report.md
|   |-- environment_interface.md
|   |-- evaluation_metrics.md
|   |-- implementation_summary.md
|   |-- rl_environment.md
|   `-- test_env.md
|
|-- compare_models.py           # Compares all 4 pricing strategies
|-- evaluate_dqn.py             # Standalone DQN evaluation script
|-- test_env.py                 # Environment sanity tests
|-- requirements.txt            # Python dependencies
|-- interview.md                # Interview preparation guide
|-- .gitignore
`-- README.md
```

---

## Environment Design

### State Space

The agent observes a **6-dimensional normalized state vector** (all values in `[0, 1]`):

| Feature | Description |
|---|---|
| `inventory_ratio` | Remaining inventory / max inventory (100) |
| `remaining_days_ratio` | Days left / total booking window (30) |
| `current_price_ratio` | Normalized current price in [₹2000, ₹8000] |
| `competitor_price_ratio` | Normalized competitor price in [₹2000, ₹8000] |
| `booking_probability` | Probability of a booking occurring this step |
| `demand_level` | Current demand level (mirrors booking probability) |

### Action Space

The agent selects from **3 discrete actions** each time step (day):

| Action | Description | Price Change |
|---|---|---|
| `0` | Decrease Price | −₹500 |
| `1` | Keep Price | ±₹0 |
| `2` | Increase Price | +₹500 |

Prices are clipped to stay within `[₹2,000, ₹8,000]`.

### Reward Function

The reward is shaped to encourage multiple desired behaviors simultaneously:

| Condition | Reward |
|---|---|
| Revenue generated | `+revenue / 200.0` |
| Successful booking | `+20` |
| No booking | `−10` |
| Low inventory (< 30%) | `+10` |
| Medium inventory (< 60%) | `+5` |
| Last-minute booking (≤ 5 days) | `+10` |
| Price > ₹7,000 | `−12` |
| Price > ₹6,000 | `−6` |
| End-of-window with >20 unsold | `−8` |

### Demand Simulation

Booking probability is computed using a **multiplicative multi-factor model**:

```
P(booking) = base_demand × price_multiplier × demand_multiplier × competitor_multiplier × market_noise
```

- **Base demand**: 0.70
- **Price multiplier**: 1.30 (≤₹3000) → 0.40 (>₹7000)
- **Demand multiplier**: 1.30 (last 3 days) → 0.85 (early booking)
- **Competitor multiplier**: 1.30 (we are cheapest) → 0.60 (we are most expensive)
- **Market noise**: Uniform(0.90, 1.10)
- **Final probability**: clipped to `[0.05, 0.98]`

---

## Reinforcement Learning Workflow

```
1.  Initialize the booking environment (100 inventory, 30-day window)
2.  Observe the current normalized state (6 features)
3.  Select a pricing action (epsilon-greedy: explore or exploit)
4.  Simulate customer demand (multi-factor probability model)
5.  Calculate immediate reward (revenue + shaping terms)
6.  Store experience in replay buffer (DQN) or update Q-table (Q-Learning)
7.  Train the neural network (DQN) on sampled mini-batches of 64
8.  Update target network periodically (every 20 episodes)
9.  Decay epsilon to reduce exploration over time (0.995 decay rate)
10. Repeat for 1000 training episodes
11. Evaluate the trained model on 1000 fresh episodes (epsilon = 0)
12. Compare with baseline strategies
13. Visualize and display results on Flask dashboard
```

---

## Agents

### Q-Learning Agent

- **Type**: Tabular, model-free, off-policy
- **State representation**: Discretized — continuous floats multiplied by 10 and cast to int
  - Example: `[1.0, 0.93, 0.55, 0.61, 0.72, 0.69]` → `(10, 9, 5, 6, 7, 7)`
- **Q-table**: Python dictionary, lazily initialized per state with zeros
- **Update rule (Bellman equation)**:
  ```
  Q(s,a) ← Q(s,a) + α × [r + γ × max_a' Q(s',a') − Q(s,a)]
  ```
- **Hyperparameters**: α=0.1, γ=0.95, ε=1.0→0.01 (decay 0.995)
- **Saved as**: `saved_models/q_table.npy`

### DQN Agent

- **Type**: Deep neural network, model-free, off-policy
- **Architecture**: `Linear(6→64) → ReLU → Linear(64→64) → ReLU → Linear(64→3)`
- **Key techniques**:
  - **Experience Replay**: Randomly samples 64 transitions from a 10,000-capacity deque buffer
  - **Target Network**: Separate frozen network updated every 20 episodes for training stability
  - **Epsilon-Greedy**: ε=1.0→0.01 (decay rate 0.995 per step)
- **Optimizer**: Adam (lr=0.001)
- **Loss function**: MSE between predicted Q-values and Bellman targets
- **Device**: Auto-selects CUDA (GPU) or CPU
- **Saved as**: `saved_models/dqn_model.pth`

---

## Pricing Strategies Compared

| Strategy | Description |
|---|---|
| **Fixed Price** | Always keeps price at base (₹5,000) — action 1 every step |
| **Daily Discount** | Reduces price in the last 7 days to boost late bookings |
| **Q-Learning** | Learned tabular policy trained over 1000 episodes |
| **DQN** | Learned neural network policy trained over 1000 episodes |

Results saved to: `results/model_comparison.csv`

---

## Model Evaluation

The trained DQN model is evaluated over **1000 simulation episodes** (epsilon = 0, no exploration).

**Performance metrics tracked:**

| Metric | Description |
|---|---|
| Average Revenue | Mean total revenue per episode (₹) |
| Average Reward | Mean cumulative reward per episode |
| Average Bookings | Mean number of successful bookings per episode |
| Average Remaining Inventory | Mean unsold inventory at episode end |

Results saved to: `results/evaluation_results.csv`

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Dynamic-Pricing-RL
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install torch pandas matplotlib flask
```

### 3. Train the Q-Learning Model

```bash
python -m rl_agent.train
```

### 4. Train the DQN Model

```bash
python -m rl_agent.train_dqn
```

### 5. Evaluate the DQN Model

```bash
python evaluate_dqn.py
```

### 6. Generate Performance Graphs

```bash
python -m rl_agent.plot_results
```

### 7. Compare All Pricing Strategies

```bash
python compare_models.py
```

### 8. Run the Flask Dashboard

```bash
cd flask_app
python app.py
```

Then open your browser at: `http://127.0.0.1:5000`

### 9. Run Environment Tests

```bash
python test_env.py
```

---

## Generated Outputs

### Saved Models
- `saved_models/q_table.npy` — Trained Q-Learning table (dictionary format)
- `saved_models/dqn_model.pth` — Trained DQN model weights (PyTorch state dict)

### Result Files
- `results/evaluation_results.csv` — DQN episode-level evaluation data
- `results/model_comparison.csv` — Aggregated strategy comparison (all 4 strategies)
- `results/price_trajectory.csv` — Price decision history per episode

### Graphs
- `graphs/revenue_vs_episode.png`
- `graphs/reward_vs_episode.png`
- `graphs/bookings_vs_episode.png`
- `graphs/inventory_vs_episode.png`

---

## Results

The Reinforcement Learning agents learn adaptive pricing strategies that respond to real-time booking conditions. DQN outperforms Q-Learning and both baseline strategies due to its ability to generalize across continuous state spaces using neural network function approximation. The target network and experience replay further improve stability and sample efficiency. Fixed Price and Daily Discount strategies serve as interpretable baselines for benchmarking.

---

## Future Enhancements

- Real-time hotel and airline booking data integration
- Live competitor pricing analysis via web scraping or API
- Advanced RL algorithms (PPO, A3C, SAC)
- Multi-agent pricing for competing properties
- Cloud deployment (AWS / GCP / Azure)
- Interactive real-time analytics dashboard
- Real-time demand forecasting with LSTM
- Price elasticity modeling
- Seasonal and event-based demand pattern handling

---

## Conclusion

This project demonstrates the application of Reinforcement Learning to solve real-world dynamic pricing problems in the travel and hospitality industry. By combining a custom Gymnasium environment, Q-Learning, Deep Q-Networks, reward shaping, evaluation analytics, and a Flask dashboard, the system provides an intelligent, autonomous pricing solution capable of maximizing revenue while efficiently managing limited inventory across a 30-day booking horizon.

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
├── Flask_app/
|  
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
