class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age


class AgeValidator:
    @staticmethod
    def validate(age):
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130")


class UserDisplay:
    @staticmethod
    def display(user):
        print(f"{user.name} {user.last_name} {user.age}")


class UserInput:
    @staticmethod
    def input_user_data(user):
        user.name = input("Input name: ")
        user.last_name = input("Input last name: ")
        while True:
            try:
                age = int(input("Input age: "))
                AgeValidator.validate(age)
                user.age = age
                break
            except ValueError as e:
                print(e)


# Usage example
user = User("Bill", "Windows", 34)
UserDisplay.display(user)
UserInput.input_user_data(user)
UserDisplay.display(user)
