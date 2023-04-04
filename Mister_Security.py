import getpass
import pandas as pd
from datetime import datetime
import io
import pandas as pd
import msoffcrypto
# Задача: к столбцу 'Столица' применить шифр Цезаря

try:
    alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    my_password = getpass.getpass() # Вводим пароль
    decrypted_workbook = io.BytesIO()
    with open('C:/Users/kochkin.ao/Desktop/Weather/Новая_ПогодКА_03.09 01.32.48.xlsx', 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key(password=my_password) #проверка пароля
        office_file.decrypt(decrypted_workbook)
    excel = pd.read_excel(decrypted_workbook)
    print("Вход выполнен!")

    # Создаем счётчик времени, чтоб сохранять данные только в новый файл
    current_datetime = datetime.now()
    time_now = current_datetime.strftime(" %d.%m.%Y %H.%M.%S")
    
    step = int(input('Шаг шифровки: ')) 
    for i, row in zip(range(0, len(excel['Погода'])) , excel['Столица'] ):
        y = excel['Столица'][i][0] # Берём первую букву столицы
        
        mesto = alfavit.find(y)   # Алгоритм для шифрования сообщения на русском 
        new_mesto = mesto + step
        if y in alfavit:
            excel.loc[i, ['Столица']] = f'{alfavit[new_mesto]}{row[1:]}' # Склеиваем "зашифрованное" слово
    print(excel)
    excel.to_excel(f'C:/Users/kochkin.ao/Desktop/python/Шифр_Цезаря{time_now}.xlsx')
except: 
    print("Ну, вот, опять ошибка")