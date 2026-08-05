import csv
import os
import torch

from gym_environment.pricing_env import DynamicPricingEnv
from rl_agent.dqn_agent import DQNAgent


def evaluate():

    env = DynamicPricingEnv()

    agent = DQNAgent()

    agent.load_model("saved_models/dqn_model.pth")

    # Disable exploration
    agent.epsilon = 0

    episodes = 1000

    revenues = []
    rewards = []
    bookings = []
    inventory_left = []

    # Store one episode's price trajectory
    price_history = []
    day_history = []

    for episode in range(episodes):

        state, info = env.reset()

        done = False

        total_reward = 0

        # Clear trajectory for the first episode only
        if episode == 0:
            price_history.clear()
            day_history.clear()

        while not done:

            action = agent.choose_action(state)

            next_state, reward, terminated, truncated, info = env.step(action)

            # Save price trajectory only for Episode 1
            if episode == 0:
                price_history.append(info["current_price"])
                day_history.append(info["remaining_days"])

            done = terminated or truncated

            state = next_state

            total_reward += reward

        revenues.append(info["total_revenue"])
        rewards.append(total_reward)
        bookings.append(info["total_bookings"])
        inventory_left.append(info["inventory"])

    avg_revenue = sum(revenues) / episodes
    avg_reward = sum(rewards) / episodes
    avg_bookings = sum(bookings) / episodes
    avg_inventory = sum(inventory_left) / episodes

    print("=" * 60)
    print("DQN Evaluation Summary")
    print("=" * 60)
    print(f"Episodes              : {episodes}")
    print(f"Average Revenue       : ₹{avg_revenue:.2f}")
    print(f"Average Reward        : {avg_reward:.2f}")
    print(f"Average Bookings      : {avg_bookings:.2f}")
    print(f"Average Inventory Left: {avg_inventory:.2f}")
    print("=" * 60)

    os.makedirs("results", exist_ok=True)

    # -----------------------------
    # Evaluation Results CSV
    # -----------------------------

    with open(
        "results/evaluation_results.csv",
        "w",
        newline=""
    ) as file:

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

    print("Evaluation results saved.")

    # -----------------------------
    # Price Trajectory CSV
    # -----------------------------

    with open(
        "results/price_trajectory.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Remaining_Days",
            "Current_Price"
        ])

        for day, price in zip(day_history, price_history):

            writer.writerow([
                day,
                price
            ])

    print("Price trajectory saved.")


if __name__ == "__main__":
    evaluate()