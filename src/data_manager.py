import os
import json
from abstract_manager import AbstractDataManager


class DataManager(AbstractDataManager):
    """
    Класс для работы с файлами
    """

    def __init__(self, filename: object) -> object:
        """
        Задает путь к файлу
        """
        self.filename = filename

    def add_job(self, value):
        """
        Добавляет данные в файл
        """
        with open(self.filename, 'a', encoding='UTF-8') as file:
            json.dump(value, file, indent=2, ensure_ascii=False)
            file.write('\n')

    def open_file(self):
        """
        Открывает файл для чтения
        """
        with open(self.filename, 'r', encoding='UTF-8') as file:
            return json.load(file)

    def delete_job(self):
        """
        Полностью очищает файл
        """
        open(self.filename, 'w').close()
        os.remove(self.filename)