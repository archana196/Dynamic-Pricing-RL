from gym_environment.pricing_env import DynamicPricingEnv

env = DynamicPricingEnv()

obs, info = env.reset()

print("Initial Observation")
print(obs)

done = False

while not done:

    action = env.action_space.sample()

    obs, reward, terminated, truncated, info = env.step(action)

    env.render()

    print("Action :", action)
    print("Reward :", reward)
    print("State  :", obs)

    done = terminated or truncated

env.close()