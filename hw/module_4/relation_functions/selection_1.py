# coding=utf-8

"""
Дан файл с логами переходов пользователей. Каждая строка состоит из 3 полей:
время перехода (unix timestamp), ID пользователя, URL, на который перешел
пользователь.

Напишите mapper с помощью Hadoop Streaming, печатающий только те строки из
файла, которые соответствуют пользователю user10.

Sample Input:

    1448713968	user2	https://ru.wikipedia.org/
    1448764519	user10	https://stepic.org/
    1448713968	user5	http://google.com/
    1448773411	user10	https://stepic.org/explore/courses
    1448709864	user3	http://vk.com/

Sample Output:

    1448764519	user10	https://stepic.org/
    1448773411	user10	https://stepic.org/explore/courses
"""

import sys

for line in sys.stdin:
    timestamp, user_id, url = line.strip().split('\t')
    if user_id == 'user10':
        print(line.strip())
