from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/lokasi", methods=["POST"])
def lokasi():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")

    print(f"📍 GPS diterima: {lat}, {lon}")

    return jsonify({"status": "ok"})

app.run(host="0.0.0.0", port=5000)
