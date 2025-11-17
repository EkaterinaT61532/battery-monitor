import psutil

def format_time(seconds):
    if seconds == psutil.POWER_TIME_UNLIMITED or seconds < 0:
        return "Unknown"
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}"

def main():
    battery = psutil.sensors_battery()

    if not battery:
        print("⚠️ Battery info not available.")
        return

    percent = battery.percent
    plugged = battery.power_plugged
    time_left = format_time(battery.secsleft)

    print(f"🔋 Battery: {percent}%")
    print(f"⚡ Status: {'Charging' if plugged else 'Discharging'}")
    print(f"⏳ Time left: {time_left}")

if __name__ == "__main__":
    main()
