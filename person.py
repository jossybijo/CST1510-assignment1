
from datetime import date


class Person:
    """defining the class person"""
    def __init__(self, name, dob, address):
        """the constructor for the Person class"""
        self.name = name
        self.dob = dob
        self.address = address

    def age(self):
        """returns the current age of the person"""
        today = date.today()
        return self.find_age(today)

    def find_age(self, the_date):
        """returns the age of the person on the given date"""
        years = the_date.year - self.dob.year

        if (the_date.month, the_date.day) < (self.dob.month, self.dob.day):
            years -= 1

        return years

    def date_for_age(self, the_age):
        """returns the date when the person turns the given age"""
        return date(
            self.dob.year + the_age,
            self.dob.month,
            self.dob.day
        )

person1 = Person(
    "Jossy Bijo",
    date(2000, 12, 15),
    "Dubai, UAE"
)

person2 = Person(input("Enter name: "), 
                 date.fromisoformat(input("Enter date of birth (YYYY-MM-DD): ")), 
                 input("Enter address: "))

print("Name of person1:", person1.name)
print("Date of birth of person1:", person1.dob)
print("Address of person1:", person1.address)
print("Name of person2:", person2.name)
print("Date of birth of person2:", person2.dob)
print("Address of person2:", person2.address)


print("Current age:", person1.age())
print("Current age of person2:", person2.age())


print("Age on the date given:", person1.find_age(date(2026, 12, 18)))
print("Age on the date given for person2:", person2.find_age(date(2026, 12, 18)))

print("Date when Alice turns 30:", person1.date_for_age(30))
print("Date when person2 turns 30:", person2.date_for_age(30))