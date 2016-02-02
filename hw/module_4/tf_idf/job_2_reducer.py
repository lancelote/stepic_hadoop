# coding=utf-8

""""
Реализуйте reducer второй mapreduce задачи для расчета TF-IDF с помощью
Hadoop Streaming.

Входные данные: ключ - слово, значение - тройка: номер документа, tf слова
в документе и 1 (разделены ';').

Выходные данные: ключ - пара: слово, номер документа (разделены '#'),
значение - пара: tf слова в документе, n - количество документов
с данным словом (разделены табуляцией).

Sample Input:

    aut	1;4;1
    aut	2;2;1
    bene	2;1;1
    de	2;1;1
    mortuis	2;1;1
    nihil	1;1;1
    nihil	2;1;1
    Caesar	1;1;1

Sample Output:

    aut#1	4	2
    aut#2	2	2
    bene#2	1	1
    de#2	1	1
    mortuis#2	1	1
    nihil#1	1	2
    nihil#2	1	2
    Caesar#1	1	1
"""

import sys

prev_word = ''
n = 1
data = []

for line in sys.stdin:
    word, metadata = line.strip().split('\t')
    doc, frequency, _ = metadata.split(';')

    if not prev_word:
        prev_word = word
        data = [(doc, frequency)]
        continue

    if word == prev_word:
        n += 1
        data.append((doc, frequency))
    else:
        for document in data:
            print('%s#%s\t%s\t%d' % (prev_word, document[0], document[1], n))
        prev_word = word
        n = 1
        data = [(doc, frequency)]

for document in data:
    print('%s#%s\t%s\t%d' % (prev_word, document[0], document[1], n))
