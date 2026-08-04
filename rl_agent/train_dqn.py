import os

from gym_environment.pricing_env import DynamicPricingEnv
from rl_agent.dqn_agent import DQNAgent


def train():

    env = DynamicPricingEnv()

    agent = DQNAgent()

    episodes = 1000

    target_update = 20

    save_path = "saved_models"

    os.makedirs(save_path, exist_ok=True)

    for episode in range(episodes):

        state, info = env.reset()

        done = False

        total_reward = 0

        while not done:

            action = agent.choose_action(state)

            next_state, reward, terminated, truncated, info = env.step(action)

            done = terminated or truncated

            agent.remember(
                state,
                action,
                reward,
                next_state,
                done,
            )

            agent.train()

            state = next_state

            total_reward += reward

        if episode % target_update == 0:
            agent.update_target_network()

        if (episode + 1) % 100 == 0:

            print("=" * 60)

            print(f"Episode            : {episode+1}")

            print(f"Reward             : {total_reward:.2f}")

            print(f"Revenue            : ₹{info['total_revenue']}")

            print(f"Bookings           : {info['total_bookings']}")

            print(f"Epsilon            : {agent.epsilon:.3f}")

            print("=" * 60)

    model_path = os.path.join(
        save_path,
        "dqn_model.pth"
    )

    agent.save_model(model_path)

    print("\nTraining Completed Successfully!")

    print(f"Model Saved At : {model_path}")


if __name__ == "__main__":
    train()