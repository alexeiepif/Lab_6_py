#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести все буквы м и н в нем.

import sys


if __name__ == '__main__':
    sentence = input("Введите предложение на русском языке: ")

    letters_m_n = []

    for letter in sentence:
        if (letter == 'м' or letter == 'М'
                or letter == 'н' or letter == 'Н'):
            letters_m_n.append(letter)

    if not letters_m_n:
        print("Букв 'м' и 'н' нет в данном предложении", file=sys.stderr)
        exit(1)
        
    print("Буквы 'м' и 'н' в предложении:", ', '.join(letters_m_n))
