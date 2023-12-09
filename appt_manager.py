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


def load_schedule_from_file(appointment_list):
    appt_filename = input('Enter filename: ')
    scheduled_count = 0

    try:
        with open(appt_filename, 'r') as file:
            for line in file:
                attributes = line.strip().split(',')
                if len(attributes) >= 4:
                    appointment_time = attributes[0]

                    found_appointment = find_appointment_by_time(
                        appointment_list, appointment_time)
                    if found_appointment is not None:
                        found_appointment.schedule(
                            attributes[1], attributes[2])

                        scheduled_count += 1

    except FileNotFoundError:
        print("File not found.")

    return scheduled_count
