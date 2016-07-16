# -*- coding: utf-8 -*-


import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class RotateUserAgentMiddleware(UserAgentMiddleware):

    otherheaders ={
                'Accept-Encoding':'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Cache-Control': 'max-age=0',
                'Cookie': 'MUID=127B5A91B46861293E9E522AB06862D0; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=929FF2CB92714BCA92883F1896301926; SRCHUSR=DOB=20160419; MUIDB=127B5A91B46861293E9E522AB06862D0; _RwBf=s=70&o=16; _BINGNEWS=SW=1262&MSW=1776; _EDGE_S=SID=0338C0293430645E170CC97D359165CC; _ITAB=STAB=TR; SCRHDN=ASD=0&DURL=#; RMS=A=gUACEEAAIAAQ; _SS=SID=0338C0293430645E170CC97D359165CC&HV=1468684535&bIm=913956; WLS=TS=63604281335; SRCHHPGUSR=CW=1262&CH=810&DPR=2',
                }

    def __init__(self, user_agent=''):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'

    def process_request(self, request, spider):
        if request.url[-3:].lower() != 'jpg':
            for k, v in self. otherheaders.items():
                request.headers.setdefault(k,v)
