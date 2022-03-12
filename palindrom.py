# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# Разработайте регулярное выражение для идентификации в англоязычном тексте слов-палиндромов из 2-5 букв (например, ee, eye, noon, kayak).
# Импортируем библиотеку Регулярных выражений
import re
# Составляем регулярное выражение для поиска палиндромов
regex = r"\b([a-z])?([a-z])?([a-z])?\2\1\b"
# Вводим текст в котором бует производится поиск
test_str = "Madam im.Adam Tenet Stats Was it a car or a cat I saw? 2 3"
# Используем функцию finditer Итератор всем непересекающимся шаблонам
matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)
# Вводим цикл для поиска всех результатов а не одного
for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
# Вводим цикл для нумерования совпадений
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
# Выводим все совпадения в терминал      
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.