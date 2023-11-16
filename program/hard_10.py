#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Даны три слова. Напечатать только те буквы слов, 
# которые есть лишь в одном из слов. Рассмотреть два варианта:
# повторяющиеся буквы каждого слова рассматриваются; 
# повторяющиеся буквы каждого слова не рассматриваются.

def find_unique_letters_with_repeats(words):
    letters = list(''.join(words))
    unique_letters = []
    for letter in letters:
        if letter not in unique_letters:
            unique_letters.append(letter)
    result = []
    for letter in unique_letters:
        count = 0
        for word in words:
            if letter in word:
                count += 1
        if count == 1:
            result.append(letter)

    return result


def find_unique_letters_without_repeats(words):
    letters = list(''.join(words))
    unique_letters = []
    for letter in letters:
        if letter not in unique_letters:
            unique_letters.append(letter)
    result = []
    for letter in unique_letters:
        count = 0
        for word in words:
            if word.count(letter) > 1:
                count = 0
                break
            elif letter in word:
                count += 1
        if count == 1:
            result.append(letter)

    return result


if __name__ == '__main__':
    # Запрос ввода трёх слов у пользователя
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")
    word3 = input("Введите третье слово: ")

    words = [word1.lower(), word2.lower(), word3.lower()]
    # Решаем первый вариант и выводим результат
    result1 = find_unique_letters_with_repeats(words)
    print("Повторяющиеся буквы каждого слова рассматриваются:", result1)

    # Решаем второй вариант и выводим результат
    result2 = find_unique_letters_without_repeats(words)
    print("Повторяющиеся буквы каждого слова не рассматриваются:", result2)
