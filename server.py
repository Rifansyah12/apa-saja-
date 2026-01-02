from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Izinkan semua origin & header (untuk testing)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/lokasi", methods=["POST", "OPTIONS"])
def lokasi():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"})

    data = request.get_json(force=True, silent=True)

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    lat = data.get("latitude")
    lon = data.get("longitude")

    print(f"📍 GPS diterima: {lat}, {lon}")

    return jsonify({"status": "ok"})

app.run(host="0.0.0.0", port=5000)
