
with open('text_file.txt', 'w') as file:
    while True:
        user_input = input("Введіть рядок (порожній рядок для завершення): ")
        if user_input == "":
            break
        file.write(user_input + '\n')

print("Дані записано у файл 'text_file.txt'.")
