# -- help 查看帮助信息
scrapy -- help
 
 
# version 查看版本信息
scrapy version
 
 
# version -v 更加全面的版本信息
scrapy version -v
 
 
# startproject 创建工程
scrapy startproject tutorial(工程名称)
 
 
cd tutorial
 
 
# 以下方法在 tutorial 目录下进行
 
 
# genspider 建立爬虫文件（创建文件在 tutorial/spider 目录下）
# 创建的时候要注意不同的spider文件的name必须不同
scrapy genspider 爬虫的名称 爬取的网站
 
 
# crawl 运行爬虫
scrapy crawl 爬虫的名称 
scrapy crawl 爬虫的名称 -o 保存的文件名
 
 
# list 本工程中查看所有爬虫
scrapy list
 
 
# view 查看页面源码在浏览器中显示的样子
# 执行下面语句会在浏览器中查看该网页
scrapy view http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
 
 
# parse 在工程中使用固定的parse函数解析某个页面，可以用来查看parse函数写的是否正确
# （此命令执行错误，还没找到原因，但是爬虫运行都正常）
scrapy parse http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
 
 
# shell 可用于调试数据，检测xpath，查看页面源码等等
cd ..（跳出tutorial目录）
scrapy shell http://www.dmoz.org/Computers/Programming/Languages/Python/Books/
# 获取当前路径下书籍的总数量
In [1]: response.xpath('//*[@id="site-list-header"]/span[2]')
Out[1]: [<Selector xpath='//*[@id="site-list-header"]/span[2]' data=u'<span clas
s="header-count node-count">18'>]
 
 
In [2]: response.xpath('//*[@id="site-list-header"]/span[2]').extract()
Out[2]: [u'<span class="header-count node-count">18</span>']
 
 
In [6]: response.xpath('//*[@id="site-list-header"]/span[2]/text()').extract()
Out[6]: [u'18']
 
 
In [7]: response.xpath('//*[@id="site-list-header"]/span[2]/text()').re(r'\d+')
...:
Out[7]: [u'18']
 
 
In [8]: response.xpath('//*[@id="site-list-header"]/span[2]/text()').re(r'\d+')
...: [0]
Out[8]: u'18'
 
 
In [9]: response.xpath('//*[@id="site-list-header"]/span[2]/text()').re(r'\d+')
...: [0]
Out[9]: u'18'
 
 
# runspider 运行单独的一个爬虫，也可以完成爬取，不需要使用框架
# dmoz_spider.py 文件放在一个单独的文件夹，比如桌面
scrapy runspider dmoz_spider.py
 
 
# bench 运行一个基准测试，用来查看是否安装好
scrapy bench