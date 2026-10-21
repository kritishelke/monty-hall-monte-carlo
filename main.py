import random
import matplotlib.pyplot as plt

switch_win_probability = []
stay_win_probability = []

doors = ["car", "goat", "goat"]

def monte_carlo(iterations):
    win_switch_counter = 0
    win_stay_counter = 0

    for i in range(iterations):
        random.shuffle(doors)
        k = random.randrange(0,3)
    
        if doors[k] != "car":
            win_switch_counter += 1
        elif doors[k] == "car":
            win_stay_counter += 1

    win_by_switch_probability = win_switch_counter / (i+1)
    win_by_stay_probability = win_stay_counter / (i+1)

    switch_win_probability.append(win_by_switch_probability)
    stay_win_probability.append(win_by_stay_probability)

    return win_by_switch_probability, win_by_stay_probability

switch, stay = monte_carlo(10000)
print(f"Always switch: {switch}")
print(f"Always stay: {stay}")

import matplotlib.pyplot as plt
plt.plot(switch_win_probability)
plt.plot(stay_win_probability) 