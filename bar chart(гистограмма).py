import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import (AutoMinorLocator)
# Задача: отобразить погоду столиц мира на гистограмме

# Берём файл с данными
excel =pd.read_excel('C:/Users/kochkin.ao/Desktop/python/RESULT 29.03.2023 08.52.32.xlsx')
# Создаем массив World_Weather - для температуры,
World_Weather = []
# а Capitals - для столиц
Capitals = []

# Создаём сетку для нашей гистограммы
fig, ax = plt.subplots(figsize=(8, 6))
ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

# Счётчик нужен, чтобы распределять значения температуры внутри графика по оси x
i = 0
for  row,capital in zip(excel['Погода'],excel['Страна'] ):
    World_Weather.append(row) # добавляем значения температуры
    Capitals.append(capital) # добавляем столицы
    plt.text(-0.5 + i,row,row) # добавляем знач-я температуры в график
    i = i + 1
print('Секунду...')

# Делаем цену деления для осей x и y
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
# Параметры длины и ширины цены деления(снаружи графика)
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)

# Отображаем гистограмму
x =Capitals
y = World_Weather
sns.barplot(x=x, y=y )

plt.xticks(rotation=80) # Поворачиваем названия столиц на 80° (за графиком)
plt.title('Погода столиц мира', fontsize=20, fontname='Times New Roman' ) # настройка заглавия
plt.ylabel('Температура, °C', color='gray') # озаглавие оси y

# Конец фильма
print('Смотри')
plt.show()