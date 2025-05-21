from abc import ABC, abstractmethod
import requests


class JobApi(ABC):
    url: str

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterApi(JobApi):
    url: str

    def __init__(self):
        super().__init__("https://api.hh.ru/vacancies")

    def get_vacancies(self, params=None):
        try:
            response = requests.get(self.url, params=params)
            return response.json().get("items")
        except Exception as e:
            raise e


class Vacancy:
    name: str
    vacancy_url: str
    salary: int
    description: str

    def __init__(self, name, vacancy_url, salary, description):
        self.name = name
        self.vacancy_url = vacancy_url
        self.salary = salary
        self.description = description

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Данные не относятся к единому классу или типу")

        return other if isinstance(other, int) else other.salary

    def __eq__(self, other):
        obj = self.__verify_data(other)
        return self.salary == obj

    def __lt__(self, other):
        obj = self.__verify_data(other)
        return self.salary < obj

    def __le__(self, other):
        obj = self.__verify_data(other)
        return self.salary <= obj

    def __gt__(self, other):
        obj = self.__verify_data(other)
        return self.salary > obj

    def __ge__(self, other):
        obj = self.__verify_data(other)
        return self.salary >= obj


# alternate_url - ссылка на вакансию
# name - имя вакансии
# salary (from to) - зарплата
# snipper (responsobility, requarement) - описание


if __name__ == "__main__":
    hh = HeadHunterApi()
    vacanci = hh.get_vacancies()
    for i in vacanci:
        print(i)
        print()
    # obj1 = Vacancy("лорсит", "https:hiuy", 500, "9")
    # obj2 = Vacancy("лорсит", "https:hiuy", 500, "9")
    # print(obj1 <= obj2)
