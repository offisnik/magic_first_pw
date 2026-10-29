from faker import Faker

faker = Faker()

def username():
    return faker.user_name()

def email():
    return faker.email()

def password():
    return faker.password(10)
