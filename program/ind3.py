#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово, оканчивающее символом «.».
# Вставить заданную букву после первой буквы и.

import sys


if __name__ == '__main__':
    word = input("Введите слово, оканчивающееся символом '.':\n")
    if not word.endswith('.'):
        print("Ошибка: Входное слово не оканчивается символом '.'!",
              file=sys.stderr)
        exit(1)
    # Ищем индекс первой буквы "и"
    index_of_i = word.find('и')

    if index_of_i != -1:
        letter = input("Введите букву: ")
        # Вставляем заданную букву после первой буквы "и"
        inserted_word = word[:index_of_i + 1] + \
            letter + word[index_of_i + 1:]

        print("Результат:", inserted_word)
    else:
        print("Ошибка: В слове нет буквы 'и'.", file=sys.stderr)
        exit(1)
