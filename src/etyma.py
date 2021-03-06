#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LostInNight
# @Date:   2015-11-05 12:06:55
# @Last Modified by:   LostInNight
# @Last Modified time: 2015-11-05 14:10:22


"""抓取词根与解释
http://etymonline.com/
"""

import requests, sys
from bs4 import BeautifulSoup


def query(etyma):
    url = r"http://etymonline.com/index.php?allowed_in_frame=0&search={0}&searchmode=none"
    url = url.format(etyma)
    return requests.get(url).text


def get_data(etymas):
    for etyma in etymas:
        html = query(etyma)
        soup = BeautifulSoup(html, "lxml")
        datas = soup.find_all(name=lambda x: x and "a" == x.name and not x.has_attr(
            "class"), text=lambda x: x and (etyma + " ") in x)
        for data in datas:
            word = data.string
            desc = "".join(data.find_next(name="dd").strings)
            print("单词：", word.encode('gbk', errors = 'ignore').decode('gbk'))
            print("释义：", desc.encode('gbk', errors = 'ignore').decode('gbk'), end="\n"*2)


if __name__ == '__main__':
    etymas = []
    if len(sys.argv) > 1:
        etymas.extend(sys.argv[1:len(sys.argv)])
    else:
        etymas = ["churn", "anti", "abs"]
        print("没有输入单词，下面演示查询：", "、".join(etymas), end = "\n"*2)
    get_data(etymas)

