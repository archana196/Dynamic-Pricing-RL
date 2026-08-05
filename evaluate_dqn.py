import csv
import os
import torch

from gym_environment.pricing_env import DynamicPricingEnv
from rl_agent.dqn_agent import DQNAgent


def evaluate():
    env = DynamicPricingEnv()
    agent = DQNAgent()
    agent.load_model("saved_models/dqn_model.pth")

    # Disable exploration during evaluation
    agent.epsilon = 0

    episodes = 1000

    revenues = []
    rewards = []
    bookings = []
    inventory_left = []

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

        # Save metrics at the end of each episode
        revenues.append(info["total_revenue"])
        rewards.append(total_reward)
        bookings.append(info["total_bookings"])
        inventory_left.append(info["inventory"])
  
    avg_revenue = sum(revenues) / len(revenues)
    avg_reward = sum(rewards) / len(rewards)
    avg_bookings = sum(bookings) / len(bookings)
    avg_inventory = sum(inventory_left) / len(inventory_left)
   
    print("=" * 60)
    print("DQN Evaluation Summary")
    print("=" * 60)
    print(f"Episodes              : {episodes}")
    print(f"Average Revenue       : ₹{avg_revenue:.2f}")
    print(f"Average Reward        : {avg_reward:.2f}")
    print(f"Average Bookings      : {avg_bookings:.2f}")
    print(f"Average Inventory Left: {avg_inventory:.2f}")
    print("=" * 60)

    # Fixed indentation below
    os.makedirs("results", exist_ok=True)
    csv_path = "results/evaluation_results.csv"

    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Episode",
            "Revenue",
            "Reward",
            "Bookings",
            "Inventory_Left"
        ])

        for i in range(episodes):
            writer.writerow([
                i + 1,
                revenues[i],
                rewards[i],
                bookings[i],
                inventory_left[i]
            ])

    print(f"\nResults saved to: {csv_path}")


if __name__ == "__main__":
    evaluate()