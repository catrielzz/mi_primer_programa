from datetime import datetime


class Contact:
    def __init__(self, name, surname, phone, email, born_date):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.born_date = datetime.strptime(born_date, "%d/%m/%Y")

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_age(self):
        today = datetime.today()
        return today.year - self.born_date.year - \
               ((today.month, today.day) < (self.born_date.month, self.born_date.day))


contact = Contact("Yoel", "Estrada", "1168662684", "estradyoel@gmail.com", "08/11/1996")

print(contact.name)
print(contact.get_full_name())
print(contact.get_age())
