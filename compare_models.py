import os
import torch
import csv
import numpy as np
import pandas as pd

from gym_environment.pricing_env import DynamicPricingEnv

from rl_agent.dqn_agent import DQNAgent
from rl_agent.q_learning import QLearningAgent


EPISODES = 1000


# ==========================================================
# Evaluate Fixed Price Strategy
# ==========================================================

def evaluate_fixed_price(episodes=EPISODES):

    env = DynamicPricingEnv()

    revenues = []
    rewards = []
    bookings = []

    for episode in range(episodes):

        state, info = env.reset()

        done = False
        total_reward = 0

        while not done:

            # Keep Base Price
            action = 1

            next_state, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            state = next_state
            total_reward += reward

        revenues.append(info["total_revenue"])
        rewards.append(total_reward)
        bookings.append(info["total_bookings"])

    return {
        "Strategy": "Fixed Price",
        "Revenue": np.mean(revenues),
        "Reward": np.mean(rewards),
        "Bookings": np.mean(bookings),
    }


# ==========================================================
# Evaluate Daily Discount Strategy
# ==========================================================

def evaluate_daily_discount(episodes=EPISODES):

    env = DynamicPricingEnv()

    revenues = []
    rewards = []
    bookings = []

    for episode in range(episodes):

        state, info = env.reset()

        done = False

        total_reward = 0

        while not done:

            # Last week -> reduce price
            if env.remaining_days <= 7:
                action = 0

            else:
                action = 1

            next_state, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            state = next_state
            total_reward += reward

        revenues.append(info["total_revenue"])
        rewards.append(total_reward)
        bookings.append(info["total_bookings"])

    return {
        "Strategy": "Daily Discount",
        "Revenue": np.mean(revenues),
        "Reward": np.mean(rewards),
        "Bookings": np.mean(bookings),
    }


# ==========================================================
# Evaluate Q-Learning Agent
# ==========================================================

def evaluate_q_learning(episodes=EPISODES):

    env = DynamicPricingEnv()

    agent = QLearningAgent()

    agent.load_q_table("saved_models/q_table.npy")

    agent.epsilon = 0

    revenues = []

    rewards = []

    bookings = []

    for episode in range(episodes):

        state, info = env.reset()

        done = False

        total_reward = 0

        while not done:

            action = agent.predict(state)

            next_state, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            state = next_state

            total_reward += reward

        revenues.append(info["total_revenue"])
        rewards.append(total_reward)
        bookings.append(info["total_bookings"])

    return {
        "Strategy": "Q-Learning",
        "Revenue": np.mean(revenues),
        "Reward": np.mean(rewards),
        "Bookings": np.mean(bookings),
    }

# ==========================================================
# Evaluate DQN Agent
# ==========================================================

def evaluate_dqn(episodes=EPISODES):

    env = DynamicPricingEnv()

    agent = DQNAgent()

    agent.load_model("saved_models/dqn_model.pth")

    # Disable exploration
    agent.epsilon = 0

    revenues = []
    rewards = []
    bookings = []

    for episode in range(episodes):

        state, info = env.reset()

        done = False
        total_reward = 0

        while not done:

            action = agent.choose_action(state)

            next_state, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            state = next_state
            total_reward += reward

        revenues.append(info["total_revenue"])
        rewards.append(total_reward)
        bookings.append(info["total_bookings"])

    return {
        "Strategy": "DQN",
        "Revenue": np.mean(revenues),
        "Reward": np.mean(rewards),
        "Bookings": np.mean(bookings),
    }


# ==========================================================
# Compare All Models
# ==========================================================

def compare_models():

    print("=" * 60)
    print("Running Strategy Comparison")
    print("=" * 60)

    results = []

    print("\nEvaluating Fixed Price...")
    results.append(evaluate_fixed_price())

    print("Evaluating Daily Discount...")
    results.append(evaluate_daily_discount())

    print("Evaluating Q-Learning...")
    results.append(evaluate_q_learning())

    print("Evaluating DQN...")
    results.append(evaluate_dqn())

    df = pd.DataFrame(results)

    return df


# ==========================================================
# Save Results
# ==========================================================

def save_results(df):

    os.makedirs("results", exist_ok=True)

    output_path = "results/model_comparison.csv"

    df.to_csv(output_path, index=False)

    print(f"\nResults saved to: {output_path}")







# ==========================================================
# Display Comparison
# ==========================================================

def display_results(df):

    print("\n" + "=" * 70)
    print("DYNAMIC PRICING MODEL COMPARISON")
    print("=" * 70)

    print(df.to_string(index=False))

    print("=" * 70)

    best_revenue = df.loc[df["Revenue"].idxmax()]
    best_reward = df.loc[df["Reward"].idxmax()]
    best_bookings = df.loc[df["Bookings"].idxmax()]

    print(f"\nBest Revenue  : {best_revenue['Strategy']} "
          f"(₹{best_revenue['Revenue']:.2f})")

    print(f"Best Reward   : {best_reward['Strategy']} "
          f"({best_reward['Reward']:.2f})")

    print(f"Best Bookings : {best_bookings['Strategy']} "
          f"({best_bookings['Bookings']:.2f})")

    print("=" * 70)


# ==========================================================
# Main Function
# ==========================================================

def main():

    comparison_df = compare_models()

    save_results(comparison_df)

    display_results(comparison_df)

    print("\nComparison completed successfully.")


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()