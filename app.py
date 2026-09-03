import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "service": "sdlc-target",
        "time_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
