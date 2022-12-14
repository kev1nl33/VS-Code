from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
page_text = "file:///Users/kevinlee/Desktop/python学习/第二章/b.html"
tree = etree.parse(page_text, parser = parser)
result = tree.xpath("/html")
result = tree.xpath("/html/body/ul/li/a/text()")
result = tree.xpath("/html/body/ul/li[1]/a/text()") #xpath的顺序是从1开始数的，[]表示索引
result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()") #[@xxx=xxx]属性的筛选
# print(result)
ol_li_list = tree.xpath('/html/body/ol/li')

for li in ol_li_list:
    #从每个li中提取文字信息
    result = li.xpath('./a/text()') #在li中继续去寻找，相对查找  ./
    print(result)
    result2 = li.xpath('./a/@href') # 拿到属性值：@属性
    print(result2)

print(tree.xpath('/html/body/ul/li/a/@href'))

print(tree.xpath('/html/body/div[1]/text()'))
print(tree.xpath('/html/body/div[2]/text()'))