from abstractvacancyprovclass import AbstractVacancyProvClass
import requests

from vacancy import Vacancy


class VacancyProvHh(AbstractVacancyProvClass):

    def get_vacancy(self, vacancy_name):
        res = requests.get("https://api.hh.ru/vacancies", params={"text": vacancy_name},
                           headers={"User-Agent": "SkyPro/1.0(https://github.com/hunkerbek"})
        if res.status_code == 200:
            data = res.json()
            result = []
            # pprint(data)
            for a in data["items"]:
                salary = a["salary"]
                if salary:
                    salary_from = salary.get("from", None)
                    salary_to = salary.get("to", None)
                else:
                    salary_from = None
                    salary_to = None

                new_vacancy = Vacancy(a["name"], salary_from, salary_to, a["alternate_url"])
                result.append(new_vacancy)
            return result

        else:
            return []
