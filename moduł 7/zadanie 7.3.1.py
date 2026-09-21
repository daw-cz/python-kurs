from faker import Faker
fake = Faker('pl_PL')

class BaseContact:

    def __init__(self, name, surname, phone, mail):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}"

    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1

class BusinessContact(BaseContact):

    def __init__(self, company, position, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.work_phone = work_phone

    def contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.name} {self.surname}"

def create_contacts(card_type, quantity):
    contacts = []

    for _ in range(quantity):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.email()
        private_phone = fake.phone_number()

        if card_type == "base":
            new_card = BaseContact(
                name=name, surname=surname, phone=private_phone, mail=email
            )
        elif card_type == "business":
            company = fake.company()
            position = fake.job()
            work_phone = fake.phone_number()
            new_card = BusinessContact(
                company=company,
                position=position,
                work_phone=work_phone,
                name=name,
                surname=surname,
                phone=private_phone,
                mail=email,
            )

        contacts.append(new_card)

    return contacts



private_cards = create_contacts("base", 2)
for card in private_cards:
    print(card.contact())
    print(f"Długość etykiety: {card.label_length}\n")

business_cards = create_contacts("business", 2)
for card in business_cards:
    print(card.contact())
    print(f"Firma: {card.company}, Stanowisko: {card.position}")
    print(f"Długość etykiety: {card.label_length}\n")
