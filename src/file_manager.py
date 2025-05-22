import json
import os
from abc import ABC, abstractmethod
from src.Vacancy import Vacancy


class AbstractFile(ABC):
    @abstractmethod
    def add_vacancy(self, data, file_path):
        pass

    @abstractmethod
    def get_vacancy(self, file_path):
        pass

    @abstractmethod
    def delete_vacancy(self, file_path):
        pass


class FileManager(AbstractFile):
    def add_vacancy(self, data, file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        vacancies = []
        try:
            with open(file_path, "r", encoding="UTF-8") as f:
                vacancies = json.load(f)
                if not isinstance(vacancies, list):
                    vacancies = []
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        if isinstance(data, Vacancy):
            data = data.to_dict()
        vacancies.append(data)
        with open(file_path, "w", encoding="UTF-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)

    def get_vacancy(self, file_path, criteria=None):
        try:
            with open(file_path, "r", encoding="UTF-8") as f:
                vacancies = json.load(f)
                if not isinstance(vacancies, list):
                    return []
                if criteria:
                    keyword = criteria.get("keyword")
                    if keyword:
                        return [
                            v for v in vacancies
                            if keyword.lower() in v.get("description", "").lower()
                        ]
                return vacancies
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def delete_vacancy(self, file_path, criteria=None):
        vacancies = self.get_vacancy(file_path)
        if criteria:
            url = criteria.get("url")
            if url:
                vacancies = [v for v in vacancies if v.get("vacancy_url") != url]
        with open(file_path, "w", encoding="UTF-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=2)

    #Нам сказали добавить заглушку
    def connect_to_db(self):
        # Заглушка для подключения к БД
        pass

    def save_to_db(self, data):
        # Заглушка для сохранения в БД
        pass