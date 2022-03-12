# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
# Разработайте регулярное выражение для идентификации в англоязычном тексте конструкций Unreal Conditional (Past) по модели: If <…> had <...>, … would have… . (например: If he had had time, Ted would have mowed the grass).
# Импортируем библиотеку Регулярных выражений
import re
# Состовляем Регулярное выражение ыражение для идентификации в англоязычном тексте конструкций Unreal Conditional (Past)
regex = r"If(.{1,})had(.{1,})would(.{1,})(\.)"
# Вводим текст в котором будет осуществляться поиск
test_str = ("Madam im.Adam Tenet Stats Was it a car or a cat I saw? 2 3\n"
	"He was like: «Wow!» If he had time, Ted would mow the grass. ")
# Используем фунцкцию re.search чтобю найти в строке string первую строчку, подходящую под шаблон pattern;
matches = re.search(regex, test_str)
# Определяем совпадения
if matches:
    print ("Match was found at {start}-{end}: {match}".format(start = matches.start(), end = matches.end(), match = matches.group()))
# Используем цикл for in для выделения всех совпадений
    for groupNum in range(0, len(matches.groups())):
        groupNum = groupNum + 1
# Выводим итоговый результат       
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = matches.start(groupNum), end = matches.end(groupNum), group = matches.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
