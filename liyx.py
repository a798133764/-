# a="hello_world"
# print(a)
#
# # 列表
# l = [1,2,3,4,3]
# l[0]=10
# print(l)
#
# #元祖
# t=(1,2,3,4,5,2)
# print(t)
#
# #集合
# s = {1,2,3,4,1,2,3,4}
# print(s)
#
# #字典
# # dict{"name":"李亚新","age":18}    #key不可修改，key不可重复，无序
# d={"name":"tian","age":"18"}
# print(d["name"])
#
#
# a=10
# b="20"
# print(a + int(b)) #字符串转整数
# print(str(a) + b) #整数转字符串
#
# a=10
# b="2.9"
# print(a +float(b)) #字符串转小数
# print(str(a) +b)  #整数转字符串
#
# a=True # 布尔类型也是数字 True 1 False 0
# b=29
# print(a + b)
#
# l = [1,2,3,4,5,6]
# print(tuple(l))  #list转tuple
# print(set(l))  #list 转 set
#
# t = (1,2,3,4,5)
# print(list(t)) #tuple转list
# print(set(t))  #tuple转set
#
#
# print(list(s))   #set转list
# print (tuple(s))  # set转tuple
# '''
# 成员运算符
# in
# not in
# '''
#
# a = "ahelog"
# l = ["a","4","g"]
# t = ("a","4","g")
# s = {"a","4","g"}
# d = {"name":"王大锤","sex":"女"}
#
# print("a" in a)
# print("a" in l)
# print("a" in t)
# print("a" in s)
# print("name"in d)
#
# money = 500000000
#
# if (money < 5000000):
#     print("买两个辣条")
#     print("吃一个，扔一个")
#
# elif(money < 10000000):
#     print("来根华子")
#
# elif(money < 100000000):
#     print("自己做华子")
#
# else:
#     print("把中国烟草买了")
#
# #循环
# for i in [1,2,3,4,5,6]:
#     print(i)
#     print("重要的事情说100遍！")
#
# for i in range(100):
#     print("理解！")
#
# print(list(range(12,5,-3)))
# print(list(range(121,2,-3)))
# print(list(range(121,12,-3)))
#
# # while 循环
#
# i = 1
# while(i < 10):
#     print(i)
#     i += 1
#
# #continue , pass  跳过  break 结束循环
# for i in range (1,11):
#     if (i == 7):
#         continue
#     print(i)
#
#     for i in range(1, 11):
#         if (i == 7 or i ==8):
#             pass
#         else:
#           print(i)
#
#
# for m in range(1,10):
#
#     for n in range(1,10):
#
#         print('%s×%s=%s'%(m,n,m*n),end=' ')
#
#         if n>m:
#
#             break
#
#     print()

# def select_data(sql):
#     res = "查询结果"
#     return res
#
# led = select_data("")
# print(led);

# def div(a,b):
#     if b == 0:
#         print("被除数不能为0")
#     else:
#         print(a/b)
#
# div(10,20)
# div(40,10)
# div(60,130)

# def s(a,b):
#     return a+b
# print(s(1,2))
#
# def s(a=3,b=7):
#     return a+b
# print(s(1))
#
# print(s(1,2))
#
# print(s(b=20))
#
# def ss (a,*s,b=20,**d):
#     print(s)
#     print(d)
# ss(1,2,3,4,5,6,s=8,d=9)

# #操作文件
# f = open ("a.txt",'w') #以写入的形式打开文件
# f.write("hef.llo") #写入数据
# f.close() # 关闭文件
#
# f = open("a.txt",'r')
# res = f.read()
# print(res)
# f.close()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,'=',i*j,end='\t')
#     print()
#
# c = 200
#
# def liyx():
#     c = 20
#     print(c)
# liyx ()
# print(c)

# def liyx():
#     global c     #global可以在局部作用域中声明变量为全局变量
#     c = 20
# liyx()
# print(c)

#字符串
# a = "1234567890"
# b = "456"
# print(a+b)  #拼接
# print(a*3)   #复制3份
# print(a[0])  #根据下标获取单个字符
# print(a[2:6]) #截取3-6的字符
# print(a[:6]) #截取1-6的字符
# print(a[-2:]) #截取倒数第2到最后一个字符
# print(a[0:-1]) #截取第一个到倒数第二个字符
#
# a = "asfdamfnsaklfmnlkasf"  #字符串
# a = a.strip()
# print(a.strip())      #去空格
# print(a.lstrip())   #去左空格  l = 左
# print(a.rstrip())   #去右空格  r = 右
# ss = "年龄，大小，性别"
# ss = ss.replace(",",",")  #替换
# print(ss)    #打印出字符串
# print(ss.split(','))    #切片打印
# print(ss.find("预期"))  #find查找

# #format 格式化字符串，%s格式化字符串，%d格式化数字
# for i in range(1,10):
#     for j in range (1,i+1):
#         print("{} X {} = {}".format(j,i,j*i),end='\t')
#     print()
#
# print("我是:%s,今年%d岁了"%("李亚新",888))

#列表
# l = [1,2,3,4,5,6,7,8,9,0]
#
# l[0]=20
# print(l)   #根据下标修改列表元素的值
# l.append(9)  # append 在列表末尾加值
# l.insert(2,30) # insert 在特定位置加值 光标第2位
# l.extend((1,2,3,4,5,)) # extend 在列表末尾添加多个数据
# l.pop() # pop 删除列表最后一个元素
# l.pop(1) #根据下标删除数据
# l.remove(2) # remove 根据内容删除第一个数据
# print(l.index(6))  #查询某个元素的下标，如果多个值只查询第一个
# l.sort()  # sort 排序  默认升序，会修改表的数据
# l.sort(reverse=True) #  reverse=True    降序

# #集合
# s =set()   显示集合

# #字典
# d = {"name":"小明","age":"20"}
#
# print(d["name"])  #查询字典值
# d["name"] = "小红" #修改value
# d["sex"] = "女" #因为sex在字段不存在，所以新增
# d.pop("sex") #删除字典中的数据
#
# d2 = {"sex":"女"}
# d.update(d2) #update 合并两个字典，数据重复取新
# print(dict(d,addr="黑龙江",phone="15645277577"))  #dict 创建一个新的字典

# #面向对象编程
# def s(a,b):
#     return a+b
# print(s(10,20))
#
# #对变量和方法的打包
# def open():
#     print("操作文件")
#     pass

# f = open("a.txt,","r")
# res = f.read()
# f.close()

# 对变量和方法的打包

# 类和对象
# 创建一个类
# class str_demo ():
#     s = None
#     def say(self):
#         print("字符串替换")
#     def split (self):
#         print("字符串切割")
# sd = str_demo() # 实例化 sd就是一个对象
# sd.s = "hello"
# sd.say()
# sd.split()
#
# class sss():
#     _a = None
#     def set_a(self,value):
#         self._a = value
#     def get_a(self):
#         return self._a
# p = sss()
# p.set_a ("hello")
# print(p.get_a())
# # print(p.get_a)
# import random
# l = s = random.choices("1",k=1)
# s = random.choices("0123456789",k=10)
# print("".join(l))
# print("".join(s))
# j = (l + s)
# print(j)
# print("".join(j))
try:
    r = open("333.py","r")
except (FileNotFoundError,ZeroDivisionError) as d:
    print("错")
    print("重来")
    print("对")
else:
    print("没错")
finally:
    print("不管程序")






