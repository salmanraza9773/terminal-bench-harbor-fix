import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

def test_criterion_1_parse_metrics():
    """Verify traffic analysis metrics: total_requests, unique_ips, and top_path."""
    assert REPORT_PATH.exists()
    
    with open(REPORT_PATH, 'r') as f:
        data = json.load(f)
        
    assert isinstance(data.get("total_requests"), int) and data["total_requests"] > 0
    assert isinstance(data.get("unique_ips"), int) and data["unique_ips"] > 0
    assert isinstance(data.get("top_path"), str) and len(data["top_path"]) > 0

def test_criterion_2_save_location():
    """Verify output destination is exactly at /app/report.json."""
    assert REPORT_PATH.exists()
    try:
        with open(REPORT_PATH, 'r') as f:
            json.load(f)
    except json.JSONDecodeError:
        assert False

def test_criterion_3_strict_schema():
    """Verify the JSON keys exactly match the specified structural schema."""
    with open(REPORT_PATH, 'r') as f:
        data = json.load(f)
        
    required_keys = ["total_requests", "unique_ips", "top_path"]
    for key in required_keys:
        assert key in data
    assert len(data) == len(required_keys)