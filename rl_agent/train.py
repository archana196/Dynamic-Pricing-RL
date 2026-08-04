import os

from gym_environment.pricing_env import DynamicPricingEnv
from rl_agent.q_learning import QLearningAgent


# ----------------------------------------
# Training Configuration
# ----------------------------------------

EPISODES = 1000


# ----------------------------------------
# Create Environment
# ----------------------------------------

env = DynamicPricingEnv()


# ----------------------------------------
# Create Agent
# ----------------------------------------

agent = QLearningAgent()


# ----------------------------------------
# Store Rewards
# ----------------------------------------

episode_rewards = []


# ----------------------------------------
# Training Loop
# ----------------------------------------

for episode in range(EPISODES):

    # Reset Environment
    state, info = env.reset()

    done = False
    total_reward = 0

    while not done:

        # Choose Action
        action = agent.choose_action(state)

        # Perform Action
        next_state, reward, terminated, truncated, info = env.step(action)

        # Update Q Table
        agent.update_q_table(
            state,
            action,
            reward,
            next_state,
        )

        # Move to Next State
        state = next_state

        # Accumulate Reward
        total_reward += reward

        # Check Episode End
        done = terminated or truncated

    # Save Reward
    episode_rewards.append(total_reward)

    # Reduce Exploration
    agent.decay_epsilon()

    # ----------------------------------------
    # Progress
    # ----------------------------------------

    print("=" * 60)
    print(f"Episode           : {episode + 1}/{EPISODES}")
    print(f"Total Reward      : {total_reward:.2f}")
    print(f"Revenue           : ₹{info['total_revenue']}")
    print(f"Bookings          : {info['total_bookings']}")
    print(f"Inventory Left    : {info['inventory']}")
    print(f"Remaining Days    : {info['remaining_days']}")
    print(f"Final Price       : ₹{info['current_price']}")
    print(f"Epsilon           : {agent.epsilon:.3f}")
    print("=" * 60)


# ----------------------------------------
# Save Trained Model
# ----------------------------------------

os.makedirs("saved_models", exist_ok=True)

agent.save_q_table(
    "saved_models/q_table.npy"
)


# ----------------------------------------
# Training Summary
# ----------------------------------------

print("\nTraining Completed Successfully!")
print(f"Episodes Trained : {EPISODES}")
print(f"Average Reward   : {sum(episode_rewards)/len(episode_rewards):.2f}")
print(f"Maximum Reward   : {max(episode_rewards):.2f}")
print(f"Minimum Reward   : {min(episode_rewards):.2f}")


env.close()