from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/version", methods=["GET"])
def version():
    now_utc = datetime.now(timezone.utc)
    return jsonify({
        "service": "sdlc-target",
        "time_utc": now_utc.isoformat(),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
