"""GitHub evidence-ledger adapter boundary."""
from __future__ import annotations
from src.evaluation.immutable_ledger import verify_prediction

class GitHubLedgerAdapter:
    def __init__(self, client, repo:str, branch:str="main"):
        self.client,self.repo,self.branch=client,repo,branch
    def append_prediction(self, locked_prediction):
        if not verify_prediction(locked_prediction): raise ValueError("ledger hash verification failed")
        return self.client.append_jsonl(self.repo,"data/ledger/predictions.jsonl",locked_prediction,self.branch)
    def verify_prediction(self, prediction_id):
        record=self.client.find_prediction(self.repo,prediction_id,self.branch)
        return bool(record) and verify_prediction(record)
