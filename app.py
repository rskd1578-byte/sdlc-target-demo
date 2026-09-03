from datetime import datetime, timezone
from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/healthz", methods=["GET"])
def healthz():
   return jsonify({"status": "ok"}), 200
@app.route("/version", methods=["GET"])
def version():
   """
   Returns the service name and the current server time.
   """
   return jsonify({
       "service": "sdlc-target",
       "time_utc": datetime.now(timezone.utc).isoformat()
   }), 200
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
