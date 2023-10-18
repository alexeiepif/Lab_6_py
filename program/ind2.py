#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дана последовательность слов. Проверить,
# правильно ли в ней записаны буквосочетания жи и ши.

if __name__ == '__main__':
    words = input("Введите последовательность слов: ").split()

    errors = []
    toogle = False
    for word in words:
        if "жи" in word or "ши" in word:
            toogle = True
        elif "жы" in word or "шы" in word:
            toogle = True
            errors.append(word)

    if not toogle:
        print("В последовательности слов нет буквосочетаний\nкоторые необходимо проверить")
    elif len(errors) == 0:
        print("В последовательности нет ошибок с буквосочетаниями 'жи' и 'ши'.")
    else:
        print("Обнаружены ошибки в следующих словах:")
        for error in errors:
            if "жы" in error:
                print(f"Ошибка в слове '{error}': буквосочетание 'жы'")
            else:
                print(f"Ошибка в слове '{error}': буквосочетание 'шы'")
