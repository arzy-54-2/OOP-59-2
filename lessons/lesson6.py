# 1. Что такое декоратор?
# Декоратор — это функция, которая принимает другую функцию как аргумент и
# возвращает новую функцию, обычно обернутую в дополнительную функциональность.

#                  def say_hello 2 - шаг
def simple_decorator(func):
    def wrapper():
        print("До выполнения!!") # - 3 шаг
        func() # say_hello()    # - 4 шаг
        print("После выполнения!!") # - 5 шаг
    return wrapper

# simple_decorator(say_hello) 1 - шаг
@simple_decorator
def say_hello():
    print('Hello')

# say_hello()
#                     def greeting()
def greeting_decorator(func):
    def wrapper(name):
        func(name)
        print(f"{name} как дела ?")
    return wrapper

# greeting_decorator(greeting)
#     def wrapper(name)
@greeting_decorator
def greeting(name):
    print(f"{name} привет")

# greeting("Ardager")  # - 1 щаг def greeting_decorator(greeting())
                        #           def wrapper("Ardager")

def repeat_decorator(n):
    def decorator(func):
        def wrapper(name):
            for i in range(n):
                func(name)
        return wrapper
    return decorator

@repeat_decorator(4)
def say_name(name):
    print(f"{name}")

# say_name("Ardager")  # - repeat_decorator(4)
                        #   def decorator(def say_name())
                            #   def wrapper("Ardager")
                                    # for i in range(4):
                                      #  say_name()
            #  class OldClass:
def class_decorator(OldClass):
    class NewClass(OldClass):
        def new_method(self):
            return "Я новый метод!!"
    return NewClass

@class_decorator
class OldClass:
    def old_method(self):
        return "я старый метод!!"


# obj_1 = OldClass()
#
# print(obj_1.new_method())
# print(obj_1)


# Привет (user_name, role, id, phone)
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

ardager = User("Ardager", "admin")

def is_admin(func):
    def wrapper(users, command):
        if users.role == "admin" and command == "ban":
            func(users,command)
        else:
            print("Вы не админ или такой команды нет !!")
    return wrapper

@is_admin
def ban(user, command):
    print(f'{user.name} забанил пользователя!!')

# ban(ardager, "ban")







# def find_element(array, target):
#     print(array[target])
#     for ind, num in enumerate(array):
#         if target == ind:
#             print('нашел')
#         else:
#             print("не нашел")
#
# find_element([1,23,4,5,5,64,7,3], 3)

# O (n)
# O (long n)
def find_element(array, target):
    left, right = 0, len(array) -1
    while left <= right:
        mid = (left + right) // 2
        print(f"LEFT: {left} == RIGHT: {right}")
        print(mid)
        if array[mid] == target:
            return print("Найден")
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print("не найден!!")

find_element([1,23,432,2,44,6,7,8,9,10,11], 1)


