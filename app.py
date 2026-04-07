import os
import pickle
from flask import Flask, request, jsonify
from utils import recommend_crop
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
CROP_MAPPING_PATH = os.path.join(BASE_DIR, "crop_mapping.pkl")

# Load model and crop mapping
model = pickle.load(open(MODEL_PATH, "rb"))
crop_mapping = pickle.load(open(CROP_MAPPING_PATH, "rb"))

@app.route('/')
def home():
    return "💧 HydroGuard_AI API Running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json(force=True)

    try:
        rainfall = float(data.get('rainfall', 0))
        temperature = float(data.get('temperature', 0))
        crop_name = str(data.get('crop', '')).strip()
        water_usage = str(data.get('water_usage', '')).strip().lower()

        # Convert crop to number using mapping
        crop_code = next(
            (key for key, value in crop_mapping.items() if value.lower() == crop_name.lower()),
            None
        )
        if crop_code is None:
            return jsonify({"error": "Invalid crop name"}), 400

        # Convert water usage
        water_map = {'low': 0, 'medium': 1, 'high': 2}
        if water_usage not in water_map:
            return jsonify({"error": "Invalid water usage"}), 400
        water_code = water_map[water_usage]

        # Prediction
        features = [[rainfall, temperature, crop_code, water_code]]
        prediction = float(model.predict(features)[0])

        # Limit range
        prediction = max(0.0, min(50.0, prediction))

        if prediction > 30:
            level_status = "⚠️ High Depletion"
        elif prediction > 15:
            level_status = "Moderate"
        else:
            level_status = "Safe"

        suggestion = recommend_crop(prediction)

        return jsonify({
            "groundwater_prediction": round(prediction, 2),
            "status": level_status,
            "recommended_crop": suggestion
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    print("🚀 Starting HydroGuard_AI Backend...")
    print("🔥 Running Flask server on http://0.0.0.0:5000")
    app.run(debug=True, host="0.0.0.0", port=5000)

# import pickle
# import pandas as pd
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from utils import recommend_crop

# app = Flask(__name__)
# CORS(app)

# # Load model and mappings
# model = pickle.load(open("model.pkl", "rb"))
# crop_mapping = pickle.load(open("crop_mapping.pkl", "rb"))
# df = pd.read_csv("data.csv")
# df.columns = ["district", "groundwater", "rainfall", "temperature", "crop", "water_usage"]

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     data = request.json
#     try:
#         rainfall = float(data['rainfall'])
#         temp = float(data['temperature'])
#         crop_name = data['crop']
#         water_usage = data['water_usage']

#         # Encode crop
#         crop_code = next((k for k, v in crop_mapping.items() if v.lower() == crop_name.lower()), None)
#         if crop_code is None: return jsonify({"error": "Invalid crop"}), 400

#         # Encode water usage
#         water_map = {'low': 0, 'medium': 1, 'high': 2}
#         water_code = water_map.get(water_usage.lower(), 1)

#         # Prediction & Insights
#         prediction = model.predict([[rainfall, temp, crop_code, water_code]])[0]
#         prediction = max(0, min(50, prediction))

#         # "XAI" Logic - Simple feature impact explanation
#         insights = []
#         if temp > 25: insights.append("High temperature is increasing evaporation.")
#         if rainfall < 500: insights.append("Low rainfall is limiting aquifer recharge.")

#         return jsonify({
#             "prediction": round(prediction, 2),
#             "status": "Critical" if prediction > 30 else "Moderate" if prediction > 15 else "Safe",
#             "recommendation": recommend_crop(prediction),
#             "insights": insights
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/map-data')
# def get_map_data():
#     # Group by district for the heatmap
#     avg_data = df.groupby('district')['groundwater'].mean().to_dict()
#     return jsonify(avg_data)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)