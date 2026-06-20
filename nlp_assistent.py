import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

print("=" * 50)
print("🚁 AI Drone NLP Assistant")
print("=" * 50)

problem = input("\nDescribe Drone Problem: ").lower()

# Feature Extraction
yaw = 0
gps = 0
motor = 0
vibration = 0

# Yaw Keywords
if any(word in problem for word in [
    "yaw", "rotate", "rotating", "spinning", "spin"
]):
    yaw = 1

# GPS Keywords
if any(word in problem for word in [
    "gps", "hdop", "satellite", "location"
]):
    gps = 1

# Motor Keywords
if any(word in problem for word in [
    "motor", "hot", "overheating", "heat"
]):
    motor = 1

# Vibration Keywords
if any(word in problem for word in [
    "vibration", "shake", "shaking", "vibrate"
]):
    vibration = 1

# Create DataFrame
input_data = pd.DataFrame(
    [[yaw, gps, motor, vibration]],
    columns=["yaw", "gps", "motor_hot", "vibration"]
)

# Prediction
fault = model.predict(input_data)[0]

# Solutions
solutions = {
    "Compass": "Recalibrate compass using Mission Planner.",
    "GPS": "Check GPS wiring and antenna placement.",
    "ESC": "Inspect ESC temperature and recalibrate ESCs.",
    "MotorDirection": "Verify CW and CCW motor rotation.",
    "Propeller": "Inspect and replace damaged propellers."
}

print("\n🔍 Diagnosis Result")
print("-" * 30)
print("Fault:", fault)

if fault in solutions:
    print("Solution:", solutions[fault])

print("-" * 30)