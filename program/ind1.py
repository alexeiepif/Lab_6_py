#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести все буквы м и н в нем.

if __name__ == '__main__':
    sentence = input("Введите предложение на русском языке: ")

    letters_m_n = []

    for letter in sentence:
        if (letter == 'м' or letter == 'М'
                or letter == 'н' or letter == 'Н'):
            letters_m_n.append(letter)

    print("Буквы 'м' и 'н' в предложении:", ', '.join(letters_m_n))
