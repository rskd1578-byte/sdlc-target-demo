from datetime import datetime, timezone, timedelta
from app import app
def test_version_endpoint():
   """
   Tests the /version endpoint to ensure it meets acceptance criteria.
   """
   client = app.test_client()
   response = client.get("/version")
   # AC-2: The endpoint returns a 200 OK status code.
   assert response.status_code == 200, "Status code should be 200"
   # AC-3: The response is a valid JSON object.
   try:
       data = response.get_json()
       assert isinstance(data, dict), "Response should be a JSON object"
   except Exception:
       assert False, "Response is not valid JSON"
   # AC-4: The JSON object contains a 'service' key with the value 'sdlc-target'.
   assert "service" in data, "Response should contain 'service' key"
   assert data["service"] == "sdlc-target", "Service name should be 'sdlc-target'"
   # AC-5: The JSON object contains a 'time_utc' key with a value that is a valid ISO-8601 timestamp.
   assert "time_utc" in data, "Response should contain 'time_utc' key"
   time_str = data["time_utc"]
   try:
       parsed_time = datetime.fromisoformat(time_str)
       # Check if it's timezone-aware
       assert parsed_time.tzinfo is not None, "Timestamp should be timezone-aware"
       # Check if the time is recent (e.g., within a reasonable delta)
       now_utc = datetime.now(timezone.utc)
       assert abs(now_utc - parsed_time) < timedelta(seconds=5), "Timestamp is not recent"
   except (ValueError, TypeError) as e:
       assert False, f"'{time_str}' is not a valid ISO-8601 timestamp. Error: {e}"
