"""
Реализуйте алгоритм, определяющий, все ли символы в строке встречаются
только один раз.
"""


def check_identity(text: str) -> bool:
    text = list(text)  # Превращаем наш текст в list
    text.sort()  # Sorting text
    tmp_ch = text[0]  # Создаем переменную которая отвечает за проверку

    for i in range(1, len(text)):
        if text[i] != tmp_ch:  # проверяем преведуйший символ со следуйшим
            tmp_ch = text[i]  # меняем преведуйший символ со следуйшим
        else:
            return False  # если они равны значит символы повторяются
    return True  # если цикл завершился и не было равенства то повторенией нет!


if __name__ == '__main__':
    txt = list(input("Введите текст-:"))
    print(check_identity(txt))
