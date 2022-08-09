import re


# # findall: 匹配字符串中所有符合正则的内容

# list = re.findall(r'\d+',"我的电话号码是:10086，我女朋友的电话是10010")
# print(list)


# #finditer: 匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿到内容需要使用.group()]

# it = re.finditer(r'\d+',"我的电话号码是:10086，我女朋友的电话是10010")

# for i in it:

#     print(i.group())


# #search，找到一个结果就返回，返回的是match对象，拿数据需要.group()

# s = re.search(r'\d+',"我的电话号码是:10086，我女朋友的电话是10010")

# print(s.group())



# #match是从头开始匹配

# s = re.match(r'\d+',"我的电话号码是:10086，我女朋友的电话是10010")

# print(s.group())


#预加载正则表达式

# obj = re.compile(r'\d+')

# jls_extract_var = '我的电话号码是:10086，我女朋友的电话是10010'
# ret = obj.finditer(jls_extract_var)
# for it in ret:
#     print(it.group())

# rac = obj.search(jls_extract_var)
# print(rac.group())


#(?P<分组名字>正则) 可以单独从正则匹配的内容中提取进一步内容
s = """
<div class='jay'><span id = '1'>郭麒麟</span></div>
<div class='jj'><span id = '2'>宋轶</span></div>
<div class='kevin'><span id = '3'>大聪明</span></div>
<div class='zeo'><span id = '4'>范思哲</span></div>
<div class='roy'><span id = '5'>乱七八糟</span></div>
"""

obj = re.compile(r"<div class='(?P<wahaha>.*?)'><span id = '(?P<qiongchacha>\d+)'>(?P<hahaha>.*?)</span></div>", re.S) #re.S:让.能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("wahaha"))
    print(it.group("qiongchacha"))
    print(it.group("hahaha"))
