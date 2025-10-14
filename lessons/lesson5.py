# # class Test:
# #     # Магический метод
# #     def __init__(self, name):
# #         self.name = name
# #
# #     def __str__(self):
# #         return self.name
# #
# # class MyInt:
# #     def __init__(self, value):
# #         self.value = value
# #
# #     def __str__(self):
# #         return self.value
# #
# # test3 = MyInt(123)
# # test4 = 123
# #
# # print(test4)
#
#
#
# # class Money:
# #
# #     def __init__(self, amount, currency):
# #         self.amount = amount
# #         self.currency = currency
# #
# #     #      +
# #     def __add__(self, other):
# #         if self.currency == other.currency:
# #             print(self.amount + other.amount)
# #         else:
# #             print(f"Currency error")
# #     #      <
# #     def __lt__(self, other):
# #         print(self.amount)
# #         print(other.amount)
# #
# #     #      >
# #     def __gt__(self, other):
# #         print(self.amount)
# #         print(other.amount)
# #
# #
# #
# # USD = Money(100, "USD")
# #
# # SOM = Money(100, "SOM")
# #
# # new_obj = SOM > USD
#
#
# class MyList:
#
#     def __init__(self, values: list):
#         self.values = values
#
#     # def __new__(cls, *args, **kwargs):
#
#     # def __call__():
#
#     def __setitem__(self, key, value):
#         print(key)
#         print(value)
#
#     def __getitem__(self, item):
#         print(item)
#
#     # def __del__(self):
#
#
#
#
# test = [1,2,3,4,5,6]
# print(test)
# del test[1]
# print(test)
# # print(test)
# # test[1] = 123
# # print(test)
#
# # test2 = MyList([1,23,4,56,7])
#
# # test2[1] = 123
#
#
# # print(test2[1])



# class Test:
#     #  Атрибута класса
#     name = "Class Name"
#
#     def __init__(self, value):
#         # Атрибута экземпляра класса
#         self.value = value
#
#     def just_method(self):
#         print(f"{self.value} я отработал" )
#
#     @staticmethod
#     def static_method():
#         print("я отработал!!")
#
#     @classmethod
#     def class_method(cls):
#         print(cls.name)
#
#     @property
#     def property_method(self):
#         return "Atrebut"

# objects = Test("test")
# print(objects.value)
# print(objects.just_method())
# print(objects.property_method)
# Test.static_method()
# Test.class_method()
# objects.just_method()



# class User:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return f"{self.last_name} {self.first_name}"
#
#
# john = User("John", "Doe")
#
# print(john.full_name)

