# Вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм - сортування за співвідношенням калорій до вартості
def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected = []
    total_cost = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected.append(name)
            total_cost += data["cost"]

    return selected

# Динамічне програмування - підбір оптимального набору, без повторів
def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, data = item_list[i - 1]
        cost = data["cost"]
        calories = data["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлення вибраних страв
    selected = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, data = item_list[i - 1]
            selected.append(name)
            b -= data["cost"]

    selected.reverse()
    return selected

# Запуск алгоритмів

budget = 199

print("Жадібний алгоритм:")
print(greedy_algorithm(items, budget))

print("\nДинамічне програмування:")
print(dynamic_programming(items, budget))