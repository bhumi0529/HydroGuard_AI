import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

print("🔄 Loading data...")

# Load dataset
data = pd.read_csv("data.csv")

# Clean column names
data.columns = ["district", "groundwater", "rainfall", "temperature", "crop", "water_usage"]

print("✅ Data loaded")

# Encode categorical columns
# Crop encoding (automatic for ALL crops)
data['crop'] = data['crop'].astype('category')
crop_mapping = dict(enumerate(data['crop'].cat.categories))
data['crop'] = data['crop'].cat.codes

# Water usage encoding
data['water_usage'] = data['water_usage'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Features and target
X = data[['rainfall', 'temperature', 'crop', 'water_usage']]
y = data['groundwater']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model + crop mapping
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(crop_mapping, open("crop_mapping.pkl", "wb"))

print("✅ Model trained and saved!")
print("📊 Crop mapping:", crop_mapping)