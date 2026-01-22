from src.parser import HeadHunterAPI
from src.save_file import SaveFile
from src.vacancy import Vacancy


def user_interaction() -> None:
    keyword = input("Введите поисковый запрос: ")
    hh_api = HeadHunterAPI()
    hh_api._load_vacancies(keyword=keyword)
    raw_vacancies = hh_api._vacancies
    vacancy_objects = []
    for vac in raw_vacancies:
        v = Vacancy(
            name=vac["name"],
            salary=vac["salary"],
            alternate_url=vac["alternate_url"],
            responsibility=vac["snippet"]["responsibility"],
        )
        vacancy_objects.append(v)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = []
    if filter_words:
        for vacancy in vacancy_objects:
            vacancy_text = f"{vacancy.responsibility}".lower()
            if any(word.lower() in vacancy_text for word in filter_words):
                filtered_vacancies.append(vacancy)
    else:
        filtered_vacancies = vacancy_objects

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    top_vacancies = sorted(filtered_vacancies[:top_n], reverse=True)
    dict_vacations = []
    for v in top_vacancies:
        dict_vacations.append(v.cast_to_dict())

    save_yes_no = input("Сохранить данные в файл? Да/Нет? ").lower()
    if save_yes_no == "да":
        name_file = input("Введите название файла")
        if name_file == "":
            save = SaveFile()
        else:
            save = SaveFile(name_file)
        save.save_data(dict_vacations)
    else:
        None
    del_yes_no = input("Удалить данные из файла? ").lower()
    if del_yes_no == "да":
        name_file = input("Введите название файла")
        if name_file == "":
            save = SaveFile()
        else:
            save = SaveFile(name_file)
        del_word = "Введите ключевое слово"
        save.del_data(del_word)
    else:
        None
