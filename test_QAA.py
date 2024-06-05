import requests

# URL для тестирования
REGION_LIST = "https://regions-test.2gis.com/1.0/regions"

# Функция для получения данных через API
def get_items(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка запроса API с кодом {response.status_code}")

def get_q(q):
    return requests.get(REGION_LIST, params={'q':q})

# Тест-1, Проверка соответствия количества элементов = 15 и количества элементов в списке items
def test_total_matches_items_count_15():
    data = get_items(REGION_LIST+"?page=1&page_size=15")
    max_total_in_page = 15
    items_count = len(data['items'])
    assert max_total_in_page == items_count, f"Максимальное кол-во в виде: {max_total_in_page} не соответствует количеству элементов {items_count}"

# Тест-2, Проверка соответствия количества элементов = 10 и количества элементов в списке items
def test_total_matches_items_count_10():
    data = get_items(REGION_LIST+"?page=1&page_size=10")
    max_total_in_page = 10
    items_count = len(data['items'])
    assert max_total_in_page == items_count, f"Максимальное кол-во в виде: {max_total_in_page} не соответствует количеству элементов {items_count}"

# Тест-3, Проверка соответствия количества элементов = 5 и количества элементов в списке items
def test_total_matches_items_count_5():
    data = get_items(REGION_LIST+"?page=1&page_size=5")
    max_total_in_page = 5
    items_count = len(data['items'])
    assert max_total_in_page == items_count, f"Максимальное кол-во в виде: {max_total_in_page} не соответствует количеству элементов {items_count}"

# Тест-4, Проверка соответствия количества элементов по умолчанию и количества элементов в списке items
def test_total_matches_items_count():
    data = get_items(REGION_LIST)
    max_total_in_page = 15
    items_count = len(data['items'])
    assert max_total_in_page == items_count, f"Максимальное кол-во в виде: {max_total_in_page} не соответствует количеству элементов {items_count}"

# Тест-5 Проверка на передачу пустого параметра q
def test_q_empty():
    q_empty_response = get_q("")
    assert q_empty_response.status_code == 404, f"Ожидаемый код ошибки 404 not found для путого параметра 'q', пришел код {q_empty_response.status_code}"

# Тест-6 Проверка на минимальное кол-во символов в параметре q
def test_q_params_3_symbols():
    q = "a" * 3
    response = get_q(q)
    assert response.status_code == 200

# Тест-7 Проверка на передачу меньше минимального кол-ва символов в параметре q
def test_q_params_2_symbols():
    low_q = "a" * 2
    response = get_q(low_q)
    assert response.status_code == 200
    error_message = response.json()['error']['message']
    message = "Параметр 'q' должен быть не менее 3 символов"
    assert error_message == message

# Тест-8 Проверка на передачу больше максимального кол-ва символов в параметре q
def test_q_params_31_symbols():
    long_q = "a" * 31
    response = get_q(long_q)
    assert response.status_code == 200
    error_message = response.json()['error']['message']
    message = "Параметр 'q' должен быть не более 30 символов"
    assert error_message == message

# Тест-9 Проверка корректность кода страны 'ru' при фильтрации
def test_country_code_correct_ru():
    data = get_items(REGION_LIST+"?country_code=ru")
    ru_code = "ru"
    mismatches = []  # Список для сохранения несоответствующих элементов
    for item in data['items']:
        item_code = item['country']['code']
        if ru_code != item_code:
            mismatches.append(f"В регионе '{item['name']}' не соответсвует код страны {ru_code}, с '{item_code}")
    assert not mismatches, "Найденны несоответствия для следующих регионов: " + ";".join(mismatches)

# Тест-10 Проверка корректность кода страны 'kg' при фильтрации
def test_country_code_correct_kg():
    data = get_items(REGION_LIST+"?country_code=kg")
    kg_code = "kg"
    mismatches = []  # Список для сохранения несоответствующих элементов
    for item in data['items']:
        item_code = item['country']['code']
        if kg_code != item_code:
            mismatches.append(f"В регионе '{item['name']}' не соответсвует код страны {kg_code}, с '{item_code}")
    assert not mismatches, "Найденны несоответствия для следующих регионов: " + ";".join(mismatches)

# Тест-11 Проверка корректность кода страны 'kz' при фильтрации
def test_country_code_correct_kz():
    data = get_items(REGION_LIST+"?country_code=kz")
    kz_code = "kz"
    mismatches = []  # Список для сохранения несоответствующих элементов
    for item in data['items']:
        item_code = item['country']['code']
        if kz_code != item_code:
            mismatches.append(f"В регионе '{item['name']}' не соответсвует код страны {kz_code}, с '{item_code}")
    assert not mismatches, "Найденны несоответствия для следующих регионов: " + ";".join(mismatches)

# Тест-12 Проверка корректность кода страны 'cz' при фильтрации
def test_country_code_correct_cz():
    data = get_items(REGION_LIST+"?country_code=cz")
    cz_code = "cz"
    mismatches = []  # Список для сохранения несоответствующих элементов
    for item in data['items']:
        item_code = item['country']['code']
        if cz_code != item_code:
            mismatches.append(f"В регионе '{item['name']}' не соответсвует код страны {cz_code}, с '{item_code}")
    assert not mismatches, "Найденны несоответствия для следующих регионов: " + ";".join(mismatches)

# Тест-13 Проверка корректность кода страны 'ua' при фильтрации
def test_country_code_negativ_ua():
    response = get_items(REGION_LIST+"?country_code=ua")
    error_message = response['error']['message']
    message = "Параметр 'country_code' может быть одним из следующих значений: ru, kg, kz, cz"
    assert error_message == message

# Тест-14 Проверка на передачу некорректного значения page_size
def test_page_size_negativ_22():
    response = get_items(REGION_LIST+"?page=1&page_size=22")
    error_message = response['error']['message']
    message = "Параметр 'page_size' может быть одним из следующих значений: 5, 10, 15"
    assert error_message == message

# Тест-15 Проверка на передачу дробного числа в значения page_size
def test_page_size_negativ():
    response = get_items(REGION_LIST+"?page=1&page_size=1.5")
    error_message = response['error']['message']
    message = "Параметр 'page_size' длжен быть целым числом"
    assert error_message == message

# Тест-16 Проверка на передачу дробного числа в значения page
def test_page_negativ():
    response = get_items(REGION_LIST+"?page=1.5")
    error_message = response['error']['message']
    message = "Параметр 'page' длжен быть целым числом"
    assert error_message == message

# Тест-17 Проверка на передачу некорректного значения country_code
def test_country_code_negativ_ru1():
    response = get_items(REGION_LIST+"?country_code=ru1")
    error_message = response['error']['message']
    message = "Параметр 'country_code' может быть одним из следующих значений: ru, kg, kz, cz"
    assert error_message == message
