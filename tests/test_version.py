from datetime import datetime
import json
import pytest
def test_version_endpoint(client):
   """
   Tests the /version endpoint to ensure it meets specifications.
   """
   response = client.get("/version")
   assert response.status_code == 200
   assert response.content_type == "application/json"
   data = json.loads(response.data)
   assert data["service"] == "sdlc-target"
   assert "time_utc" in data
   # Validate the timestamp is a valid ISO 8601 string
   try:
       # datetime.fromisoformat() in some Python versions doesn't parse
       # the 'Z' suffix for UTC, so we replace it with a standard offset.
       time_str = data["time_utc"].replace("Z", "+00:00")
       datetime.fromisoformat(time_str)
   except ValueError:
       pytest.fail(f"time_utc '{data['time_utc']}' is not a valid ISO 8601 timestamp.")
