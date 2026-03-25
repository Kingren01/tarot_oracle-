import os
import csv
import json
from datetime import datetime
from typing import List, Dict, Any, Optional

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
BUCKET_PATH = os.path.join(DATA_DIR, "intelligence_bucket.csv")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    if not os.path.exists(BUCKET_PATH):
        from .mock_data import accounts as mock_accounts, mock_crewai_output
        with open(BUCKET_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Headers: account_name, incumbent, industry, value, score, timestamp, payload_json
            writer.writerow(["account_name", "incumbent", "industry", "value", "score", "timestamp", "payload_json"])
            
            # Seed with mock data
            for acc in mock_accounts:
                # Merge mock metadata with the base response payload for consistency
                payload = mock_crewai_output.copy()
                payload["target_account"] = acc["name"]
                payload["competitor_name"] = acc["incumbent"]
                
                writer.writerow([
                    acc["name"], 
                    acc["incumbent"], 
                    acc["industry"], 
                    acc["value"], 
                    acc["score"], 
                    "2025-01-01 12:00:00", 
                    json.dumps(payload)
                ])

def save_intelligence_record(account_name: str, incumbent: str, score: float, payload: Dict[str, Any]):
    """Saves a new CrewAI result to the CSV bucket."""
    ensure_data_dir()
    
    # Extract some high-level metrics for the table
    industry = "Life Sciences" # Default for this app
    value = payload.get("dashboard_metrics_package", {}).get("financial_projections", {}).get("year_1_savings", "N/A")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Store the full JSON payload for the detail view
    payload_json = json.dumps(payload)
    
    with open(BUCKET_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([account_name, incumbent, industry, value, score, timestamp, payload_json])

def load_intelligence_records() -> List[Dict[str, Any]]:
    """Loads and ranks all records from the CSV bucket by score descending."""
    ensure_data_dir()
    
    records = []
    if not os.path.exists(BUCKET_PATH):
        return records

    with open(BUCKET_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["score"] = float(row["score"])
                records.append(row)
            except (ValueError, TypeError):
                continue
    
    # Rank by score descending
    records.sort(key=lambda x: x["score"], reverse=True)
    return records

def get_record_by_name(account_name: str) -> Optional[Dict[str, Any]]:
    """Retrieves a specific record's full payload."""
    records = load_intelligence_records()
    for r in records:
        if r["account_name"] == account_name:
            if "payload_json" in r:
                return json.loads(r["payload_json"])
    return None
