class Vacancy:
    name: str
    vacancy_url: str
    salary: int
    description: str

    def __init__(self, name, vacancy_url, salary, description):
        if not isinstance(name, str):
            raise ValueError("Название вакансии должно быть строкой")
        if not isinstance(vacancy_url, str):
            raise ValueError("Ссылка на вакансию должна быть строкой")
        if vacancy_url and not vacancy_url.startswith("http"):
            raise ValueError("Ссылка на вакансию должна быть валидным URL")
        if not isinstance(description, str):
            raise ValueError("Описание должно быть строкой")
        if salary is None:
            self.salary = 0
        elif not isinstance(salary, (int, float)):
            raise ValueError("Зарплата должна быть числом или None")
        else:
            self.salary = salary

        self.name = name
        self.vacancy_url = vacancy_url
        self.description = description

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, float, Vacancy)):
            raise TypeError("Сравнение возможно только с числом или объектом Vacancy")
        if isinstance(other, Vacancy):
            return other.salary if other.salary != 0 else 0
        return other

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

    def __str__(self):
        return (
            f"Вакансия: {self.name}\n"
            f"Ссылка: {self.vacancy_url}\n"
            f"Зарплата: {self.salary if self.salary != 0 else 'Зарплата не указана'}\n"
            f"Описание: {self.description}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "vacancy_url": self.vacancy_url,
            "salary": self.salary,
            "description": self.description,
        }