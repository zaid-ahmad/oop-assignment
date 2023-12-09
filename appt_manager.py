from appointment import Appointment


def create_weekly_calendar():
    calendar = []
    days_in_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday"]
    for day in days_in_week:
        for hour in range(9, 17):
            appointment = Appointment("", "", 0, day, hour)
            calendar.append(appointment)
    return calendar


def print_menu():
    print("Jojo's Hair Salon Appointment Manager")
    print("="*37)
    print("1) Schedule an appointment")
    print("2) Find appointment by name")
    print("3) Print calendar for a specific day")
    print("4) Cancel an appointment")
    print("5) Exit the system")
    input("Enter your selection: ")
