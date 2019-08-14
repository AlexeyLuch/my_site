# f = open('/home/usr/base.txt', 'r')
# g = open('/home/usr/read.txt', 'a')
# for line in f:
#     g.write(line)
#     print(line)
# f.close()
# import sqlite3
# import datetime
# import re
# con = sqlite3.connect('db.sqlite3')
# cur = con.cursor()
# with open("/home/usr/base.txt") as infile:
#     now = datetime.datetime.now()
#     day_month = now.day,now.month
#     print(day_month)
#     for line in infile:
#         data = line.split(";")
#         test=re.findall('(?:\+|\d+)[\d\-\(\) ]{9,}\d+', data[0])
#         cur.execute( 'INSERT INTO poll_phonebase ( reg_date,phone_persone, name_persone) VALUES ( "%s","%s","%s" )'%(day_month,test,data[1]))
#         con.commit()
#
#         print(test)
#         # записать test и data[1] в базу
#
#
#
#
#
# con = sqlite3.connect('db.sqlite3')
# cur = con.cursor()
# cur.execute('SELECT * FROM poll_phonebase')
# print(cur.fetchall())
#
# def intro(**data):
#     print("\nData type of argument: ",type(data))
#
#     for key, value in data.items():
#         print("{} is {}".format(key, value))
#
# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# #
""""""""""""""""""""""""""""""""""""


"""keyword"""


# def rest(**rest):
#     for key,value in rest.items():
#         print("{} are {}".format(key, value))
#
# rest(Alexey="Luch",Alexey2= "Vorchun",Andrey="Kassad")


""" swap """

# a = 20
# b = 21
# a, b = b, a
# print("a = %d and b = %d" % (a,b))

""" list to string """

# a = ["sada","reter","kust","veter"]
# print("it\'s the string==> "+" ".join(a))

# print(list(map(abs, (-1, 0, 1))))  """ HZ 4TO """

""" use MAP for make list to string and back """

# old_list = [1,2,3,4]
# new_list = list(map(str, old_list))
# print(new_list)
# old_list = list(map(int, new_list))
# print(old_list)

""" tuple = кортеж / преобразование """
# a = tuple('hello, world!')
# print(a)
# b = tuple(a)
# print(b)

""" lambda """

# func = lambda x,y : +x
# print(func(2,3))
""" Except """
# try:
#     k= 1/0
#     print("True")
# except ZeroDivisionError:
#     print("False")

""" iterating over file’s lines """

# with open("intents.json") as files:
#     for i in files:
#         print(i)

"""lists in dict """

# uniq = [1,2,3,4]
# fifa = ['a','b','c','d','e']
# c = dict(zip(uniq,fifa))
# print(c)

""" list to string (for) """

# c = str()
# fifa = ['a','b','c','d','e']
# for x in fifa:
#     c+=x
# print(c)
# print(type(c))

""" revers """

# fifa = ['2','3','1','2','4']
# c = fifa[::-1]
# print(c)

""" узнать путь к импорту """

# import sys
#
# print(sys.path)

# a = ["a","s"]
# b = ["1a","1s","1d"]
# c = dict(zip(a,b))
# print(c)
"""Список простых чисел"""
# from math import sqrt
# n = int(input("n="))
# lst=[]
# for i in range(2, n+1):
#     if (i > 10):
#         if (i%2==0) or (i%10==5):
#             continue
#     for j in lst:
#         if j > int((sqrt(i)) + 1):
#             lst.append(i)
#             break
#         if (i % j == 0):
#             break
#     else:
#         lst.append(i)
# print (lst)

"""Простое число или нет"""
# def index(rest):
#     deliteli = 1
#     i = 1
#     while i <= rest:
#         i += 1
#         if rest % i == 0:
#             print(rest,i)
#             deliteli +=1
#             if deliteli >2:
#                 print(False)
#                 break
#
#     if deliteli <= 2:
#         print(True)
# index(117)

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
#
# fruits.update(more_fruits)
# print(fruits)
# car ={
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))

""" list comprehensions """
# arr = {1,2,34}
# x = (i for i in arr)
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
""" декораторы """
# def my_shiny_new_decorator(function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
#     # получая возможность исполнять произвольный код до и после неё.
#     def the_wrapper_around_the_original_function():
#         print("Я - код, который отработает до вызова функции")
#         function_to_decorate() # Сама функция
#         print("А я - код, срабатывающий после")
#     # Вернём эту функцию
#     return the_wrapper_around_the_original_function
#
# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# def stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
#
#
# # Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# # который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# # готовую к использованию функцию:
# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Оставь меня в покое")
#
# another_stand_alone_function()
""" Instagram API """
# import requests
#
# response = requests.get('https://api.instagram.com/v1/users/17768547978/?access_token=')
# response = requests.get('https://api.instagram.com/v1/users/17768547978/media/recent/?access_token=')
# response = requests.get('https://api.instagram.com/oembed/?url=http://instagr.am/p/B05JNd3nS06/')
# response = requests.get('https://api.instagram.com/v1/media/1405754808615775546_1234223790/likes/?access_token=')
#
# response = requests.post('https://api.instagram.com/v1/media/558717847597368461_9538472/likes/?access_token=')
#
# print(response.content)
# print(response.json())
import json

# some JSON:

# parse x:

# products = [
#     {
#         "discontinued": 0,
#         "lead_time_days": 4,
#         "product_category": "Toy",
#         "product_description": "Pull out a bock without crashing the stack ...",
#         "product_id": 101,
#         "product_name": "Jenga Classic Game",
#         "reorder_level": 50,
#         "unit_price": 14.99
#     },
#     {
#         "discontinued": 0,
#         "lead_time_days": 4,
#         "product_category": "Wireless Phone Accessory",
#         "product_description": "Display: 2.5 inches Camera: 2 MP Talk Time: 4.5 hours Weight: 3.3 ounces",
#         "product_id": 102,
#         "product_name": "AT&T Z431 GoPhone (AT&T)",
#         "reorder_level": 14,
#         "unit_price": 49.99
#     },
#     {
#         "discontinued": 1,
#         "lead_time_days": 4,
#         "product_category": "Wireless Phone Accessory",
#         "product_description": "Display: 4.5-inches Camera: 5-MP Input: Touchscreen OS: Android",
#         "product_id": 103,
#         "product_name": "AT&T Z998 LTE Android Go Phone (AT&T Prepaid)",
#         "reorder_level": 29,
#         "unit_price": 159.99
#     },
#     {
#         "discontinued": 1,
#         "lead_time_days": 4,
#         "product_category": "Personal Computers",
#         "product_description": "8 inch Display (1920x1200) ...",
#         "product_id": 104,
#         "product_name": "NVIDIA SHIELD Tablet (WiFi)",
#         "reorder_level": 10,
#         "unit_price": 299.0
#     }
# ]
#
# print_messages = [' - '.join([product['product_name'], product['product_description']])
#                   for product in products if product['discontinued']]
#
# for message in print_messages:
#     print(message + "/n")

# names = ['Adam', 'Bob', 'Cyril']
# print("Winners are:", *names, sep="\n")




def bablu_sort(nums):
    cicle = True

    while cicle:
        cicle = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
                cicle = True

list_numb = [1,12,32,2,4,3,1]
bablu_sort(list_numb)
print(list_numb)