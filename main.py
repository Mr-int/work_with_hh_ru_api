from src.hh import HeadHunterApi
from src.file_manager import FileManager

def decor():
    print("----" * 40)

def select_settings():
    print("Вас приветствует программа вывода вакансий hh.ru 🫶")
    vacancy_name = input("Введите поисковый запрос для запроса вакансий из hh.ru: ")
    while True:
        try:
            vacancy_quantity = int(
                input("Введите количество вакансий, которые вы хотите видеть: ")
            )
            if vacancy_quantity <= 0:
                print("\033[31mЧисло должно быть больше нуля\033[0m\n")
            else:
                break
        except ValueError:
            print("\033[31mВведите число, большее нуля\033[0m\n")

    keyword = input(
        "Введите ключевое слово в описании вакансии (или 'N' для пропуска): "
    )
    print_vacancy(vacancy_name, vacancy_quantity, keyword if keyword.lower() != "n" else None)

def print_vacancy(name, quantity, keyword=None, file_path="data/vacancies.json"):
    hh = HeadHunterApi()
    params = {"text": name, "per_page": quantity}
    vacancies = hh.get_vacancies(params)
    if not vacancies:
        print("Вакансии не найдены")
        return

    file_manager = FileManager()
    for vacancy in vacancies:
        file_manager.add_vacancy(vacancy, file_path)

    sorted_vacancies = sorted(vacancies, key=lambda x: x.salary or 0, reverse=True)
    if keyword:
        sorted_vacancies = [
            v for v in sorted_vacancies
            if keyword.lower() in v.description.lower()
        ]

    for i, vacancy in enumerate(sorted_vacancies[:quantity], 1):
        decor()
        print(f"Вакансия {i}:")
        print(vacancy)

if __name__ == "__main__":
    select_settings()