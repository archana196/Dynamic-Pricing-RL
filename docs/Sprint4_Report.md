# Sprint 4 Report – Policy Evaluation & Business Dashboard

## Project Title

**Travel & Hospitality – Reinforcement Learning for Dynamic Pricing**

---

# Sprint Objective

The objective of Sprint 4 is to evaluate the performance of the trained Deep Q-Network (DQN) agent and present the results through performance metrics, visualizations, and a business dashboard. This sprint demonstrates how the reinforcement learning agent performs over multiple booking seasons and provides insights into its pricing strategy.

---

# Work Completed

## 1. DQN Policy Evaluation

* Loaded the trained DQN model.
* Evaluated the model over **1000 simulated booking seasons**.
* Disabled exploration (`epsilon = 0`) to test the learned policy.
* Recorded evaluation metrics for every episode.

---

## 2. Performance Metrics

The following metrics were collected:

* Total Revenue
* Total Reward
* Total Bookings
* Remaining Inventory

Average values were calculated after completing all simulation episodes.

---

## 3. Evaluation Results Export

All episode-wise evaluation data was exported to:

```
results/evaluation_results.csv
```

The CSV contains:

* Episode Number
* Revenue
* Reward
* Bookings
* Remaining Inventory

This file is used for further analysis and dashboard integration.

---

## 4. Performance Visualization

Generated the following graphs using Matplotlib:

* Revenue vs Episode
* Reward vs Episode
* Bookings vs Episode
* Remaining Inventory vs Episode

These graphs help analyze the learning performance and consistency of the trained DQN agent.

---

# Technologies Used

* Python
* Gymnasium
* PyTorch
* Pandas
* Matplotlib

---

# Files Created

```
rl_agent/
    evaluate_dqn.py
    plot_results.py

results/
    evaluation_results.csv

graphs/
    revenue_vs_episode.png
    reward_vs_episode.png
    bookings_vs_episode.png
    inventory_vs_episode.png
```

---

# Outcome

Successfully evaluated the trained DQN agent over multiple booking simulations and generated quantitative performance metrics along with graphical visualizations. The generated results are ready to be integrated into the Flask dashboard for business analysis and demonstration.

---

# Next Steps

* Compare DQN with baseline pricing strategies.
* Integrate evaluation results into the Flask dashboard.
* Perform complete system testing.
* Finalize project documentation and presentation.
