# poem_printer.py
from mcolour_modify import custom_styled_text, warning_message

def print_poem():
    poem = """
    Світає,
    Край неба палає,
    Соловейко в темнім гаї
    Сонце зустрічає.
    Тихесенько вітер віє,
    Степи, лани мріють,
    Меж ярами над ставами
    Верби зеленіють.
    Сади рясні похилились,
    Тополі по волі
    Стоять собі, мов сторожа,
    Розмовляють з полем.
    І все то те, вся країна,
    Повита красою,
    Зеленіє, вмивається
    Дрібною росою,
    Споконвіку вмивається,
    Сонце зустрічає.
    І нема тому почину,
    І краю немає!
    """

    # Виведення вірша з використанням стилів
    custom_poem = custom_styled_text(poem, color="blue", background="purpure", style="3", bold_keywords=["Соловейко", "країна"])
    print(custom_poem)


if __name__ == "__main__":
    print_poem()
