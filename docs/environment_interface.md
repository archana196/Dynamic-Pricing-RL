# Environment Interface

## State

[inventory, remaining_days, current_price]

Example:

[100,30,5000]

---

## Actions

0 -> Decrease Price

1 -> Keep Same Price

2 -> Increase Price

---

## Reset

state = env.reset()

Returns:

Initial State

---

## Step

next_state, reward, terminated, truncated, info = env.step(action)

Returns

next_state

reward

terminated

truncated

info

---

## Info Dictionary

booking_status

inventory

remaining_days

current_price

revenue
