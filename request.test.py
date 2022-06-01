# -*- encoding = utf-8 -*-
import requests
from lxml import etree
import time
import random

class xpath(object):
    # 初始化url
    def __init__(self):
        self.url = "https://www.python.org/jobs//page{}"
        self.blog = 1

    def get_heml(self, url):
        url = 'https://www.python.org/jobs/'
        self.blog += 1
        hearders = {
            'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36',

            }
        response = requests.get(url, headers=hearders)
        p = etree.HTML(response.text)
        lists = p.xpath('//*[@class="row"]')

        items = {}
        for i in range(1, 21):
            for li in lists:
                DetailUrl = li.xpath('//*[@class="listing-company-name"]//a/@href')
                # 判断空值
                if DetailUrl:
                    items["DetailUrl"] = DetailUrl[i]
                else:
                    items["DetailUrl"] = None

                JobTitle = li.xpath('//*[@class="listing-company-name"]/a/text()')
                if JobTitle:
                    items["JobTitle"] = JobTitle[i]
                else:
                    items["JobTitle"] = None

                Company = li.xpath('//*[@class="listing-company-name"]/text()')
                print(type(Company))
                if Company:
                    items["Company"] = Company[i]
                else:
                    items["Company"] = None

                PostDate = li.xpath('//*[@class="listing-posted"]/time/text()')
                if PostDate:
                    items["PostDate"] = PostDate[i]
                else:
                    items["PostDate"] = None

                Location = li.xpath('//*[@class="listing-location"]/a/text()')
                if Location:
                    items["Location"] = Location[i]
                else:
                    items["Location"] = None
                # FromWhere = li.xpath('')
                CrawledTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                if CrawledTime:
                    items["CrawledTime"] = CrawledTime
                else:
                    items["CrawledTime"] = None

            with open('python.org.csv', 'a', encoding='utf-8') as fp:
                fp.write(str(items))
                fp.close()
                print(items)
                print("保存成功")
    def run(self):
        # 页的信息
        for pg in range(1, 2):
            # 将页码数嵌入url中
            url = self.url.format(pg)
            # 调用主方法
            self.get_heml(url)
            # 设置间隔，休眠0或1秒，目的是反爬
            time.sleep(random.randint(0, 1))
            self.blog = 1


if __name__ == "__main__":
    spider = xpath()
    spider.run()
print('完毕！')