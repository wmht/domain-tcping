#!/usr/bin/env python
# coding=utf-8

from method.dnsRecords import Record
import json


class DomainList(object):
    """
    获取域名地址
    """
    @staticmethod
    def get_record_list():
        # 合并所有域名的解析，并输出为数组格式：[{},{}, ...]
        record_lists = Record().get_records()
        re_list = []
        for records in record_lists:
            records_json = json.loads(records)['DomainRecords']['Record']
            re_list = re_list + records_json
        return re_list

    def get_domain_list(self):
        # 当Status为ENABLE,返回域名地址: ['','', ...]
        record = self.get_record_list()
        domain_list = []
        for re in record:
            re_status = re.get('Status')
            re_rr = re.get('RR')
            re_white = ['@', 'pop3', 'smtp', 'mail']
            if re_status == 'ENABLE' and re_rr not in re_white:
                domain = re.get('RR') + '.' + re.get('DomainName')
                domain_list.append(domain)
        return domain_list
        # print(domain_list)


if __name__ == '__main__':
    r = DomainList()
    r.get_domain_list()

