#打印测试
# print("Hello");
# """
# 啊啊所大所多
# """
# if True:
#     print("yes")
# else:
#     print("no")
#
# str = 'Runoob'
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始后的所有字符
# print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
# print(str * 2)  # 输出字符串两次
# print(str + '你好')  # 连接字符串
#
# print('------------------------------')
#
# print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# input("\n\n按下回车键后退出")
# import sys; x = 'xuqianlei'; sys.stdout.write(x + '\n')
# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)
#
# print('---------')
# # 不换行输出
# print(x, end=" ")
# print(y, end=" ")
# print()
# import sys
# from sys import argv,path
# print('命令行参数为: ')
# for i in argv:
#     print(i)
# print('\n python路径为', path)
# import sys
# print ('参数个数为:', len(sys.argv), '个参数。')
# print ('参数列表:', str(sys.argv))
# print ('脚本名:', str(sys.argv[0]))
# import sys
# import getopt
# def site():
#     name = None
#     url = None
#
#     argv = sys.argv[1:]
#
#     try:
#         opts, args = getopt.getopt(argv, "a:u:")
#     except:
#         print("Error")
#     for opt, arg in opts:
#         if opt in ['-a']:
#             name = arg
#         elif opt in ['-u']:
#             url = arg
#     print(name + " " + url)
# site()
# counter = 100          # 整型变量
# miles   = 1000.0       # 浮点型变量
# name    = "runoob"     # 字符串
#
# print (counter)
# print (miles)
# print (name)
# a, b, c, d = 10, 2.2, True, 4+3j
# print(type(a))
# print(type(b))
# print(type(c))
# # print(type(d))
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
#
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表
# a = [1, 2, 3, 4, 5]
# print(a[:])
# a[0] = 9
# print(a[:])
# a[0] = []
# print(a[0])
# def reverseWords(input):
#     inputWords = input.split(" ")
#     inputWords = inputWords[-1::-1]
#     output = ' '.join(inputWords)
#     return output
#
# if __name__ == "__main__":
#     input = 'I like china'
#     rw = reverseWords(input)
#     print(rw)
# tup1 = ()
# tup2 = (20,)
# print(tup2[0])
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
#
# print(sites)   # 输出集合，重复的元素被自动去掉
#
# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')
#
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)     # a 和 b 的差集
#
# print(a | b)     # a 和 b 的并集
#
# print(a & b)     # a 和 b 的交集
#
# print(a ^ b)     # a 和 b 中不同时存在的元素
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2]     = "2 - 菜鸟工具"
#
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
#
#
# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值
# a = 5
# b = 5
# print(id(a))
# print(id(b))
# a += 1
# print(id(a))
# print(id(b))
# a = b
# print(id(a))
# print(id(b))
# import random
# print(random.choice(range(100)))
# print("我叫 %s 我是荣耀王者 %d 颗星!" % ('徐前磊', 50))
# print("我叫 {} 我是荣耀网址 {} 颗星".format("徐前磊", 50))
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# input("点击 enter 键退出")
# n = 100
# sum = 0
# num = 1
# while num <= n:
#     sum += num
#     num += 1
#
# print(sum)

# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行 pass 块')
#     print('当前字母 :', letter)
#
# print("Good bye!")

# import sys
# list=[1,2,3,4]
# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# import sys
#
# def yieldtest(n, w=0):
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a+b
#         print('%d, %d' % (a,b))
#         counter += 1
# f = yieldtest(10, 0)
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except:
#         sys.exit()
# sum = lambda a, b: a + b
# print(sum(10, 20))
# vec = [2, 4, 6]
# print([[x, x**2] for x in vec])
# import main, sys
# main.print_hi('hhh')
# print(sys.path)
# f = open("/Users/xql/Pyproject/study/text.txt", "r")
#
# str = f.readlines()
# print(str)
#f.write("今天又是美好的一天")
#f.close()

# import pickle
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1,2,3]
# selfref_list.append(selfref_list)
# output = open('/Users/xql/Pyproject/study/text.txt', 'wb')
#
# pickle.dump(data1, output)
#
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
#
# output.close()

# import pprint, pickle
#
# #使用pickle模块从文件中重构python对象
# pkl_file = open('/Users/xql/Pyproject/study/text.txt', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()
# from main import print_hi
# try:
#     print_hi("hhhh")
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行。')
# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
#
# # 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())

# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# s = student('ken', 10, 60, 3)
# s.speak()

# 类定义
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
#
# # 单继承示例
# class student(people):
#     grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# # 另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#
#     def __init__(self, n, t):
#         self.name = n
#         self.topic = t
#
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))
#
#
# # 多重继承
# class sample(speaker, student):
#     a = ''
#
#     def __init__(self, n, a, w, g, t):
#         student.__init__(self, n, a, w, g)
#         speaker.__init__(self, n, t)
#
#
# test = sample("Tim", 25, 80, 4, "Python")
# test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
# import re
# print(re.match('www', 'www.xuqianlei.com').span())
# print(re.match('www', 'www.xuqianlei.com'))
# line = "Cats are smarter than dogs"
# # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# # (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
#!/usr/bin/python3

# import _thread
# import time
#
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")
#
# while 1:
#    pass

# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")

# import threading
# import time
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# threadLock = threading.Lock()
# threads = []
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
#
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")
