"""Champion Health Score skeleton."""


def champion_health_score(metrics):
    weights = {
        "accuracy": 0.30,
        "stability": 0.20,
        "robustness": 0.20,
        "data_quality": 0.15,
        "explainability": 0.15,
    }
    return sum(metrics.get(k, 0) * w for k, w in weights.items())
