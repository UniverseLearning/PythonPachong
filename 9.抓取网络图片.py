# -*- coding:utf8 -*-
import requests
import re
from urllib import parse
import os


class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/flip?tn=baiduimage&word={}'
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsMiwxMyw3LDYsNSwxMiw5&word=python'
        self.headers = {'User-Agent': 'Mozilla/4.0'}

    # 获取图片
    def get_image(self, url, word):
        # 使用 requests模块得到响应对象
        res = requests.get(url, headers=self.headers)
        # 更改编码格式
        res.encoding = "utf-8"
        # 得到html网页
        html = res.text
        print(html)
        # 正则解析
        pattern = re.compile('"hoverURL":"(.*?)"', re.S)
        img_link_list = pattern.findall(html)
        # 存储图片的url链接
        print(img_link_list)

        # 创建目录，用于保存图片
        directory = 'C:/Users/Administrator/Desktop/image/{}/'.format(word)
        # 如果目录不存在则创建，此方法常用
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 添加计数
        i = 1
        for img_link in img_link_list:
            filename = '{}{}_{}.jpg'.format(directory, word, i)
            self.save_image(img_link, filename)
            i += 1

    # 下载图片
    def save_image(self, img_link, filename):
        html = requests.get(url=img_link, headers=self.headers).content
        with open(filename, 'wb') as f:
            f.write(html)
        print(filename, '下载成功')

    # 入口函数
    def run(self):
        word = input("您想要谁的照片？")
        word_parse = parse.quote(word)
        url = self.url.format(word_parse)
        self.get_image(url, word)


if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()