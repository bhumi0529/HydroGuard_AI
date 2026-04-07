import pickle
from flask import Flask, request, jsonify
from utils import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Load model and crop mapping
model = pickle.load(open("model.pkl", "rb"))
crop_mapping = pickle.load(open("crop_mapping.pkl", "rb"))

@app.route('/')
def home():
    return "💧 HydroGuard_AI API Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json

    rainfall = float(data['rainfall'])
    temperature = float(data['temperature'])
    crop_name = data['crop']
    water_usage = data['water_usage']

    # Convert crop to number using mapping
    crop_code = None
    for key, value in crop_mapping.items():
        if value.lower() == crop_name.lower():
            crop_code = key
            break

    if crop_code is None:
        return jsonify({"error": "Invalid crop name"})

    # Convert water usage
    water_map = {'Low': 0, 'Medium': 1, 'High': 2}
    water_code = water_map[water_usage.capitalize()]

    # Prediction
    features = [[rainfall, temperature, crop_code, water_code]]
    prediction = model.predict(features)[0]

    suggestion = recommend_crop(prediction)

    return jsonify({
        "groundwater_prediction": round(prediction, 2),
        "recommended_crop": suggestion
    })

if __name__ == '__main__':
    print("🚀 Starting HydroGuard_AI Backend...")
    print("🔥 Running Flask server...")
    app.run(debug=True)