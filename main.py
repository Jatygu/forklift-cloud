import random
import time
import json

print("🚀 Forklift Cloud v23 starting...")

def generate_strategy():
    return {
        "buy_threshold": random.uniform(0.001, 0.02),
        "sell_threshold": random.uniform(0.001, 0.02),
        "position_size": random.uniform(0.1, 1.0)
    }

def mutate(strategy):
    return {
        "buy_threshold": strategy["buy_threshold"] * random.uniform(0.8, 1.2),
        "sell_threshold": strategy["sell_threshold"] * random.uniform(0.8, 1.2),
        "position_size": strategy["position_size"] * random.uniform(0.8, 1.2)
    }

def test_strategy(strategy):
    base = random.uniform(-0.5, 1.5)
    edge = strategy["buy_threshold"] - strategy["sell_threshold"]
    return base + edge * 10

def save_best(strategy):
    with open("logs/best_strategy.json", "w") as f:
        json.dump(strategy, f)

best_strategy = None

while True:
    best_score = -999

    for _ in range(20):
        strategy = mutate(best_strategy) if best_strategy else generate_strategy()
        score = test_strategy(strategy)

        if score > best_score:
            best_score = score
            best_strategy = strategy

    print("🔥 BEST:", best_strategy, "Score:", best_score)
    save_best(best_strategy)

    time.sleep(5)
