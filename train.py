import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load Dataset
data = pd.read_csv("drone_data.csv")

# Features
X = data[["yaw", "gps", "motor_hot", "vibration"]]

# Target
y = data["fault"]

# Train Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save Model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ AI Model Trained Successfully")