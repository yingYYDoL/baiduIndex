from urllib.parse import urlencode
import queue
import math
import datetime
import random
import time
import json

import requests
import random

from config import COOKIES, PROVINCE_CODE, CITY_CODE
import utils


headers = {
    'Host': 'index.baidu.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
}


class BaiduIndex:
    """
        百度搜索指数
        :keywords; list
        :start_date; string '2018-10-02'
        :end_date; string '2018-10-02'
        :area; int, search by cls.province_code/cls.city_code
    """

    province_code = PROVINCE_CODE
    city_code = CITY_CODE
    #_all_kind = ['all', 'pc', 'wise']
    _all_kind = ['all']
    _params_queue = queue.Queue()
    cookies = COOKIES[0]

    def __init__(self, keywords: list, start_date: str, end_date: str, area=0):
        self.keywords = keywords
        self._area = area
        self._init_queue(start_date, end_date, keywords)


    def get_index(self,begin_date):
        """
        获取百度指数
        返回的数据格式为:
        {
            'keyword': '武林外传',
            'type': 'wise',
            'date': '2019-04-30',
            'index': '202'
        }
        """
        while 1:
            try:
                params_data = self._params_queue.get(timeout=1)
                encrypt_datas, uniqid = self._get_encrypt_datas(
                    start_date=params_data['start_date'],
                    end_date=params_data['end_date'],
                    keywords=params_data['keywords']
                )
                key = utils.get_key(uniqid, self.cookies)
                # for encrypt_data in encrypt_datas:
                #     for kind in self._all_kind:
                #         encrypt_data[kind]['data'] = utils.decrypt_func(
                #                 key, encrypt_data[kind]['data'])
                #     for formated_data in self._format_data(encrypt_data):
                #         yield formated_data
                for encrypt_data in encrypt_datas:
                    for kind in self._all_kind:
                        encrypt_data[kind]['data'] = utils.decrypt_func(
                                key, encrypt_data[kind]['data'])
                    for formated_data in self._format_data(encrypt_data):
                        return   [formated_data['index']]
                #formated_data = encrypt_datas
                #return formated_data
                #yield formated_data

            except requests.Timeout:
                self._params_queue.put(params_data)
            except queue.Empty:
                break
            self._sleep_func()

    def _init_queue(self, start_date, end_date, keywords):
        """
            初始化参数队列
        """
        keywords_list = self._split_keywords(keywords)
        time_range_list = self._get_time_range_list(start_date, end_date)
        for start_date, end_date in time_range_list:
            for keywords in keywords_list:
                params = {
                    'keywords': keywords,
                    'start_date': start_date,
                    'end_date': end_date
                }
                self._params_queue.put(params)

    def _split_keywords(self, keywords: list) -> [list]:
        """
        一个请求最多传入5个关键词, 所以需要对关键词进行切分
        """
        return [keywords[i*5: (i+1)*5] for i in range(math.ceil(len(keywords)/5))]

    def _get_encrypt_datas(self, start_date, end_date, keywords):
        """
        :start_date; str, 2018-10-01
        :end_date; str, 2018-10-01
        :keyword; list, ['1', '2', '3']
        """
        # request_args = {
        #     'word': ','.join(keywords),
        #     'startDate': start_date.strftime('%Y-%m-%d'),
        #     'endDate': end_date.strftime('%Y-%m-%d'),
        #     'area': self._area,
        #     #'area': area,
        # }
        #
        # url = 'http://index.baidu.com/api/SearchApi/index?' + urlencode(request_args)
        # time.sleep(0.1)
        # html = self._http_get(url)
        # datas = json.loads(html)
        # #print(json.dumps(datas,indent=2))
        # uniqid = datas['data']['uniqid']
        # #print(datas['data']['generalRatio'][0]['all']['avg'])#need!
        # '''encrypt_datas = []
        # for single_data in datas['data']['userIndexes']:
        #     encrypt_datas.append(single_data)
        # return (encrypt_datas, uniqid)'''
        # encrypt_datas = []
        # encrypt_datas.append(datas['data']['generalRatio'][0]['all']['avg'])
        # return (encrypt_datas, uniqid)
        word_list = [
            [{'name': keyword, 'wordType': 1} for keyword in keyword_list]
            for keyword_list in keywords
        ]
        request_args = {
            'word': json.dumps(word_list),
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d'),
            'area': self._area,
        }
        url = 'http://index.baidu.com/api/SearchApi/index?' + urlencode(request_args)
        html = utils.http_get(url, self.cookies)
        datas = json.loads(html)
        uniqid = datas['data']['uniqid']
        encrypt_datas = []
        for single_data in datas['data']['userIndexes']:
            encrypt_datas.append(single_data)
        return (encrypt_datas, uniqid)

    def _get_key(self, uniqid):
        """
        """
        url = 'http://index.baidu.com/Interface/api/ptbk?uniqid=%s' % uniqid
        html = self._http_get(url)
        datas = json.loads(html)
        key = datas['data']
        return key

    '''def _format_data(self, data):
        """
            格式化堆在一起的数据
        """
        keyword = str(data['word'])
        time_length = len(data['all']['data'])
        start_date = data['all']['startDate']
        cur_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        for i in range(time_length):
            for kind in self._all_kind:
                index_datas = data[kind]['data']
                index_data = index_datas[i] if len(index_datas) != 1 else index_datas[0]
                formated_data = {
                    'keyword': keyword,
                    'type': kind,
                    'date': cur_date.strftime('%Y-%m-%d'),
                    'index': index_data if index_data else '0'
                }
                yield formated_data
            cur_date += datetime.timedelta(days=1)'''


    def _http_get(self, url, cookies=COOKIES):
        """
            发送get请求, 程序中所有的get都是调这个方法
            如果想使用多cookies抓取, 和请求重试功能
            在这自己添加
        """
        i = random.randint(0,len(cookies)-1)
        #headers['user-agent']= "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"#可有可无
        headers['Cookie'] = cookies[i]
        proxy_list = [
            {"https": "http://127.0.0.11:1080"},
            {"https":"http://223.198.128.105:1080"},
            {"https": "http://124.93.201.59:8888"}
        ]
        proxy = random.choice(proxy_list)  # 随机选择一个ip地址
        response = requests.get(url, headers=headers,proxies=proxy, timeout=5)
        #response = requests.get(url, headers=headers,timeout=5)
        if response.status_code != 200:
            raise requests.Timeout
        return response.text




    def _get_time_range_list(self, startdate, enddate):
        """
            切分时间段
        """
        date_range_list = []
        startdate = datetime.datetime.strptime(startdate, '%Y-%m-%d')
        enddate = datetime.datetime.strptime(enddate, '%Y-%m-%d')
        '''while 1:
            #tempdate = startdate + datetime.timedelta(days=300)
            tempdate = startdate + datetime.timedelta(days=365)
            if tempdate > enddate:
                date_range_list.append((startdate, enddate))
                break
            date_range_list.append((startdate, tempdate))
            startdate = tempdate + datetime.timedelta(days=1)'''
        date_range_list.append((startdate, enddate))
        return date_range_list

    def _decrypt_func(self, key, data):
        """
            数据解密方法
        """
        a = key
        i = data
        n = {}
        s = []
        for o in range(len(a)//2):
            n[a[o]] = a[len(a)//2 + o]
        for r in range(len(data)):
            s.append(n[i[r]])
        return ''.join(s).split(',')

    def _sleep_func(self):
        """
            sleep方法, 单账号抓取过快, 一段时间内请求会失败
        """
        sleep_time = random.choice(range(50, 90)) * 0.1
        time.sleep(sleep_time)

    def _format_data(self, data):
        """
            格式化堆在一起的数据
        """
        keyword = str(data['word'])
        start_date = datetime.datetime.strptime(data['all']['startDate'], '%Y-%m-%d')
        end_date = datetime.datetime.strptime(data['all']['endDate'], '%Y-%m-%d')
        date_list = []
        while start_date <= end_date:
            date_list.append(start_date)
            start_date += datetime.timedelta(days=1)

        for kind in self._all_kind:
            index_datas = data[kind]['data']
            for i, cur_date in enumerate(date_list):
                try:
                    index_data = index_datas[i]
                except IndexError:
                    index_data = ''
                formated_data = {
                    'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))],
                    'type': kind,
                    'date': cur_date.strftime('%Y-%m-%d'),
                    'index': index_data if index_data else '0'
                }
                yield formated_data
