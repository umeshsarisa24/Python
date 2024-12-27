from datetime import datetime, timedelta
import time


def calculate_age_live(dob):
    while True:
        current_time = datetime.now()
        age = current_time - dob

        # Extract years, months, days, hours, minutes, and seconds
        years = age.days // 365
        remaining_days = age.days % 365
        months = remaining_days // 30
        days = remaining_days % 30
        hours = age.seconds // 3600
        minutes = (age.seconds % 3600) // 60
        seconds = age.seconds % 60

        # Display the live age
        print(f"\rYou are {years} years, {months} months, {days} days, "
              f"{hours} hours, {minutes} minutes, {seconds} seconds old.", end="")

        # Wait for 1 second before updating
        time.sleep(1)


# Input your date of birth
dob_input = input("Enter your date of birth (YYYY-MM-DD HH:MM:SS): ")
dob = datetime.strptime(dob_input, "%Y-%m-%d %H:%M:%S")

# Start the live age calculator
calculate_age_live(dob)
