from abc import ABC, abstractmethod
import requests
from src.Vacancy import Vacancy  # Исправленный импорт

class JobApi(ABC):
    url: str

    def __init__(self, url):
        self.url = url

    @abstractmethod
    def get_vacancies(self):
        pass

class HeadHunterApi(JobApi):
    def __init__(self):
        super().__init__("https://api.hh.ru/vacancies")

    def get_vacancies(self, params=None):
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            data = response.json()
            if "items" not in data:
                raise ValueError("Ответ API не содержит вакансий")
            data = data["items"]
            vacancies = []
            for item in data:
                salary = item.get("salary")
                salary_value = (
                    salary["from"] if salary and salary.get("from") else 0
                )
                vacancy = Vacancy(
                    name=item.get("name", "Название не указано"),
                    vacancy_url=item.get("alternate_url", ""),
                    salary=salary_value,
                    description=item.get("snippet", {}).get("responsibility", "")
                                or item.get("snippet", {}).get("requirement", ""),
                )
                vacancies.append(vacancy)
            return vacancies
        except requests.RequestException as e:
            raise Exception(f"Ошибка при запросе к API: {e}")

if __name__ == "__main__":
    hh = HeadHunterApi()
    vacancies = hh.get_vacancies({"text": "Python", "per_page": 5})
    for vacancy in vacancies:
        print(vacancy)
        print()