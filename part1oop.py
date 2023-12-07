
class Appointment:
    print('='*50)
    print ("Jojo's Hair Salon Appointment Manager")
    print('='*50) 
    
    
    
def __init__(self, day, start_hour, client_name, client_phone, appointment_type):
        self.day = day
        self.start_hour = start_hour
        self.client_name = client_name
        self.client_phone = client_phone
        self.appointment_type = appointment_type

def __str__(self):
        return f"{self.client_name}'s appointment on {self.day} at {self.start_hour}:00 for a {self.appointment_type}"

def main():
    appointments = []

    while True:
        print("1) Schedule an appointment")
        print("2) Find appointment by name")
        print("3) Print calendar for specific days")
        print("4) Cancel an appointment")
        print("9) Exit the system")

        user_input = input("Enter your selection: ")

        if user_input == "1":
            day = input("What day: ")
            start_hour = input("Enter start hour (24 hour clock): ")
            client_name = input("Client Name: ")
            client_phone = input("Client Phone: ")
            print("Appointment types")
            print("1: Mens Cut $50")
            print("2: Ladies Cut $80")
            print("3: Mens Colouring $50")
            print("4: Ladies Colouring $120") 
            appointment_type = input("Type of Appointment: ")

            types = { "1": "Men's Cut",
                      "2": "Ladies Cut",
                      "3": "Men's Colouring",
                      "4": "Ladies Colouring" }
            appointment_type_text = types.get(appointment_type, "Unknown")

            new_appointment = Appointment(day, start_hour, client_name, client_phone, appointment_type_text)
            appointments.append(new_appointment)
            print("OK,", new_appointment)

        elif user_input == "2":
            name_to_find = input("Enter client name to find: ")
            found = False
            for appointment in appointments:
                if appointment.client_name.lower() == name_to_find.lower():
                    print(appointment)
                    found = True
            if not found:
                print("No appointment found for", name_to_find)

        elif user_input == "3":
            day_to_print = input("Enter day to print appointments for: ")
            for appointment in appointments:
                if appointment.day.lower() == day_to_print.lower():
                    print(appointment)

        elif user_input == "4":
            name_to_cancel = input("Enter client name to cancel appointment: ")
            appointments = [appointment for appointment in appointments if appointment.client_name.lower() != name_to_cancel.lower()]
            print("Appointments for", name_to_cancel, "cancelled.")

        elif user_input == "9":
            print("Exiting system.")
            break

if __name__ == "__main__":
    main()
def __str__(self):
        appt_type_desc = self.get_appt_type_desc()
        return f"{self.client_name:<20}{self.client_phone:<15}{self.day_of_week:<10}{self.start_time_hour:02}:00  -  {int(self.start_time_hour)+1:02}:00     {appt_type_desc}"

