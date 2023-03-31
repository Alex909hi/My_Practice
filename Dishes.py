# Задание: вывести продукты и их кол-во в зависимости от кол-ва гостей на празднике
cook_book = [
['салат',
[ ['картофель', 100, 'гр.'],
['морковь', 50, 'гр.'],
['огурцы', 50, 'гр.'],
['горошек', 30, 'гр.'],
['майонез', 70, 'мл.'], ] ],
['пицца',
[ ['сыр', 50, 'гр.'],
['томаты', 50, 'гр.'],
['тесто', 100, 'гр.'],
['бекон', 30, 'гр.'],
['колбаса', 30, 'гр.'],
['грибы', 20, 'гр.'], ] ],
['фруктовый десерт',
[ ['хурма', 60, 'гр.'],
['киви', 60, 'гр.'],
['творог', 60, 'гр.'],
['сахар', 10, 'гр.'],
['мед', 50, 'мл.'], ] ] ]
#🥗🥗🥗🥗🥗
def salad():
    return str(cook_book[0][0]).capitalize()
#🥔🥔🥔
def potatoes():
    return cook_book[0][1][0][0]
def potatoes_weight():
    return int(cook_book[0][1][0][1])
#🥕🥕🥕
def carrot():
    return cook_book[0][1][1][0]
def carrot_weight():
    return int(cook_book[0][1][1][1])
#🥒🥒🥒
def cucumber():
        return cook_book[0][1][2][0]
def cucumber_weight():
    return int(cook_book[0][1][2][1])
# Горошек
def pea():
    return cook_book[0][1][3][0]
def pea_weight():
    return int(cook_book[0][1][3][1])
# Майонез
def mayonnaise():
    return cook_book[0][1][4][0]
def mayonnaise_weight():
    return int(cook_book[0][1][4][1])
#🍕🍕🍕🍕🍕
def pizza():
    return str(cook_book[1][0]).capitalize()
#🧀🧀🧀
def cheese():
    return cook_book[1][1][0][0]
def cheese_weight():
    return int(cook_book[1][1][0][1])
#🍅🍅🍅
def tomato():
    return cook_book[1][1][1][0]
def tomato_weight():
    return int(cook_book[1][1][1][1])
#🍞🍞🍞
def dough():
    return cook_book[1][1][2][0]
def dough_weight():
    return int(cook_book[1][1][2][1])
#🥓🥓🥓
def bacon():
    return cook_book[1][1][3][0]
def bacon_weight():
    return int(cook_book[1][1][3][1])
#🌭🌭🌭
def sausage():
    return cook_book[1][1][4][0]
def sausage_weight():
    return int(cook_book[1][1][4][1])
#🍄🍄🍄
def mushroom():
    return cook_book[1][1][5][0]
def mushroom_weight():
    return int(cook_book[1][1][5][1])
#🍉🍋🍇🍊🍐
def fruit_dessert():
    return str(cook_book[2][0]).capitalize()
# Хурма
def persimmon():
    return cook_book[2][1][0][0]
def persimmon_weight():
    return int(cook_book[2][1][0][1])
#🥝🥝🥝
def kiwi():
    return cook_book[2][1][1][0]
def kiwi_weight():
    return int(cook_book[2][1][1][1])
# Творог
def curd():
    return cook_book[2][1][2][0]
def curd_weight():
    return int(cook_book[2][1][2][1])
# Сахар
def sugar():
    return cook_book[2][1][3][0]
def sugar_weight():
    return int(cook_book[2][1][3][1])
#🍯🍯🍯
def honey():
    return cook_book[2][1][4][0]
def honey_weight():
    return int(cook_book[2][1][4][1])
sum_people = int(input("Введите кол-во гостей: "))
print(
f"{salad()}🥗🥗🥗:\n"
f"{potatoes()}🥔, {potatoes_weight() * sum_people}гр.\n"
f"{carrot()}🥕, {carrot_weight()* sum_people}гр.\n"
f"{cucumber()}🥒, {cucumber_weight()* sum_people}гр.\n"
f"{pea()}, {pea_weight()* sum_people}гр.\n"
f"{mayonnaise()}, {mayonnaise_weight()* sum_people}мл.\n"
f"{pizza()}🍕🍕🍕:\n"
f"{cheese()}🧀, {cheese_weight()* sum_people}гр.\n"
f"{tomato()}🍅, {tomato_weight()* sum_people}гр.\n"
f"{dough()}🍞, {dough_weight()* sum_people}гр.\n"
f"{bacon()}🥓, {bacon_weight()* sum_people}гр.\n"
f"{sausage()}🌭, {sausage_weight()* sum_people}гр.\n"
f"{mushroom()}🍄, {mushroom_weight()* sum_people}гр.\n"
f"{fruit_dessert()}🍉🍋🍇🍌🍊:\n"
f"{persimmon()}, {persimmon_weight()* sum_people}гр.\n"
f"{kiwi()}🥝, {kiwi_weight()* sum_people}гр.\n"
f"{curd()}, {curd_weight()* sum_people}гр.\n"
f"{sugar()}, {sugar_weight()* sum_people}гр.\n"
f"{honey()}🍯, {honey_weight()* sum_people}мл.\n"
)