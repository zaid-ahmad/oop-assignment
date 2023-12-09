class Appointment:
    '''A Class that represents appointment for Jojo's Hair Salon'''

    def __init__(self, day_of_week, start_time_hour):
        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = 0
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour

    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour

    def get_appt_type_desc(self):
        appt_types = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring"
        }
        return appt_types.get(self.__appt_type, "Invalid Appointment Type")

    def get_end_time_hour(self):
        return self.__start_time_hour + 1

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def set_appt_type(self, appt_type):
        self.__appt_type = appt_type

    def schedule(self, client_name, client_phone, appt_type):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type

    def cancel(self):
        self.__client_name = ''
        self.__client_phone = ''
        self.__appt_type = 0

    def format_record(self):
        return f"{self.__client_name}, {self.__client_phone}, {self.__appt_type}, {self.__day_of_week}, {self.__start_time_hour:02d}"

    def __str__(self):
        return f"{self.__client_name:<19} {self.__client_phone:<14} {self.__day_of_week:<9} {self.__start_time_hour:02}:00 - {self.get_end_time_hour():02}:00       {self.get_appt_type_desc()}"
