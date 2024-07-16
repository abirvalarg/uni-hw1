#!/usr/bin/python

HUNDREDS = ('', 'сто ', 'двести ', 'триста ', 'четыреста ', 'пятьсот ', 'шестьсот ', 'семьсот ',
            'восемсот ', 'девятьсот ')
TENS = ('', None, 'двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ', 'семьдесят ',
        'восемьдесят ', 'девяносто ')
TENS_PLUS_ONES = ('десять', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
                  'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать')
ONES = ('', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')

ORDERS = (HUNDREDS, TENS, ONES)

inputValue = input('> ')
inputValue = '0' * (3 - len(inputValue)) + inputValue

result = []
for digit, order in zip(inputValue, ORDERS):
    word = order[int(digit)]
    if word is None:
        result.append(TENS_PLUS_ONES[int(inputValue[-1])])
        break
    else:
        result.append(word)
print(''.join(result))
