
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
}
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


def geo_ru(geo_logs):
    counter = len(geo_logs)
    while counter > 0:
        for id, geo_log in enumerate(geo_logs):
            if 'Россия' not in list(geo_log.values())[0]:
                del geo_logs[id]
            counter -= 1
    return geo_logs

def ids_un(ids):
    list_ = []
    for data in ids.values():
        list_ += data
    return list(set(list_))


def queries_says(queries):
    says = {}
    result = ''
    for request in queries:
        words = request.split()
        if len(words) in says.keys():
            says[len(words)] += 1
        else:
            says[len(words)] = 1

    for key_, value_ in says.items():
        percentage = round((value_ / len(queries)) * 100)
        result += f'Поисковых запросов из {key_} слов: {percentage}%\n'
    return result


if __name__ == "__main__":
    pass
