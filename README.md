# Магазин товаров


## Описание проекта

Этот проект представляет собой простую систему управления товарами для магазина. Он включает в себя классы Category и Product, а также реализованы две категории товаров: **Смартфоны** и **Трава газонная**, которые позволяют создавать и хранить информацию о различных категориях и связанных с ними продуктах. Также предусмотрена возможность загрузки данных из JSON-файла.

## Структура классов

### Class: BaseProduct

- Абстрактный класс, который определяет общие свойства и методы для всех сущностей.

### Class: PrintMixin

- Класс-миксин, который при создании объекта, то есть при работе метода __init__, печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.

#### Атрибуты


### Class: Category

#### Атрибуты

  • name (str): Название категории.

  • description (str): Описание категории.

  • products (list): Список продуктов, относящихся к категории.

  • category_count (int): Общее количество созданных категорий (статический атрибут).

  • product_count (int): Общее количество продуктов во всех категориях (статический атрибут).

#### Методы

  • __init__(self, name, description, products=None): Конструктор класса, который инициализирует категорию, увеличивает счетчик категорий и добавляет количество продуктов.

### Class: Product

#### Атрибуты

  • name (str): Название продукта.

  • description (str): Описание продукта.

  • price (float): Цена продукта.

  • quantity (int): Количество продукта на складе.

#### Методы

  • __init__(self, name, description, price, quantity): Конструктор класса, который инициализирует продукт.

### Class Smartphone - класс для товаров категории "Смартфоны".
   - Наследует от класса Product.
   - Дополнительные свойства:
     - efficiency (производительность)
     - model (модель)
     - memory (объем встроенной памяти)
     - color (цвет)

### Class LawnGrass - класс для товаров категории "Трава газонная".
   - Наследует от класса Product.
   - Дополнительные свойства:
     - country (страна-производитель)
     - germination_period (срок прорастания)
     - color (цвет)

### Функции

#### Функция: read_json(path: str) -> dict

Читает данные из указанного JSON-файла.

#### Параметры

  • path (str): Путь к JSON-файлу.

#### Возвращает

  • dict: Словарь с данными из файла.

### Функция: create_category_from_json(data)

Создает список категорий из данных, загруженных из JSON.

#### Параметры

  • data (list): Список категорий в формате JSON.

#### Возвращает

  • list: Список объектов категорий.
  
## Установка

1. Скопируйте код в свой проект.

2. Убедитесь, что у вас установлен Python.

3. Убедитесь, что у вас есть файл JSON с данными о категориях и продуктах.


## Тесты

В проекте предусмотрены тесты для проверки функциональности классов Category и Product, и наследуемых классов Smartphone и LawnGrass. Тесты написаны с использованием библиотеки pytest.

### Установка

poetry add --group dev pytest