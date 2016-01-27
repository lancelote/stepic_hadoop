# coding=utf-8

""""
Реализуйте reducer первой mapreduce задачи для расчета TF-IDF с помощью
Hadoop Streaming.

Ключ входных данных составной: он содержит слово и номер документа через "#".

Ключом в выходных данных является слово, а значение состоит из двух элементов,
разделенных табуляцией: номер документа и tf (сколько раз данное слово
встретилось в данном документе).

Sample Input:

    aut#1	1
    aut#1	1
    aut#1	1
    aut#1	1
    aut#2	1
    aut#2	1
    bene#2	1
    de#2	1
    mortuis#2	1
    nihil#1	1
    nihil#2	1
    Caesar#1	1

Sample Output:

    aut	1	4
    aut	2	2
    bene	2	1
    de	2	1
    mortuis	2	1
    nihil	1	1
    nihil	2	1
    Caesar	1	1
"""

import sys

frequency = 1
prev_word, prev_doc = '', ''
word, doc = '', ''

for line in sys.stdin:
    word_reference, _ = line.strip().split()
    word, doc = word_reference.split('#')

    if not prev_word:
        prev_word = word
        prev_doc = doc
        continue

    if word == prev_word and doc == prev_doc:
        frequency += 1
    else:
        print('%s\t%s\t%d' % (prev_word, prev_doc, frequency))
        prev_word = word
        prev_doc = doc
        frequency = 1

print('%s\t%s\t%d' % (word, doc, frequency))
