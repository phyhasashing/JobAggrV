# -*- encoding = utf-8 -*-
import csv
import requests
import random

import time
from lxml import etree

class xpath(object):
    # 初始化url
    def __init__(self):
        self.url = "https://www.python.org/jobs/?page={}"
        self.blog = 1

    def get_heml(self, url):
        url = 'https://www.python.org/jobs/'
        self.blog += 1
        headers = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',

            }
        response = requests.get(url, headers=headers).content.decode('utf-8')#请求头
        p = etree.HTML(response)#转码
        a_list = p.xpath('//*[@id="content"]/div/section/div/ol/li')#提出列表
        items = {}
        for a in a_list:
            JobTitle = a.xpath('.//*[@class="listing-company-name"]/a/text()')[0]#提取Jobtitle
            if JobTitle:#判断是否空值
                items["JobTitle"] = JobTitle
            else:
                items["JobTitle"] = None
            DetailUrl = 'https://www.python.org' + a.xpath('.//*[@class="listing-company-name"]//@href')[0]#DetailUrl详情页面URL，进行下一步URL的使用
            if DetailUrl:#判断空值
                items["DetailUrl"] = DetailUrl
            else:
                items["DetailUrl"] = None
            detail_page_text = requests.get(url=DetailUrl, headers=headers).content.decode('utf-8')#读取详情页面
            detail_tree = etree.HTML(detail_page_text)#详情页面转码
            FromWhere = detail_tree.xpath(('//*[@id="content"]/div/section/article/div/ul/li[3]/a/text()'))#提取详情页面的FromWhere
            if FromWhere:#判断空值
                items["FromWhere"] = FromWhere
            else:
                items["FromWhere"] = None
            Company = detail_tree.xpath('normalize-space(.//*[@id="content"]/div/section/article/h1/span[1]/span/text()[3])')#提取详情页面的 Company
            if Company:#判断空值
                items["Company"] = Company
            else:
                items["Company"] = None
            PostDate = a.xpath('//*[@class="listing-posted"]/time/text()')[0]#提取PostData
            if PostDate:#判断空值
                items["PostDate"] = PostDate
            else:
                items["PostDate"] = None
            Location = a.xpath('.//*[@class="listing-location"]/a/text()')[0]#提取Location
            if Location:#判断空值
                items["Location"] = Location
            else:
                items["Location"] = None
            CrawledTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))#读取本地时间
            if CrawledTime:#判断空值
                items["CrawledTime"] = CrawledTime
            else:
                items["CrawledTime"] = None
            time.sleep(random.randint(0,1))#设置随机延迟
            with open('python.org.csv', 'a',newline='') as fp:#读入数据（追加）
                csv_writer = csv.writer(fp)
                csv_writer.writerow([JobTitle, DetailUrl, Company, FromWhere, PostDate, Location, CrawledTime])

    def run(self):
        # 页的信息，默认100
        for pg in range(1,100):
            # 将页码数嵌入url中
            url = self.url.format(pg)
            # 调用主方法
            self.get_heml(url)
            # 设置间隔，休眠0或1秒，目的是反爬
            time.sleep(random.randint(0, 1))
            self.blog = 1

if __name__ == "__main__":
    spider = xpath()
    spider.run()#启动
