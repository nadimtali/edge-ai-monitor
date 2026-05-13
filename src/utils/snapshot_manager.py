import os
from datetime import datetime
import matplotlib.pyplot as plt


class SnapshotManager:

    @staticmethod
    def save_snapshot(sensor_name, status):

        os.makedirs("snapshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"snapshots/{sensor_name}_{status}_{timestamp}.png"

        plt.savefig(filename)

        print(f"[SNAPSHOT] Saved: {filename}")