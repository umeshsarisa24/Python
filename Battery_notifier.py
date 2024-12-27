# pip install psutil win10toast
import psutil
from win10toast import ToastNotifier

# Check battery status
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

# Initialize the toaster
toaster = ToastNotifier()

if percent <= 20 and not plugged:
    # Display a notification
    toaster.show_toast(
        "Battery Low",
        f"{percent}% battery remaining! Please plug in your charger.",
        duration=5,  # Duration in seconds
        threaded=True  # Allows the script to continue running while the notification is shown
    )

# Additional optional message
print("Notification sent (if conditions met).")
