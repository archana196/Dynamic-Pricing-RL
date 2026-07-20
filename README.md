# 🚀 Dynamic Pricing using Reinforcement Learning (RL)

## 📌 Introduction

Dynamic pricing is a revenue optimization strategy where the price of a product or service changes in real time based on market conditions such as customer demand, competitor pricing, seasonality, occupancy, and other influencing factors. It is widely used in industries like hospitality, airlines, ride-sharing, and e-commerce to maximize revenue while maintaining customer satisfaction.

This project focuses on developing an **AI-powered Dynamic Pricing System** using **Reinforcement Learning (RL)**. Unlike traditional rule-based pricing methods, the RL agent continuously learns from interactions with a simulated environment and identifies optimal pricing strategies that maximize long-term rewards. The project utilizes **Q-Learning** and **Deep Q-Network (DQN)** algorithms within a custom **Gymnasium environment** to simulate realistic pricing scenarios for the travel and hospitality industry.

The solution aims to automate pricing decisions, improve occupancy rates, enhance revenue generation, and provide data-driven insights through an interactive Flask dashboard.

---
# 🎓 Internship Details

**Organization:** Infotact Solutions Pvt. Ltd.

**Internship Domain:** Artificial Intelligence & Machine Learning

**Project Title:** Dynamic Pricing using Reinforcement Learning (RL)

**Duration:** 45 Days

**Technology Stack:** Python, Gymnasium, Stable-Baselines3, Flask, Pandas, NumPy, Matplotlib

---

# Project Planning & Environment Design

## Objective

The primary objective of Week 1 was to understand the fundamentals of Dynamic Pricing and Reinforcement Learning (RL), analyze real-world pricing factors, and design the overall project architecture. The focus was on planning a custom Gymnasium environment that could simulate pricing decisions, customer demand, and booking behavior for future DQN training.

---

## Tasks Completed

- Studied the concepts of Dynamic Pricing and Reinforcement Learning.
- Explored Q-Learning and Deep Q-Network (DQN) algorithms.
- Reviewed the Gymnasium framework for creating custom RL environments.
- Designed the custom **DynamicPricingEnv** environment.
- Defined the observation space using normalized state variables:
  - Inventory Ratio
  - Remaining Days Ratio
  - Current Price Ratio
  - Competitor Price Ratio
  - Booking Probability
  - Demand Level
- Designed the action space:
  - Decrease Price
  - Keep Price
  - Increase Price
- Planned realistic customer demand simulation based on:
  - Current Price
  - Competitor Price
  - Remaining Booking Days
  - Market Randomness
- Designed a reward shaping strategy to maximize long-term revenue while balancing customer bookings and inventory utilization.
- Planned dynamic competitor pricing and booking simulation.
- Finalized the project architecture, folder structure, and technology stack.

---

## Deliverables

- Project architecture design
- Custom Gymnasium environment planning
- Observation space and action space design
- Demand simulation strategy
- Reward shaping strategy
- Project folder structure
- Development roadmap

---

## Learning Outcomes

By the end of Week 1, the project architecture and RL environment design were finalized. A strong understanding of Gymnasium, Dynamic Pricing, demand simulation, reward engineering, and DQN-based pricing strategies was established, creating a solid foundation for implementing the environment, training the RL agent, and integrating the Flask backend in the upcoming weeks.
