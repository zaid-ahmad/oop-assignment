class Appointment:
    '''A class that represents appointments for Jojo's Hair Salon.

    Attributes:
        __client_name (str): The name of the client.
        __client_phone (str): The phone number of the client.
        __appt_type (int): The index (from 'appt_types' dictionary) for the appointment type.
        __day_of_week (str): The day of the week for the appointment.
        __start_time_hour (int): The appointment's starting hour.

    Methods:
        schedule(client_name, client_phone, appt_type): Makes a new appointment for a client, updating client name, phone, and appointment type.
        cancel(): Cancels the current appointment, resetting client details and appointment type.
        get_client_name(): Retrieves the client's name.
        get_client_phone(): Retrieves the client's phone number.
        get_appt_type(): Retrieves the appointment type index.
        get_day_of_week(): Retrieves the day of the week for the appointment.
        get_start_time_hour(): Retrieves the starting hour of the appointment.
        get_appt_type_desc(): Retrieves a description of the appointment type based on its index.
        get_end_time_hour(): Calculates and retrieves the ending hour of the appointment based on the start time.
        set_client_name(client_name): Updates the client's name.
        set_client_phone(client_phone): Updates the client's phone number.
        set_appt_type(appt_type): Updates the appointment type index.
        format_record(): Formats and retrieves appointment details in a record format.

    Usage:
        Create an instance of the Appointment class to manage individual appointments for Jojo's Hair Salon.
        Use the schedule() method to set details for a new appointment.
        Utilize getters and setters to access or modify specific appointment attributes.
        Use cancel() to reset/cancel an existing appointment.
        The __str__() method provides a formatted display of the appointment details.

    Note:
        The 'appt_types' dictionary maps appointment type indices to their descriptions. 
        0: "Available",
        1: "Mens Cut",
        2: "Ladies Cut",
        3: "Mens Colouring",
        4: "Ladies Colouring"
        Any invalid appointment type index returns "Invalid Appointment Type".
    '''

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
