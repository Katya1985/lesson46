first = 'Мама мыла раму'
second = 'Рамена мало было'
a = lambda x, y : list(map(x + y, first, second))


def get_advanced_writer(file_name):
    def write_everything(*data_set):   # *data_set - параметр принимающий неограниченное количество данных любого типа
        # self.data_set = data_set
        file_name = data_set
    return write_everything
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

from random import choice
# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

