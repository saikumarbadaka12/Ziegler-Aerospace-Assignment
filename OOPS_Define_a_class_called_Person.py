class Person:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.mobile = input("Enter mobile number: ")

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile:", self.mobile)

# Test
person = Person()
person.display_info()
