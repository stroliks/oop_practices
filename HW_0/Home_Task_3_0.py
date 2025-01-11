# #**Описание**
# В этой задаче предстоит создать структуру для хранения информации о домашних животных.
# Каждое животное имеет свой набор характеристик, который необходимо учитывать при создании структуры.
# **Характеристики животных**
#
# - Имя: строка
# - Вид: строка (например, собака, кошка, попугай)
# - Возраст: целое число (в годах)
# - Вес: вещественное число (в килограммах)
# - Вакцинирован: булево значение (да/нет)

Struct Pet:
    name:str
    type:str
    age: int
    weight: float
    is_vakcine: bool


# Задача №2. "Ритуалы и традиции в волшебном обществе"
# Описание
# В мире, где магия является частью повседневной жизни, существует общество, которое следует определенным ритуалам
# и традициям. Эти ритуалы и традиции включают в себя использование специальных артефактов
# и проведение церемоний в определенные дни. Артефакты могут быть изготовлены из разных материалов (строка),
# иметь историческое значение(строка) и обладать определенной силой(число).
# Даты в которые проходят ритуалы характеризуются днем(число), месяцем(число) и годом(число).
# Члены общества обладают уникальными ролями(строка), одеждой(строка), стажам в обществе(число)
# и наличием одного артефакта, и каждый из них вносит свой вклад в поддержание и передачу традиций поколениями.

# Задание
# Определите ключевые сущности в ритуалах и традициях этого волшебного общества.
# Опишите детально каждую сущность в виде структуры, учитывая предоставленные характеристики.
# Анализируйте, как сущности взаимодействуют друг с другом во время ритуалов (письменный ответ).

1. Ключевые сущности:
- Артефакты
- Члены общества
- Дата
- Ритуалы

2.

Struct Artefact:
    material: str
    hystorical_value: str
    magic_power: int


Struct Wizard:
    role: str
    clothes:
    experience: int
    artefact: Artefact()
    contribution: float  # доля вклада в ритуал

Struct Date:
    day: int
    month: int
    year: int

Struct Ritual:
    content: float
    date: Date()

Struct Recipient:
    count_of_tradition: int


3. Члены общества (Wizard) взаимодействуют с Датой (реагируют на сообщения от объекта Date),
что позволят им собраться в одно время (в допущении о том, что они всегда проводят ритуал в одном месте).
Сущность Артефакт передает члену общества (Wizard) совокупность своих характеристик и в совокупности
с остальными индивидуальными харатеристиками владельца (Wizard)  образует долю вклада,
которую может внести член общества в поддержание и передачу традиций.
Сущность член общества (Wizard) взаимодействует с сущностью Ритуал,
передавая ей свое индивидуальное значение contribution, тем самым Ритуал, получая от каждого из всех членов долю вклада,
при достижении размера вклада content до 100%, считается завершенным и передает собщение членам общества, что они
передача традиций в рамках данного мероприятия (сущности Ritual) прошла успешно.
По хорошему еще нужна структура получателей традиций (ради кого все это каждый раз затевается и кому передаются все
традиции), Преемники, которые также взаимодействуют с сущностью Ритуала, получая от него (традицию (ритуал, опыт),
образованный путем формирования вклада каждого из членов общества.





# ## **Задача №3. "Городской фермерский рынок"**
#
# **Описание**
# Городской фермерский рынок — это место, где местные фермеры продают свою продукцию жителям города.
# Рынок представляет собой разнообразие стендов, каждый из которых специализируется на определённых товарах,
# таких как свежие овощи, фрукты, мясные и молочные продукты. Каждый стенд закреплен за определенным фермером,
# характеризуется именем, возрастом и имеет ассортимент продуктов (массив продуктов).
# Продукт в свою очередь описывается наименованием (строка), количеством штук в наличии (число),
# и датой изготовления (сущность из задачи №2).
# Покупатели которые приходят рано утром, идут к уже проверенным фермерам, поэтому для фермеров важно знать
# их имя (строка), возраст (число), демографические характеристики (строка), предпочтения в товарах (список имен товаров)
# , количество денег (число).
#
# **Задание**
#
# 1. Определите ключевые сущности, участвующие в деятельности городского фермерского рынка.
# 2. Для каждой сущности опишите детально её структуру.
# 3. Проанализируйте, как характеристики сущностей могут влиять на их взаимодействие и на общую атмосферу рынка.

1. Ключевые сущности:
- Фермер
- Продукт
- Покупатель
- Дата (изготовления))

2.
Struct Fermer:
    name: str
    age: int
    products: list[Product()]

Struct Product:
    name: str
    count: int
    date_of_create: Date()

Struct Date:
    day: int
    month: int
    year: int

Struct Shopper:
    name: str
    age: int
    demograf: str
    like_products: list[Product()]
    money: float

3. Наиболее значимые влияния характеристик сущностей:
- Давняя дата изготовления определенного продукта снижает уровень покупателей у фермера, торгующего этим продуктом (а мжет
и остальными (вследствие подрыва доверия (которое тоже может являться сущностью))), до нуля, тем самым создавая дефицит
определенных продуктов на рынке, недовольство покупателей и ухудшение общей атмосферы рынка
- количество денег у покупателя, бизкое к нулю, приводит к невозможности купить товар у фермера, что приводит к избытку
определенного товара на рынке, его залеживанию и удалению даты изготовления от текущей даты (что, в свою очередь приводит
к порче этого товара и плавно перетекает в п. 1)
