class SystemReporter:

    @staticmethod
    def print_summary(readings, system_status):

        statuses = [reading["status"] for reading in readings]

        ok_count = statuses.count("OK")
        warning_count = statuses.count("WARNING")
        critical_count = statuses.count("CRITICAL")
        ai_count = statuses.count("AI ALERT")

        print("\n==============================")
        print(f"System Status: {system_status}")
        print(
            f"OK: {ok_count} | "
            f"WARNING: {warning_count} | "
            f"CRITICAL: {critical_count} | "
            f"AI ALERT: {ai_count}"
        )

        print("------------------------------")

        for reading in readings:
            print(
                f"{reading['name']}: "
                f"{reading['value']} {reading['unit']} "
                f"[{reading['status']}] "
                f"(AI score: {reading['ai_score']})"
            )

        print("==============================")