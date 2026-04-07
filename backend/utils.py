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

    low_water = ["Maize ", "Potato "]
    medium_water = ["Wheat ", "Cotton ", "Kinnow ", "Litchi "]
    high_water = ["Paddy ", "Sugarcane "]

    if groundwater < 10:
        return f"✅ Good Water Availability\nWater is near the surface.\nRecommended: {', '.join(low_water)}\nAlso Suitable: {', '.join(medium_water)}\nUse high water crops carefully."

    elif groundwater < 20:
        return f"⚠️ Moderate Water Level\nWater is slightly deeper.\nRecommended: {', '.join(medium_water)}\nAvoid: {', '.join(high_water)}"

    elif groundwater < 30:
        return f"⚠️ Depleting Water Level\nWater is getting deeper.\nRecommended: {', '.join(low_water)}\nStrictly Avoid: {', '.join(high_water)}"

    else:
        return f"🚨 Severe Depletion\nWater is very deep.\nOnly grow: {', '.join(low_water)}\nAvoid all high water crops."