"""
Модуль для створення кольорових повідомлень у консолі.
"""
colour = {
    'red': '31m',
    'black': '30m',
    'green': '32m',
    'yellow': '33m',
    'blue': '34m',
    'purpure': '35m',
    'biruza': '36m',
    'white': '37m'
}


def color_text(text, colour_name):
    """
    Застосовує колір до тексту згідно із заданою назвою кольору.
    :param text: Текст, який потрібно вивести з кольором.
    :param colour_name: Назва кольору із словника `colour`.
    :return: Рядок із застосованим кольором.
    """
    coloured_txt = '\033[' + colour_name + text + '\033[0m'
    return coloured_txt


def styled(text, code="3m"):
    """
    Застосовує стиль до тексту згідно із заданим кодом стилю.
    :param text: Текст, який потрібно стилізувати.
    :param code: Код стилю (за замовчуванням "3m").
    :return: Рядок із застосованим стилем.
    """
    clean_style_code = '\033[0m'
    styled_txt = f'\033[{code}{text}{clean_style_code}'
    return styled_txt


def error_message(message):
    """
    Створює повідомлення про помилку із відповідними кольорами.
    :param message: Текст помилки.
    :return: Рядок із повідомленням про помилку.
    """
    status = "ERROR"
    error = color_text(f"{status:<8} ", colour['red'])
    _message = color_text(message, colour['yellow'])
    err_message = error + _message
    return err_message


def warning_message(message):
    """
    Створює повідомлення про попередження із відповідними кольорами.
    :param message: Текст попередження.
    :return: Рядок із попередженням.
    """
    status = "WARNING"
    warn = color_text(f"{status:<8} ", colour['yellow'])
    _message = color_text(message, colour['biruza'])
    warn_message = warn + _message
    return warn_message


def info_message(message):
    """
    Створює повідомлення інформаційне із відповідними кольорами.
    :param message: Текст інформаційного повідомлення.
    :return: Рядок із інформаційним повідомленням.
    """
    status = "INFO"
    info = color_text(f"{status:<8} ", colour['purpure'])
    info_message = info + message
    return info_message


def custom_styled_text(text, color=None, background=None, style=None):
    """
     Створює стилізований текст з заданими параметрами.
    :param text: Текст, який потрібно стилізувати.
    :param color: Колір тексту (за замовчуванням None).
    :param background: Колір фону (за замовчуванням None).
    :param style: Стиль тексту (за замовчуванням None).
    :return: Рядок із застосованими стилізацією, кольором тексту та фоном.
    """
    style_code = f"\033[{style}m" if style else ""
    color_code = f"\033[{colour[color]}m" if color else ""
    background_code = f"\033[{int(colour.get(background, '32')[:-1]) + 10}m" if background else ""
    clean_style_code = "\033[0m"

    styled_txt = f"{style_code}{color_code}{background_code}{text}{clean_style_code}"
    return styled_txt


"""
Example:
s = "\033[3m"         # відповідає за стиль
c = "\033[33m"       # відповідає за кольор
f  = "\033[41m";    #  відповідає за фон
clean = "\033[0m"  # очистка налаштувань
pattern = f"{s}{c}{f}{txt}{clean}"
"""


if __name__ == "__main__":
    """ Приклад використання:    """
    print(warning_message("ups i did sit again"))
    print(error_message("wrong way"))
    print(info_message("thanks for info"))
    custom_text = custom_styled_text("Custom Text", color="red", background="red", style="1")
    print(custom_text)


