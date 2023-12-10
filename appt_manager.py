import appointment as ap
from os import path
import sys

DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday")
FIRST_HOUR_OF_DAY = 9
LAST_HOUR_OF_DAY = 16


def create_weekly_calendar(appt_cal):
    appt_cal.clear()
    for index in range(len(DAYS_OF_WEEK)):
        for time in range(FIRST_HOUR_OF_DAY, LAST_HOUR_OF_DAY+1):
            appt = ap.Appointment(DAYS_OF_WEEK[index], time)
            appt_cal.append(appt)


def load_scheduled_appointments(appt_cal: list[ap.Appointment]):
    file_name = input("Enter appointment filename: ")
    while not path.isfile(file_name):
        file_name = input("File not found. Re-enter appointment filename: ")

    file = open(file_name, "r")

    num_imported = 0

    for line in file:
        line = line.rstrip()
        line_items = line.split(",")
        appt = find_appointment_by_time(
            appt_cal, line_items[3], int(line_items[4]))
        if appt is not None:
            appt.schedule(line_items[0], line_items[1], int(line_items[2]))
            num_imported += 1

    print(f"{num_imported} previously scheduled appointments have been loaded")
    file.close()


def print_menu():
    print("\n")

    print("""Jojo's Hair Salon Appointment Manager
=====================================
 1) Schedule an appointment
 2) Find appointment by name
 3) Print calendar for a specific day
 4) Cancel an appointment
 9) Exit the system""")
    opt = int(input("Enter your selection: "))
    return opt


def find_appointment_by_time(appt_cal: list[ap.Appointment], day_of_week, start_hour):
    for appt in appt_cal:
        if appt.get_day_of_week() == day_of_week and appt.get_start_time_hour() == start_hour:
            return appt

    return None


def show_appointments_by_name(appt_cal: list[ap.Appointment], client_name):
    found_appts = []
    for appt in appt_cal:
        if appt.get_client_name().lower().startswith(client_name.lower()):
            found_appts.append(appt)

    print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
                                                        "Phone", "Day", "Start", "End", "Type"))
    print("-" * 85)

    if len(found_appts) == 0:
        print("No appointments found.")
        return False

    for appt in found_appts:
        print(appt)

    return True


def show_appointments_by_day(appt_cal: list[ap.Appointment], day_of_week):
    found_appts = []
    for appt in appt_cal:
        if appt.get_day_of_week().lower() == day_of_week.lower():
            found_appts.append(appt)

    print("{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
                                                        "Phone", "Day", "Start", "End", "Type"))
    print("-" * 85)

    for appt in found_appts:
        print(appt)

    return True


def save_scheduled_appointments(appt_cal: list[ap.Appointment]):
    file_name = input("Enter appointment filename: ")
    overwrite = False
    while path.isfile(file_name) and not overwrite:
        overwrite_choice = input(
            "File already exists. Do you want to overwrite it (Y/N)? ").lower()
        if overwrite_choice == "y":
            overwrite = True
        elif overwrite_choice == "n":
            overwrite = False
        file_name = input("Enter appointment filename: ")
        overwrite = False

    file = open(file_name, "w")

    num_exported = 0

    for appt in appt_cal:
        if appt.get_appt_type() != 0:
            file.write(f"{appt.format_record()}\n")
            num_exported += 1

    print(f"{num_exported} scheduled appointments have been successfully saved")
    file.close()


def main():
    appt_calendar = []
    selection = 0
    print("Starting the Appointment Manager System")

    create_weekly_calendar(appt_calendar)
    print("Weekly calendar created")

    load_flag = input(
        "Would you like to load previously scheduled appointments from a file (Y/N)? ")

    while not load_flag.lower() in "yn":
        load_flag = input(
            "Would you like to load previously scheduled appointments from a file (Y/N)? ")

    if load_flag.lower() == "y":
        load_scheduled_appointments(appt_calendar)

    selection = print_menu()

    while selection != 9:

        if selection == 1:
            print("\n** Schedule an appointment **")
            schedule_appointment(appt_calendar)

        elif selection == 2:
            print("\n** Find appointment by name **")
            name = input("Enter Client Name: ")
            print(f"Appointments for {name}\n")
            show_appointments_by_name(appt_calendar, name)

        elif selection == 3:
            print("\n** Print calendar for a specific day **")
            day = input("What day: ")
            print(f"Appointments for {day.title()}\n")
            show_appointments_by_day(appt_calendar, day)

        elif selection == 4:
            print("\n** Cancel an appointment **")
            day = input("What day: ")
            hour = int(input("Enter start hour: "))
            appt = find_appointment_by_time(
                appt_calendar, day.title(), int(hour))
            if appt is not None:
                if appt.get_appt_type() != 0:
                    print(
                        f"Appointment: {appt.get_day_of_week()} {appt.get_start_time_hour()}:00 - {appt.get_end_time_hour()}:00 for {appt.get_client_name()} has been cancelled!")
                    appt.cancel()
                else:
                    print(
                        "That time slot isn't booked and doesn't need to be cancelled")
            else:
                print("Sorry that time slot is not in the weekly calendar!")

        elif selection != 9:
            print("\nInvalid option")

        selection = print_menu()

    print("\n** Exit the system **")
    save_flag = input(
        "Would you like to save all scheduled appointments to a file (Y/N)? ")
    while not save_flag.lower() in "yn":
        save_flag = input(
            "Would you like to save all scheduled appointments to a file (Y/N)? ")

    if save_flag.lower() == "y":
        save_scheduled_appointments(appt_calendar)

    print("Good Bye!")
    sys.exit()


def schedule_appointment(appt_calendar):
    day = input("What day: ").title()
    hour = int(input("Enter start hour (24 hour clock): "))
    appt = find_appointment_by_time(appt_calendar, day, hour)

    if appt == None:
        print("Sorry that time slot is not in the weekly calendar!")
        return False

    if appt.get_appt_type_desc() != "Available":
        print("Sorry that time slot is booked already!")
        return False

    name = input("Client Name: ")
    phone = input("Client Phone: ")

    print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
    type = int(input("Type of Appointment: "))

    if not type in (1, 2, 3, 4):
        print("Sorry that is not a valid appointment type!")
        return False

    appt.schedule(name, phone, type)

    print(f"OK, {name}'s appointment is scheduled!")
    return True


if __name__ == '__main__':
    main()
