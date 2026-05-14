import random
import pandas as pd
import joblib
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def generate_test_data(samples=1000):
    data = []

    for _ in range(samples):
        temperature = random.uniform(20, 100)
        vibration = random.uniform(0, 15)
        rpm = random.uniform(1000, 3000)

        if temperature > 90 or vibration > 10 or rpm > 2600:
            label = "critical"
        elif temperature > 70 or vibration > 6 or rpm > 2200:
            label = "warning"
        elif random.random() < 0.05:
            label = "anomaly"
        else:
            label = "normal"

        data.append([temperature, vibration, rpm, label])

    return pd.DataFrame(
        data,
        columns=["temperature", "vibration", "rpm", "label"]
    )


model = joblib.load("models/fault_classifier.joblib")

df = generate_test_data()
X = df[["temperature", "vibration", "rpm"]]
y_true = df["label"]

y_pred = model.predict(X)

print("Model Evaluation")
print("================")
print(f"Accuracy: {accuracy_score(y_true, y_pred):.3f}")
print()
print(classification_report(y_true, y_pred))
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8,6))
plt.imshow(cm)

plt.xticks(
    range(4),
    ["normal","warning","critical","anomaly"]
)

plt.yticks(
    range(4),
    ["normal","warning","critical","anomaly"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Fault Classifier Confusion Matrix")

for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, cm[i,j])

plt.savefig("assets/confusion_matrix.png")

print("Confusion matrix saved.")
plt.show()