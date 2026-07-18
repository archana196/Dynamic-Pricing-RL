from gym_environment.pricing_env import DynamicPricingEnv
from baseline.fixed_price import FixedPriceStrategy
from baseline.daily_discount import DailyDiscountStrategy

env = DynamicPricingEnv()

agent = DailyDiscountStrategy()

state, info = env.reset()

done = False
total_reward = 0

while not done:

    action = agent.choose_action()

    next_state, reward, terminated, truncated, info = env.step(action)

    total_reward += reward

    state = next_state

    done = terminated or truncated

print("\n========== Baseline Results ==========")
print(f"Strategy          : {agent.__class__.__name__}")
print(f"Total Reward      : {total_reward:.2f}")
print(f"Total Revenue     : ₹{info['total_revenue']}")
print(f"Total Bookings    : {info['total_bookings']}")
print(f"Inventory Left    : {info['inventory']}")
print(f"Remaining Days    : {info['remaining_days']}")
print(f"Final Price       : ₹{info['current_price']}")
print("======================================")