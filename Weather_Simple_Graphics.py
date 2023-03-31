import matplotlib.pyplot as plt
import pandas as pd

# Задача: построить простой график по погоде разных столиц мира
# Замечание к автору --> названия столбцов со странами и со столицами ПЕРЕПУТАНЫ, т.е. у столбца со странами заглавие "Столицы"

# Берём файл excel 
excel =pd.read_excel('C:/Users/kochkin.ao/Desktop/python/RESULT 29.03.2023 08.52.32.xlsx')
# Создаем массив, который будет иметь данные для диаграммы
World_Weather = []
# Это счётчик для озаглавия столиц на графике
i = 0
for row, capital in zip(excel['Погода'], excel['Страна']):

    World_Weather.append(row) # добавляем значения
    plt.text(i,row, capital, fontsize=8 ) # добавляем текст на диаграмме
    i = i + 1
plt.grid(True)
plt.xlabel('Capitals', color='gray')
plt.ylabel('Temperature, °C',color='gray')
plt.axis([0,30,0,40]) # делаем максимальное расширение всей диаграммы
plt.title('World Weather', fontsize=20, fontname='Times New Roman')
plt.plot(World_Weather, 'r')
plt.plot(World_Weather, 'bo')
print('вот  результат!')
plt.show()