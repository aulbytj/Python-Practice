
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def talk(self):
        print(f"Hi {self.firstname} {self.lastname} nice to me you.")


first_person = Person("Aulbourn", "Knowles")
second_person = Person("Mary", "Jane")

first_person.talk()
second_person.talk()