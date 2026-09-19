"""Notion adapter boundary. Concrete API client is injected by runtime."""
from __future__ import annotations


class NotionRegistryAdapter:
    def __init__(self, client, config: dict):
        self.client, self.config = client, config

    def resolve_production(self, production_id):
        return self.client.resolve_production(production_id, self.config)

    def list_due_predictions(self, as_of):
        return self.client.list_due_predictions(as_of, self.config)

    def append_evaluation(self, evaluation):
        return self.client.append_evaluation(evaluation, self.config)

    def has_evaluation(self, prediction_id, horizon):
        if hasattr(self.client, "has_evaluation"):
            return self.client.has_evaluation(
                prediction_id, horizon, self.config
            )
        if not hasattr(self.client, "list_evaluations"):
            return False
        return any(
            row.get("prediction_id") == prediction_id
            and str(row.get("horizon", "")).upper() == str(horizon).upper()
            for row in self.client.list_evaluations(None, self.config)
        )

    def list_evaluations(self, production_id):
        return self.client.list_evaluations(production_id, self.config)

    def update_health(self, production_id, health):
        return self.client.update_health(production_id, health, self.config)
