from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200


@app.route("/version", methods=["GET"])
def version():
    response = {
        "service": "sdlc-target",
        "version": "1.0.0"
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
