# Домашнее задание по теме "Интроспекция"

import inspect
from pprint import pprint


def introspection_info(obj):
    """Функция для проведения интроспекции объекта.

    Аргументы:
        obj (any): Объект любого типа, который нужно проанализировать.

    Возвращает:
        dict: Словарь с информацией об объекте, включая его тип, атрибуты,
              методы, модуль и другие свойства.
    """

    # Получаем тип объекта
    type_ = type(obj).__name__

    # Получаем все атрибуты объекта
    attributes = dir(obj)

    # Фильтруем только методы объекта
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Определяем модуль, к которому относится объект
    module = getattr(obj, "__module__", None)

    # Дополнительно можно добавить проверку специфических свойств объекта
    # Например, если это строка, можем получить длину
    additional_properties = {}
    if isinstance(obj, str):
        additional_properties["length"] = len(obj)

    return {
        "type": type_,
        "attributes": attributes,
        "methods": methods,
        "module": module,
        "additional_properties": additional_properties
    }


class MyClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        print("Это метод!")


if __name__ == '__main__':
    # Создаем экземпляр класса
    my_object = MyClass(42)

    # Проводим интроспекцию объекта
    info = introspection_info(my_object)

    # Выводим результат
    for key, value in info.items():
        pprint(f"{key}: {value}")