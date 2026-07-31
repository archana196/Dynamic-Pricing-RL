from gym_environment.pricing_env import DynamicPricingEnv


def main():
    env = DynamicPricingEnv()

    obs, info = env.reset()

    print("=" * 60)
    print("Dynamic Pricing Environment Test")
    print("=" * 60)

    print("\nInitial Observation:")
    print(obs)

    episode_reward = 0
    step = 0

    done = False

    while not done:
        step += 1

        # Random action (0 = Decrease, 1 = Keep, 2 = Increase)
        action = env.action_space.sample()

        obs, reward, terminated, truncated, info = env.step(action)

        episode_reward += reward

        print("\n" + "=" * 60)
        print(f"Step: {step}")
        print("=" * 60)

        print(f"Action              : {action}")
        print(f"Reward              : {reward:.2f}")
        print(f"Total Reward        : {episode_reward:.2f}")

        print("\nObservation:")
        print(obs)

        print("\nEnvironment Info:")
        for key, value in info.items():
            print(f"{key:20}: {value}")

        print("\nCurrent Environment State:")
        env.render()

        done = terminated or truncated

    print("\n" + "=" * 60)
    print("Episode Finished")
    print("=" * 60)
    print(f"Total Steps         : {step}")
    print(f"Total Reward        : {episode_reward:.2f}")

    env.close()


if __name__ == "__main__":
    main()
