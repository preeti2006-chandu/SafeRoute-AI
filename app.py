from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

model = joblib.load("risk_model.pkl")

@app.route("/predict-risk", methods=["POST"])
def predict_risk():
    data = request.get_json()
    crime_rate = data["crime_rate"]
    lighting = data["lighting"]
    crowd = data["crowd"]

    prediction = model.predict([[crime_rate, lighting, crowd]])[0]
    risk_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}

    return jsonify({"risk_level": risk_map[prediction]})

if __name__ == "__main__":
    app.run(debug=True)

