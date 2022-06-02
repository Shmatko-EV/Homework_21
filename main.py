from classes import Request, Store, Shop

if __name__ == '__main__':
    # Инициализируем классы.
    store = Store()
    shop = Shop()

    # Добавим товары в склад.
    store.add("печеньки", 3)
    store.add("собачки", 4)
    store.add("коробки", 5)
    # Добавим товары в магазин.
    shop.add("собачки", 5)
    shop.add("печеньки", 3)
    shop.add("рыбки", 2)
    shop.add("елки", 3)
    #shop.add("конфеты", 3)

    print("На складе есть: ")
    for k_item, v_item in store.get_items().items():
        print(f"{v_item} {k_item}")

    # Получаем запрос пользователя.
    user_request = input("Введите запрос такого вида: 'Доставить 2 печеньки из склад в магазин': \n")
    data_request = Request(user_request)

    # Если на складе есть нужное кол-во товара, то забираем от туда.
    result_remove_store = store.remove(data_request.product, data_request.amount)
    if result_remove_store:
        print(f"Курьер забрал {data_request.amount} {data_request.product} со склада\n"
              f"Курьер везет {data_request.amount} {data_request.product} со склада в магазин")
        # Добавляем товар в магазин, если есть место.
        result_add_shop = shop.add(data_request.product, data_request.amount)
        # Если удалось доставить в магазин товар, то выводим сообщение об успехе.
        if result_add_shop:
            print(f"Курьер доставил {data_request.amount} {data_request.product} в магазин")
        else:
            # Если НЕ удалось доставить в магазин товар, то возвращаем товар на склад.
            store.add(data_request.product, data_request.amount)
            print(f"Курьер вернул обратно {data_request.amount} {data_request.product} на склад")

    # Выводим сообщение о том, какой товар, сколько и где хранится.
    print("\nНа складе есть: ")
    for k_item, v_item in store.get_items().items():
        print(f"{v_item} {k_item}")

    print("\nВ магазине есть: ")
    for k_item, v_item in shop.get_items().items():
        print(f"{v_item} {k_item}")
