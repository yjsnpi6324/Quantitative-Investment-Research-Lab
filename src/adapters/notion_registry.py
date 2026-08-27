"""Notion adapter boundary. Concrete API client is injected by runtime."""
from __future__ import annotations

class NotionRegistryAdapter:
    def __init__(self, client, config:dict): self.client,self.config=client,config
    def resolve_production(self, production_id):
        return self.client.resolve_production(production_id, self.config)
    def list_due_predictions(self, as_of):
        return self.client.list_due_predictions(as_of, self.config)
    def append_evaluation(self, evaluation):
        return self.client.append_evaluation(evaluation, self.config)
    def update_health(self, production_id, health):
        return self.client.update_health(production_id, health, self.config)
