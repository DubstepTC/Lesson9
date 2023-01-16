
        # Первое задание
        # ------------------------------------------------------------------
# import copy
#
# first = tuple("hello", 21, 2.13, "square", 89,)
# second = copy.copy(first)
# third = first[:]
#
# print(first)
# print(second)
# print(third)


        # Второе задание
        # ------------------------------------------------------------------
# import random
#
# def kar(n) :
#     if n == 1:
#         kar = tuple(random.randint(0, 5) for i in range(10))
#         return kar
#     elif n == 2:
#         kar = tuple(random.randint(-5, 0) for i in range(10))
#         return kar
#
# kart1 = kar(1)
# kart2 = kar(2)
# kart3 = kart1 + kart2
#
# print("Первый кортеж: " + str(kart1))
# print("Второй кортеж: " + str(kart2))
#
# print("Третий кортеж: " + str(kart3))
# print("В нём столько нулей: " + str(kart3.count(0)))

        # Третье задание
        #------------------------------------------------------------------

# school = {"1А" : 25, "2Б" : 23, "11Г" : 17 , "8А" : 27 , "4Г" : 30 , "6Б" : 24 , "2А" : 25 , "3Д" : 23 , "9В" : 28 }
# print("Словарь до изменения" + str(school))
# sum = 0
# for value in school.values() :
#     sum = sum + int(value)
# print("Всего учеников: " + str(sum))
#
# school["6Б"]= 5
# school["1А"]= 19
# school.setdefault("6Д", 27)
# school.setdefault("9Г", 19)
# school.pop("11Г")
# school.pop("4Г")
# school.pop("3Д")
#
# print("Словарь после изменения" + str(school))
# sum = 0
# for value in school.values() :
#     sum = sum + int(value)
# print("Всего учеников: " + str(sum))


        # Четвертое задание
        #------------------------------------------------------------------
def obr(sl):
    for key, value in sl:
        sl2[value] =  key
    return sl2

sl1 = {1 : "hello", 2 : "world", 3 : "dog", 4 : "cat", 5 : "end"}
sl2 = {}

print("Исходный кортеж: " + str(sl1))
sl = sl1.items()
print("Переделанный кортеж: " + str(obr(sl)))
