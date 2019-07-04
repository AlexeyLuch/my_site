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
#
#
def rest(**rest):
    for key,value in rest.items():
        print("{} are {}".format(key, value))

rest(Alexey="Luch",Alexey2= "Vorchun",Andrey="Kassad")

# a = 20
# b = 21
#
# a, b = b, a
#
# print("a = %d and b = %d" % (a,b))

# a = ["sada","reter","kust","veter"]
# print("it\'s the string==> "+" ".join(a))
# print(list(map(abs, (-1, 0, 1))))

old_list = [1,2,3,4]
new_list = list(map(str, old_list))
print(new_list)

# a = tuple('hello, world!')
# print(a)

# func = lambda x,y : +x
# print(func(2,3))

# x = 0
# try:
#     k= 1/0
#     print("True")
# except ZeroDivisionError:
#     print("False")

# with open("intents.json") as files:
#     for i in files:
#         print(i)

# uniq = [1,2,3,4]
# fifa = ['a','b','c','d','e']
# print(dict(zip(uniq, fifa)))



fifa = ['a','b','c','d','e']
for x in fifa[:]:
    print(x)