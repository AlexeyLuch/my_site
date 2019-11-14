#
# c = [1,2,3,4,5,6]
# for i in range(len(c),-1,-1):
#     print(i)

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
        # записать test и data[1] в базу

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
#
""""""""""""""""""""""""""""""""""""
from urllib import request

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
# c = ("it\'s the string==> "+" ".join(a))
# b = c.split(" ")
# print(c)
# print(b)

# print(list(map(abs, (-199, 0, 1,2))))

""" use MAP for make list to string and back """

# old_list = [1,2,7,5,4,3,3,4]
# c = sorted(old_list)
# print(c)
# new_list = list(map(str, c))
# print(new_list)
# old_list = list(map(int, new_list))
# print(old_list)

""" tuple = кортеж / преобразование """
# a = tuple('hello, world!')
# print(a)
# b = tuple(a)
# print(b)

""" lambda """

# func = lambda x,y : y+x
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

# c = ""
# fifa = ['a','b','c','d','e']
# for x in fifa:
#     c+=x
# print(c)
# print(type(c))

""" revers """

# fifa = ['2','3','1','2','4']
# c = sorted(fifa)[::-1]
# print(c)

""" узнать путь к импорту """

# import sys
# print(sys.path)

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

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
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
# index(4)
""""""
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
""" bubble_sort """
# def bubble_sort(nums):
#     cicle = True
#
#     while cicle:
#         cicle = False
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i+1]:
#                 nums[i],nums[i+1] = nums[i+1],nums[i]
#                 cicle = True
#
# list_numb = [1,12,32,2,4,3,1,0,0,0,0,0,0]
# bubble_sort(list_numb)
# print(list_numb)

""" selection_sort """

# def selection_sort(nums):
#     # Значение i соответствует кол-ву отсортированных значений
#     for i in range(len(nums)):
#         # Исходно считаем наименьшим первый элемент
#         lowest_value_index = i
#         # Этот цикл перебирает несортированные элементы
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[lowest_value_index]:
#                 lowest_value_index = j
#         # Самый маленький элемент меняем с первым в списке
#         nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
#
# # Проверяем, что оно работает
# random_list_of_nums = [12, 8, 3, 20, 11]
# selection_sort(random_list_of_nums)
# print(random_list_of_nums)

""" """
# import pprint
# n = 3
# distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
# pprint.pprint(distance)

# Ans = ['red', 'green', 'white']
# Word = ['red', 'white', 'green', 'blue']
#
# uniqe = list(set(Ans+Word))
# print(uniqe)
#
# cross = list(set(Ans) & set(Word))
# print(cross)
#
# different = list(set(Ans) ^ set(Word))
# print(different)
#
# result=list(set(Word) - set(Ans))
# print(result)

# class A():
#     attr_1 = 'Spam_!'
#     attr_2 = 'Eggs'
#     attr_3 = 'Ni_!Ni!Ni!Ni!Ni!Ni!Ni!Ni!'
#
#
#
# x = A()
# for attr in dir(x):
#     if not attr.startswith('_'):  # Если не внутренний и не служебный
#         print(getattr(x, attr))


# import requests
# from lxml import html
# import random
# def random_fink_fan():
#     response = requests.get('https://www.youtube.com/results?search_query=%D1%82%D1%80%D0%B5%D0%B9%D0%BB%D0%B5%D1%80%D1%8B+2019&sp=CAE%253D')
#     parser_tree = html.fromstring(response.content)
#     content = parser_tree.xpath('//*[contains(@class, "yt-lockup-thumbnail")]/a[@href]')
#     links = [el.get('href') for el in content]
#     print("\nrandom.choice() to select random item from list - ", random.choice(links))
# random_fink_fan()

# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#   def test_upper(self):
#       self.assertEqual('foo'.upper(), 'FOO')
#
#   def test_isupper(self):
#       self.assertTrue('FOO'.isupper())
#       self.assertFalse('foo'.isupper())
#
#   def test_split(self):
#       s = 'hello world'
#       self.assertEqual("ыы", "ыы")
#       # Проверим, что s.split не работает, если разделитель - не строка
#       with self.assertRaises(TypeError):
#           s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()

# import random
# import time
# from threading import Thread
#
#
# class MyThread(Thread):
#     """
#     A threading example
#     """
#
#     def __init__(self, name):
#         """Инициализация потока"""
#         Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#         """Запуск потока"""
#         amount = random.randint(3, 15)
#         time.sleep(amount)
#         msg = "%s is running" % self.name
#         print(msg)
#
#
# def create_threads():
#     """
#     Создаем группу потоков
#     """
#     for i in range(5):
#         name = "Thread #%s" % (i + 1)
#         my_thread = MyThread(name)
#         my_thread.start()
#
#
# if __name__ == "__main__":
#     create_threads()

"Сортировка Телеграм"
#
c = open("all","r",encoding="utf8")
a = open("numb","a",encoding="utf8")
b = open("user","a",encoding="utf8")
for i in c:
    if i[0] == "@":
        b.write(i)
    elif i[0] == "+":
        a.write(i)

c.close()
b.close()
a.close()
"""split the entered text into two variables """

# n, m = map(int, input().split(";"))
# print(n)
# print(m)
#


# import requests
# ip = "78.137.4.44"
# country = requests.get("https://ipinfo.io/%s?token=77a09218c42d10" % ip)
# t = {"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria", "BA": "Bosnia and Herzegovina", "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Barthelemy", "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", "WS": "Samoa", "BQ": "Bonaire, Saint Eustatius and Saba ", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey", "BY": "Belarus", "BZ": "Belize", "RU": "Russia", "RW": "Rwanda", "RS": "Serbia", "TL": "East Timor", "RE": "Reunion", "TM": "Turkmenistan", "TJ": "Tajikistan", "RO": "Romania", "TK": "Tokelau", "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala", "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea", "GP": "Guadeloupe", "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana", "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", "GA": "Gabon", "SV": "El Salvador", "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", "OM": "Oman", "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong", "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico", "PS": "Palestinian Territory", "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen", "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", "PF": "French Polynesia", "PG": "Papua New Guinea", "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", "PL": "Poland", "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "EE": "Estonia", "EG": "Egypt", "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam", "SB": "Solomon Islands", "ET": "Ethiopia", "SO": "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia", "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova", "MG": "Madagascar", "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar", "ML": "Mali", "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia", "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", "MV": "Maldives", "MQ": "Martinique", "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man", "UG": "Uganda", "TZ": "Tanzania", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France", "IO": "British Indian Ocean Territory", "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji", "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia", "NE": "Niger", "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", "XK": "Kosovo", "CI": "Ivory Coast", "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile", "CC": "Cocos Islands", "CA": "Canada", "CG": "Republic of the Congo", "CF": "Central African Republic", "CD": "Democratic Republic of the Congo", "CZ": "Czech Republic", "CY": "Cyprus", "CX": "Christmas Island", "CR": "Costa Rica", "CW": "Curacao", "CV": "Cape Verde", "CU": "Cuba", "SZ": "Swaziland", "SY": "Syria", "SX": "Sint Maarten", "KG": "Kyrgyzstan", "KE": "Kenya", "SS": "South Sudan", "SR": "Suriname", "KI": "Kiribati", "KH": "Cambodia", "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia", "KR": "South Korea", "SI": "Slovenia", "KP": "North Korea", "KW": "Kuwait", "SN": "Senegal", "SM": "San Marino", "SL": "Sierra Leone", "SC": "Seychelles", "KZ": "Kazakhstan", "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic", "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "British Virgin Islands", "DE": "Germany", "YE": "Yemen", "DZ": "Algeria", "US": "United States", "UY": "Uruguay", "YT": "Mayotte", "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", "LA": "Laos", "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka", "LI": "Liechtenstein", "LV": "Latvia", "TO": "Tonga", "LT": "Lithuania", "LU": "Luxembourg", "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", "TF": "French Southern Territories", "TG": "Togo", "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libya", "VA": "Vatican", "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra", "AG": "Antigua and Barbuda", "AF": "Afghanistan", "AI": "Anguilla", "VI": "U.S. Virgin Islands", "IS": "Iceland", "IR": "Iran", "AM": "Armenia", "AL": "Albania", "AO": "Angola", "AQ": "Antarctica", "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba", "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia", "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}
# c = (country.json())
# all = c["region"]
# all1 = c["country"]
# print(t[all1])
# print(all)
# print(all1)
