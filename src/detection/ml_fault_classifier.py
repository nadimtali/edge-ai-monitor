import joblib
import pandas as pd


class MLFaultClassifier:

    def __init__(self):
        self.model = joblib.load(
            "models/fault_classifier.joblib"
        )

    def classify(
        self,
        temperature,
        vibration,
        rpm
    ):

        sample = pd.DataFrame([{
            "temperature": temperature,
            "vibration": vibration,
            "rpm": rpm
        }])

        prediction = self.model.predict(sample)[0]

        return prediction