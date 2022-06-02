from abc import abstractmethod

class Storage:
    """ Абстрактный класс """
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        """ Увеличивает запас items с учетом лимита capacity."""

        # Проверяем есть ли свободное место.
        if self.get_free_space() > 0:
            # Проверяем не превысит ли место лимит capacity, если добавим запасы.
            if self.get_free_space() >= count:
                # Проверяем есть ли такой запас в ключах словаря.
                if name in self.items.keys():
                    # Если есть, то добавляем количество запаса.
                    self.items[name] += count
                    return True
                else:
                    # А если нет такого запаса в ключах словаря, то добавляем новый запас с количеством.
                    self.items[name] = count
                    print(f"Товар {name} добавлен")
                    return True
            else:
                print(f"Не хватает места для хранения. Кол-во свободного места: {self.get_free_space()}")
                return False
        else:
            print(f"Нет свободного места для хранения")
            return False

    def remove(self, name:str, count:int):
        """ Уменьшает запас items, но не ниже 0."""

        # Проверяем есть ли такой запас в ключах словаря.
        if name in self.items.keys():
            # Проверяем не будет ли ниже 0 кол-во товара, если уменьшим.
            if self.items[name] - count < 0:
                print(f"Уменьшите кол-во товара, должно быть не больше {self.items[name]}")
                return False
            else:
                # Если есть такой запас в ключах словаря и кол-во не станет ниже 0, то уменьшаем кол-во запаса.
                self.items[name] -= count
                print("Есть необходимое количество товара")
                return True
        else:
            # А если нет такого запаса в ключах словаря, то выдаем ошибку.
            print(f"Такого товара '{name}' нет в запасах")
            return False


    def get_free_space(self):
        """ Возвращает количество свободных мест."""

        # Считаем количество занятых мест в словаре.
        count_in_items = sum(self.items.values())

        return self.capacity - count_in_items

    def get_items(self):
        """ Возвращает содержание склада в словаре {товар: количество}."""

        return self.items

    def get_unique_items_count(self):
        """ Возвращает количество уникальных товаров."""

        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        self.items = {}
        self.capacity = 20

    def add(self, name, count):
        """ Увеличивает запас items с учетом лимита capacity."""

        # Проверяем есть ли в нем меньше 5 разных товаров.
        if self.get_unique_items_count() < 5:
            # Если уникальных товаров меньше 5, то добавляем товары, используя метод класса, у которого наследовались.
            add_items_in_shop = super().add(name, count)
            # Проверяем удалось ли доставить в магазин товар.
            if add_items_in_shop:
                return True
            else:
                return False
        else:
            print("Не хватает мета для хранения, число уникальных товаров должно быть не больше 5.")
            return False


class Request:
    """ Здесь храниться запрос."""

    def __init__(self, input_str:str):
        data = input_str.split(" ")
        self.from_ = data[4]        # переменная - откуда везем
        self.to = data[6]           # переменная - куда везем
        self.amount = int(data[1])  # переменная - кол-во товара
        self.product = data[2]      # переменная - какой товар берём

    def __repr__(self):
        """ Возвращает объект класса Request."""

        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"
