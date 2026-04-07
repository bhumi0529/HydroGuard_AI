crop_map = {'paddy': 0, 'wheat': 1, 'maize': 2}
water_map = {'low': 0, 'medium': 1, 'high': 2}

def encode_input(data):
    return [
        data['rainfall'],
        data['temperature'],
        crop_map[data['crop']],
        water_map[data['water_usage']]
    ]

def recommend_crop(groundwater):
    
    # Low water crops (safe when water is low)
    low_water = ["Maize 🌽", "Potato 🥔"]
    
    # Medium water crops
    medium_water = ["Wheat 🌾", "Cotton 🌿", "Kinnow 🍊", "Litchi 🍓"]
    
    # High water crops (avoid when water is low)
    high_water = ["Paddy 🌾🚫", "Sugarcane 🎋🚫"]

    # Decision based on groundwater level
    if groundwater < 10:
        return f"⚠️ Critical Water Level\nRecommended: {', '.join(low_water)}\nAvoid: {', '.join(high_water)}"
    
    elif groundwater < 20:
        return f"⚠️ Moderate Water Level\nRecommended: {', '.join(medium_water)}\nAvoid: {', '.join(high_water)}"
    
    elif groundwater < 30:
        return f"✅ Safe Level\nRecommended: {', '.join(medium_water + low_water)}"
    
    else:
        return f"💧 High Water Availability\nAll crops suitable including: {', '.join(high_water)}"