import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(trials=100_000):
    results = {i: 0 for i in range(2, 13)}  # суми від 2 до 12

    for _ in range(trials):
        roll = random.randint(1, 6) + random.randint(1, 6)
        results[roll] += 1

    probabilities = {k: round(v / trials * 100, 2) for k, v in results.items()}
    return probabilities

# Ймовірності 
def analytical_probabilities():
    return {
        2: round(1/36 * 100, 2),
        3: round(2/36 * 100, 2),
        4: round(3/36 * 100, 2),
        5: round(4/36 * 100, 2),
        6: round(5/36 * 100, 2),
        7: round(6/36 * 100, 2),
        8: round(5/36 * 100, 2),
        9: round(4/36 * 100, 2),
        10: round(3/36 * 100, 2),
        11: round(2/36 * 100, 2),
        12: round(1/36 * 100, 2)
    }

def plot_probabilities(monte_carlo, analytical):
    sums = list(range(2, 13))
    mc_values = [monte_carlo[s] for s in sums]
    an_values = [analytical[s] for s in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, mc_values, width=0.4, label="Монте-Карло", color="skyblue", align="center")
    plt.plot(sums, an_values, label="Аналітичні", color="darkviolet", marker="o", linewidth=2)

    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність (%)")
    plt.title("Порівняння ймовірностей: Монте-Карло vs Аналітичні")
    plt.xticks(sums)
    plt.legend()
    plt.grid(True)
    plt.savefig("Task_7_dice_probabilities.png")
    plt.show()

# Запуск симуляції
monte_carlo = monte_carlo_dice_simulation(trials=100_000)
analytical = analytical_probabilities()
plot_probabilities(monte_carlo, analytical)