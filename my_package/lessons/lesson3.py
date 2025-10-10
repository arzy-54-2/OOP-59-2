# Инкапсуляция
import random

class BankAccount:

    def __init__(self, user_name, password, balance):
        self.user_name = user_name
        self._balance = balance # Защищенный атрибут _
        self.__password = password # Приватный атрибут __

    def new_pass(self, new_pass):
        self.__password = new_pass
        return 'Pass updated!!'

    def get_balance(self):
        return self._balance

    def __get_random_pass(self):
        return random.randint(1,10)

    def generate_pass(self):
        return self.__get_random_pass()

john = BankAccount("John", "Def123321", 10000)

# print(john._BankAccount__password)
# print(john.new_pass("123321"))
# print(john._BankAccount__password)
# print(john._BankAccount__get_random_pass())


# Абстракция

from abc import ABC, abstractmethod

# Абстрактный класс
class OTPSms(ABC):

    @abstractmethod
    def send_sms_phone(self):
        pass

class KGSms(OTPSms):

    def __init__(self, name):
        self.name = name
    def send_sms_phone(self):

        text = '''
            <Phone>+996779280699<Phone/>
            <Text>Ваш код для регистрации: 123321<Text/>
        '''

class RUSms(OTPSms):

    def send_sms_phone(self):
        text = {
            "phone": "+79911233232",
            "text": "Ваш код для регистрации: 123321"
        }


import lesson2
from lesson2 import Hero

hero = lesson2.Hero("Ardager", 100, 1000)

print(hero.action())
from random import randint

