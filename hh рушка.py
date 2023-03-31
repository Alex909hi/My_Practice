import requests
import json
import re
import pandas as pd
from datetime import datetime
# Задача: найти работодателей по критериям в hh.ru и занести эту информацию в блокнот

per_page = 60 # Число работодателей
page = 5 #Число страниц
df = pd.DataFrame({'Название': [], 'Регион': [], 'Адрес сайта': []}) # База данных, которую впоследствии заполним и перебросим на блокнот


with pd.option_context("display.max_rows", None):
    print("Одну минуту и ...") 
    for y in range(0, page): 
        response = requests.get(f'https://api.hh.ru/employers/?only_with_vacancies=True&per_page={per_page}&page={y}') # делаем запрос на работодателей
        data = json.loads(response.text) # Преобразуем данные в структуру JSON, но для восприятия пока непонятны
        # Чтоб данные были читаемы, нужно выполнить эту команду(в данной задаче она не нужна) -->  print(json.dumps(data,indent=1,ensure_ascii=False) ) # Для восприятия глаз

        if response.status_code == requests.codes.ok:   # Проверяем всё ли окей
            print(f" в {y} странице всё ок!")
            for i in range(0, per_page):
                id = json.dumps(data["items"][i]["id"],indent=1,ensure_ascii=False) # Получаем id работодателя
                id = int(re.sub('[^\w, ]', '', id))  # Очищаем id от лишних символов

                response_url = requests.get(f'https://api.hh.ru/employers/{id}')  # Находим инфу о работодателе по id
                data_url = json.loads(response_url.text) # Компу понятно стало, что это JSON  - а мне нет

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
                #    ДОПОЛНЕНИЕ   
                #    описание работ в Нижнекамске
                #
                #    response_Nizhnekamsk = requests.get(f'https://api.hh.ru/employers/?only_with_vacancies=True&per_page=30&area=1642')
                #    data_Nizhnekamsk = json.loads(response_Nizhnekamsk.text)
                #    id_Nizhnekamsk = json.dumps(data_Nizhnekamsk["items"][i]["id"],indent=1,ensure_ascii=False)
                #    id_Nizhnekamsk = int(re.sub('[^\w, ]', '', id_Nizhnekamsk)) 
                #    print() 
                #    response_url_Nizhnekamsk = requests.get(f'https://api.hh.ru/employers/{id_Nizhnekamsk}?only_with_vacancies=True&per_page=30&area=1642') 
                #    data_url_Nizhnekamsk = json.loads(response_url_Nizhnekamsk.text)
                #    print(json.dumps(data_url_Nizhnekamsk["description"],indent=1,ensure_ascii=False) )
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

                added_in_site = json.dumps(data_url["trusted"],indent=1,ensure_ascii=False) # Прошел ли работодатель проверку на сайте?
                black_list = json.dumps(data_url["relations"],indent=1,ensure_ascii=False) #  Добавлен ли работодатель в черный список?

                if( added_in_site and black_list != ['blacklisted']):
                # Добавляем название работодателя
                    name = json.dumps(data_url["name"],indent=1,ensure_ascii=False)
                    print(f" <{y} | {i} --> {name}")
                # Добавляем регион работодателя
                    area = json.dumps(data_url["area"]["name"],indent=1,ensure_ascii=False)
                # и сайт
                    site_url = json.dumps(data_url["site_url"]  )                                                            
                    df.loc[ len(df.index )] = [name, area,site_url] # Заносим в БД DataFrame   
        else:
            print(f"На {y} что-то не так")
        # Показать DataFrame
        print(df)
    # Создаем счётчик времени, чтоб сохранять данные только в новый файл   
    current_datetime = datetime.now()
    # Новый файл
    time_now = current_datetime.strftime(" %d.%m.%Y %H.%M.%S")
    file = open(f"C:/Users/kochkin.ao/Desktop/python/otus{time_now}.txt", "w") 
    file.write(str(df))
    file.close()       
    
print("\nВуаля!!! Всё готово!") 