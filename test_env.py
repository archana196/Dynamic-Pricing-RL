from gym_environment.pricing_env import DynamicPricingEnv

env = DynamicPricingEnv()

state, info = env.reset()

print("Initial State:", state)

done = False

while not done:

    action = env.action_space.sample()

    state, reward, terminated, truncated, info = env.step(action)

    print("----------------------------------")
    print("Action:", action)
    print("State:", state)
    print("Reward:", reward)
    print(info)

    done = terminated or truncated

env.close()