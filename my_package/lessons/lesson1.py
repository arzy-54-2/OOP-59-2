
def action():
    print('Base action!!')

action()
class Hero:

    # Метод класса
    def action(self):
        return print(f"{self.name} base action!!")

    def cast_spell(self):
        return print(f"Fire bool")


    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

asuna = Hero("Asuna", 99, 11000)

# kirito.cast_spell()
# asuna.cast_spell()
# print(asuna.hp)
# print(kirito.hp)
# print(kirito.h_name)

kirito = Hero("Kirito", 100, 1000)
integer = 123
strings = [123]

action()
kirito.action()

# print(type(kirito))
# print(type(integer))
# print(type(strings))