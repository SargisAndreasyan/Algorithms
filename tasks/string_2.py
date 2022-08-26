"""
Для двух строк напишите метод, определяющий, является ли одна строка
перестановкой другой.
Задача из книги Карьера программиста.
"""


def check_permutation(txt1: str, txt2: str) -> bool:
    txt1, txt2 = list(txt1), list(txt2)  # Превращаем нашы тексты в list
    txt1.sort()  # Sorting text
    txt2.sort()  # Sorting text
    if txt1 == txt2:  # Если тексты равны
        return True  # то это перестановка
    else:
        return False  # иначе не перестановка


if __name__ == '__main__':
    text1 = 'abac'
    text2 = 'acb'
    print(check_permutation(text2,text1))
