# ============================================================
# WHERE IS MY BUS + VEYIL
# ML PROJECT - LIST, TUPLE, DICTIONARY, SET
# ============================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor


# ============================================================
# 1. LIST
# ============================================================
# List containing multiple bus records

buses = [
    ["B001", "Kozhikode-Koyilandy", 32, 4.5, "Low", "Clear", "North", 10],
    ["B002", "Kozhikode-Ramanattukara", 25, 3.2, "High", "Cloudy", "South", 14],
    ["B003", "Kozhikode-Thamarassery", 28, 5.8, "Medium", "Clear", "East", 16],
    ["B004", "Kozhikode-Balussery", 30, 2.7, "Low", "Rain", "North", 9],
    ["B005", "Kozhikode-Feroke", 20, 6.2, "High", "Rain", "South", 20],
    ["B006", "Kozhikode-Kunnamangalam", 35, 3.5, "Medium", "Clear", "East", 11],
    ["B007", "Kozhikode-Koyilandy", 27, 4.0, "Medium", "Cloudy", "North", 13],
    ["B008", "Kozhikode-Ramanattukara", 22, 5.0, "High", "Clear", "South", 18],
    ["B009", "Kozhikode-Thamarassery", 31, 2.9, "Low", "Clear", "East", 8],
    ["B010", "Kozhikode-Balussery", 24, 4.8, "Medium", "Rain", "North", 15]
]


# ============================================================
# 2. TUPLE
# ============================================================
# Tuple for fixed GPS coordinates

bus_location = (11.2588, 75.7804)

print("\n==============================")
print("BUS LOCATION - TUPLE")
print("==============================")

print("Latitude :", bus_location[0])
print("Longitude:", bus_location[1])


# ============================================================
# 3. DICTIONARY
# ============================================================
# Dictionary containing detailed information about one bus

bus_details = {
    "bus_id": "B001",
    "route": "Kozhikode-Koyilandy",
    "speed": 32,
    "distance": 4.5,
    "traffic": "Low",
    "weather": "Clear",
    "direction": "North"
}

print("\n==============================")
print("BUS DETAILS - DICTIONARY")
print("==============================")

print("Bus ID    :", bus_details["bus_id"])
print("Route     :", bus_details["route"])
print("Speed     :", bus_details["speed"], "km/h")
print("Distance  :", bus_details["distance"], "km")
print("Traffic   :", bus_details["traffic"])
print("Weather   :", bus_details["weather"])
print("Direction :", bus_details["direction"])


# ============================================================
# 4. SET
# ============================================================
# Set stores only unique values

routes = {
    "Kozhikode-Koyilandy",
    "Kozhikode-Ramanattukara",
    "Kozhikode-Thamarassery",
    "Kozhikode-Balussery",
    "Kozhikode-Feroke",
    "Kozhikode-Kunnamangalam",
    "Kozhikode-Koyilandy"
}

print("\n==============================")
print("UNIQUE ROUTES - SET")
print("==============================")

for route in routes:
    print(route)


# ============================================================
# 5. CONVERT LIST INTO PANDAS DATAFRAME
# ============================================================

columns = [
    "bus_id",
    "route",
    "speed",
    "distance",
    "traffic",
    "weather",
    "direction",
    "eta"
]

df = pd.DataFrame(buses, columns=columns)

print("\n==============================")
print("DATASET")
print("==============================")

print(df)


# ============================================================
# 6. LABEL ENCODING
# ============================================================
# Convert text values into numbers for ML

traffic_encoder = LabelEncoder()
weather_encoder = LabelEncoder()
direction_encoder = LabelEncoder()

df["traffic_encoded"] = traffic_encoder.fit_transform(df["traffic"])
df["weather_encoded"] = weather_encoder.fit_transform(df["weather"])
df["direction_encoded"] = direction_encoder.fit_transform(df["direction"])


print("\n==============================")
print("ENCODED DATA")
print("==============================")

print(df)


# ============================================================
# 7. MACHINE LEARNING
# ============================================================
# Predict Bus ETA

features = [
    "speed",
    "distance",
    "traffic_encoded",
    "weather_encoded",
    "direction_encoded"
]

X = df[features]
y = df["eta"]


# Create ML model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X, y)


# ============================================================
# 8. USER INPUT
# ============================================================

print("\n==============================")
print("BUS ETA PREDICTION")
print("==============================")

speed = float(input("Enter bus speed (km/h): "))
distance = float(input("Enter distance to your stop (km): "))

print("\nTraffic Options: Low / Medium / High")
traffic = input("Enter traffic level: ")

print("\nWeather Options: Clear / Cloudy / Rain")
weather = input("Enter weather: ")

print("\nDirection Options: North / South / East / West")
direction = input("Enter bus direction: ")


# Encode user inputs

traffic_value = traffic_encoder.transform([traffic])[0]
weather_value = weather_encoder.transform([weather])[0]
direction_value = direction_encoder.transform([direction])[0]


# Create input for ML model

new_bus = [[
    speed,
    distance,
    traffic_value,
    weather_value,
    direction_value
]]


# Predict ETA

predicted_eta = model.predict(new_bus)[0]


# ============================================================
# 9. VEYIL / SUNLIGHT SYSTEM
# ============================================================

print("\n==============================")
print("VEYIL - SUNLIGHT PREDICTION")
print("==============================")

sun_direction = input(
    "Enter sun direction (North/South/East/West): "
)


# Simple sunlight-side logic

if sun_direction == direction:
    sun_side = "FRONT"

elif (
    (direction == "North" and sun_direction == "East") or
    (direction == "East" and sun_direction == "South") or
    (direction == "South" and sun_direction == "West") or
    (direction == "West" and sun_direction == "North")
):
    sun_side = "RIGHT"

else:
    sun_side = "LEFT"


# ============================================================
# 10. FINAL RESULT
# ============================================================

print("\n====================================")
print("        WHERE IS MY BUS + VEYIL")
print("====================================")

print("Bus Speed       :", speed, "km/h")
print("Distance        :", distance, "km")
print("Traffic         :", traffic)
print("Weather         :", weather)
print("Bus Direction   :", direction)

print("------------------------------------")

print("Predicted ETA   :", round(predicted_eta, 2), "minutes")

print("------------------------------------")

print("Sun Direction   :", sun_direction)
print("Sunlight Side   :", sun_side)

if sun_side == "LEFT":
    print("Recommended Seat: RIGHT SIDE")

elif sun_side == "RIGHT":
    print("Recommended Seat: LEFT SIDE")

else:
    print("Recommended Seat: SIDE SEAT AWAY FROM FRONT")

print("====================================")