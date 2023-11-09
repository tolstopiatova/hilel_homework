def update_hero(**kwargs):
    # Відкриваємо файл hero.ini для читання
    with open("hero.ini", "r") as file:
        lines = file.readlines()

    # Створюємо словник для збереження полів та їх значень
    data = {}
    for line in lines:
        key, value = line.strip().split("=")
        data[key] = value

    # Оновлюємо значення відповідно до переданих параметрів
    for key, value in kwargs.items():
        if key in data:
            data[key] = str(value)

    # Записуємо оновлений вміст файлу
    with open("hero.ini", "w") as file:
        for key, value in data.items():
            file.write(f"{key}={value}\n")

# Приклад виклику функції для оновлення полів
update_hero(hero="Halk", power=450, Y=2.3)
