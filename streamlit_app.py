import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🚁 AI Drone Fault Diagnosis Assistant")

yaw = st.selectbox(
    "Yaw Problem?",
    ["No", "Yes"]
)

gps = st.selectbox(
    "GPS Problem?",
    ["No", "Yes"]
)

motor = st.selectbox(
    "Motor Hot?",
    ["No", "Yes"]
)

vibration = st.selectbox(
    "High Vibration?",
    ["No", "Yes"]
)

if st.button("Predict Fault"):

    yaw_val = 1 if yaw == "Yes" else 0
    gps_val = 1 if gps == "Yes" else 0
    motor_val = 1 if motor == "Yes" else 0
    vibration_val = 1 if vibration == "Yes" else 0

    fault = model.predict(
        [[yaw_val, gps_val, motor_val, vibration_val]]
    )[0]

    st.success(f"Most Likely Fault: {fault}")

    solutions = {
        "Compass":"Recalibrate compass using Mission Planner.",
        "GPS":"Check GPS wiring and antenna placement.",
        "ESC":"Inspect ESC temperature and recalibrate ESCs.",
        "MotorDirection":"Verify CW/CCW motor rotation.",
        "Propeller":"Inspect and replace damaged propellers."
    }

    st.write("### Recommended Solution")
    st.write(solutions.get(fault, "No solution available"))