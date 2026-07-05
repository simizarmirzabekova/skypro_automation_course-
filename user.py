class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_first_name(self):
        print(self.first_name)

    def display_last_name(self):
        print(self.last_name)

    def display_full_name(self):
        print(f"{self.first_name} {self.last_name}")
        