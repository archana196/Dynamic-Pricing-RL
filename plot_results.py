import os

import pandas as pd

import matplotlib.pyplot as plt
csv_file = "results/evaluation_results.csv"

df = pd.read_csv(csv_file)
os.makedirs("graphs", exist_ok=True)
plt.figure(figsize=(10,5))

plt.plot(df["Episode"], df["Revenue"])

plt.title("Revenue vs Episode")

plt.xlabel("Episode")

plt.ylabel("Revenue")

plt.grid(True)

plt.savefig("graphs/revenue_vs_episode.png")

plt.close()
plt.figure(figsize=(10,5))

plt.plot(df["Episode"], df["Reward"])

plt.title("Reward vs Episode")

plt.xlabel("Episode")

plt.ylabel("Reward")

plt.grid(True)

plt.savefig("graphs/reward_vs_episode.png")

plt.close()
plt.figure(figsize=(10,5))

plt.plot(df["Episode"], df["Bookings"])

plt.title("Bookings vs Episode")

plt.xlabel("Episode")

plt.ylabel("Bookings")

plt.grid(True)

plt.savefig("graphs/bookings_vs_episode.png")

plt.close()
plt.figure(figsize=(10,5))

plt.plot(df["Episode"], df["Inventory_Left"])

plt.title("Remaining Inventory vs Episode")

plt.xlabel("Episode")

plt.ylabel("Remaining Inventory")

plt.grid(True)

plt.savefig("graphs/inventory_vs_episode.png")

plt.close()
print("All graphs generated successfully!")
print("Graphs saved in the 'graphs' folder.")




