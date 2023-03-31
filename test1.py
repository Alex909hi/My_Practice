#решить ряд задач со строкой: 
# "Январь, феВраль, МАРТ, «ВысотныЙ дом», ВАР, раЛ??"
import re
# находим поряд. номер месяца
month = {
    "Январь"  : 1,
    "Февраль" : 2,
    "Март"    : 3,
    "Апрель"  : 4,
    "Май"     : 5,
    "Июнь"    : 6,
    "Июль"    : 7,
    "Август"  : 8,
    "Сентябрь": 9,
    "Октябрь" : 10,
    "Ноябрь"  : 11,
    "Декабрь" : 12
}
my_string = input("Введите строку: ")
my_number = int(input("Введите число strLen: "))

def query_strLen(string, num):
    string = re.sub('[^\w, ]', '', string) # преобразовали строку:
    string = string.split(', ')      # очистили, сделали заглав. буквы, поделили по частям 
    string.sort()
    print()
   
    new_string = "" # строка, на которую будем наматывать результат 

    for i in range(len(string)):
        
        if(len(string[i]) >= num):
            string[i] = string[i].capitalize()
            if(string[i] in month.keys()): # ловит месяцы
                new_string += f"{string[i]}({month[string[i]]}), "
            else:
                new_string += f"{string[i]}, "
        
    new_string = str(new_string)
    new_string = new_string.split(', ') 
    new_string.sort()
    result = ""
    for i in range(len(new_string) ):
        result += f"{new_string[i]}, "
    print(f"Результат таков: {result}")

query_strLen(my_string, my_number)

# список правильных результатов:
# 0 = Вар, Высотный дом, Март(3), Рал, Февраль(2), Январь(1), 
# 1 = Вар, Высотный дом, Март(3), Рал, Февраль(2), Январь(1), 
# 2 = Вар, Высотный Дом, Март(3), Рал, Февраль(2), Январь(1), 
# 3 = Вар, Высотный Дом, Март(3), Рал, Февраль(2), Январь(1), 
# 4 = Высотный Дом, Март(3), Февраль(2), Январь(1), 
# 5 = Высотный Дом, Февраль(2), Январь(1), 