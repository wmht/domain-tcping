#!/usr/bin/env python
# coding=utf-8

import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest


class Record(object):
    """
    获取阿里云账户下指定域名的所有解析记录
    参考文档：https://help.aliyun.com/document_detail/29776.html?spm=a2c4g.11186623.3.3.5a543b59RyjdAD
    返回多个数组,每个域名对应一个数组：[{},{}] [{},{}]
    """

    def __init__(self):
        with open('config/config.json', 'r') as f:
            config = json.loads(f.read())
        self.access_key = config.get("AccessKey", '')
        self.secret = config.get("Secret", '')
        self.regionId = config.get("RegionId", '')
        self.PageNumber = config.get("PageNumber", '')
        self.PageSize = config.get("PageSize", '')
        self.Domains = config.get("Domains", '')

    def get_records(self):
        client = AcsClient(self.access_key, self.secret, self.regionId)
        request = DescribeDomainRecordsRequest()
        request.set_accept_format('json')
        request.set_PageNumber(self.PageNumber)
        request.set_PageSize(self.PageSize)

        responses = []
        for domain in self.Domains:
            request.set_DomainName(domain)
            response = client.do_action_with_exception(request)
            res = str(response, encoding='utf-8')
            responses.append(res)
        return responses
        # print(responses)


if __name__ == "__main__":
    r = Record()
    r.get_records()
