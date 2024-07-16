#!/usr/bin/python
HUNDREDS = ('', 'сто ', 'двести ', 'триста ', 'четыреста ', 'пятьсот ', 'шестьсот ', 'семсот ',
            'восемсот ', 'девятьсот ')
TENS = ('', None, 'двадцать ', 'тридцать ', 'сорок ', 'пятьдесят ', 'шестьдесят ', 'семдесят ',
        'восемьдесят ', 'девяносто ')
TENS_PLUS_ONES = ('десять', 'одинадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
                  'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать')
ONES = ('', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять')

ORDERS = (HUNDREDS, TENS, ONES)

def to_words(inputValue):
    inputValue = str(inputValue)
    inputValue = '0' * (3 - len(inputValue)) + inputValue

    result = []
    for digit, order in zip(inputValue, ORDERS):
        word = order[int(digit)]
        if word is None:
            result.append(TENS_PLUS_ONES[int(inputValue[-1])])
            break
        else:
            result.append(word)
    return ''.join(result)

with open('dumb-numbers.py', 'w') as fp:
    fp.writelines(['if x == 1:\n', '    print(\'один\')\n'])
    for x in range(2, 1000):
        fp.writelines([f'elif x == {x}:\n', f'    print(\'{to_words(x).strip()}\')\n'])
