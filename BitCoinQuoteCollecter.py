#!/usr/bin/python
# coding=utf-8
import json
import pycurl
import urllib,urllib2
import httplib

class BitCoinQuoteCollecter(object):
    trade_platform_list = ["coinbasebtcusd", "bitfinexbtcusd", "bitstampbtcusd", "bitfinexltcusd",
                           "okcoinbtcusdfuture", "okcoinbtcusd", "okcoinltcusdfuture", "okcoinltcusd"]
    url_head = "https://www.btc123.com/api/getTicker?symbol="
    url_list = []
    for l in trade_platform_list:
        url_list.append(url_head + l)

    url = "https://baike.baidu.com/"

    conn = httplib.HTTPConnection("113.107.238.215")
    conn.request(method="GET", url=url)

    response = conn.getresponse()
    res = response.read()
    print res
