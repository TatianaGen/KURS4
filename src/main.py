from hh_api import HHApi
from job import Job
from data_manager import DataManager
from filters import filter_jobs, filter_jobs_by_salary, get_top_jobs
from colorama import *


def user_interaction():
    print(Fore.RED + Style.BRIGHT + 'Привет! Помогу найти работу на сайте hh.ru. '
                                       + Fore.RESET)

    search_query = input('Введите вакансию для поиска: ').lower()
    top_n = input('Введите количество вакансий, которые будут отображаться в верхней N: ')
    filter_words = input('Введите ключевые слова для фильтрации вакансий: ').capitalize().split()
    salary_range = input('Введите диапазон зарплат и валюту, разделенные запятыми. '
                         'Пример: 10000,200000,RUR (USD,EUR,KZT) \n').upper()


    hh_api = HHApi()

    hh_jobs = hh_api.get_jobs(search_query)

    data_manager = DataManager(salary_range)
    data_manager.add_job(hh_jobs)

    data = data_manager.open_file()

    jobs_list = Job.from_dict(data)

    filtered_jobs = filter_jobs(jobs_list, filter_words)
    ranged_jobs = filter_jobs_by_salary(filtered_jobs, salary_range)
    top_jobs = get_top_jobs(ranged_jobs, top_n)

    for job in top_jobs:
        print(f'{job}\n')

    data_manager.delete_job()


if __name__ == '__main__':
    user_interaction()