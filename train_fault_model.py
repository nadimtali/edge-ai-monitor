import random
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = []

for _ in range(3000):

    temperature = random.uniform(20,100)
    vibration = random.uniform(0,15)
    rpm = random.uniform(1000,3000)

    if temperature > 90 or vibration > 10 or rpm > 2600:
        label = "critical"

    elif temperature > 70 or vibration > 6 or rpm > 2200:
        label = "warning"

    elif random.random() < 0.05:
        label = "anomaly"

    else:
        label = "normal"

    data.append([
        temperature,
        vibration,
        rpm,
        label
    ])

df = pd.DataFrame(
    data,
    columns=["temperature","vibration","rpm","label"]
)

X = df[["temperature","vibration","rpm"]]
y = df["label"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

joblib.dump(
    model,
    "models/fault_classifier.joblib"
)

print("Model saved.")