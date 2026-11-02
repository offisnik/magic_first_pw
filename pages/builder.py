from faker import Faker
import random

faker = Faker()

def username():
    return faker.user_name()

def email():
    return faker.email()

def password(length=10):
    return faker.password(length)

def phone():
    return Faker('ru_RU').phone_number()

def rand_int(a=1):
    return random.randint(a, 6)
