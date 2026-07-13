from gym_environment.pricing_env import DynamicPricingEnv

env = DynamicPricingEnv()

obs, info = env.reset()

print("Initial Observation:", obs)
print("Info:", info)

obs, reward, terminated, truncated, info = env.step(1)

print("\nAfter Step")
print("Observation:", obs)
print("Reward:", reward)
print("Terminated:", terminated)
print("Truncated:", truncated)
print("Info:", info)

env.close()