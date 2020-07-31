#!/usr/bin/env python
# coding=utf-8

from method.domainList import DomainList
import platform
import subprocess
import json
from tqdm import tqdm
import time


class DomainStatus(object):
    """
    采用tcping检测出80端口通，443端口不通的域名
    """

    def __init__(self):
        with open('config/config.json', 'r') as f:
            config = json.loads(f.read())
        self.white_list = config.get('WhiteList')

    @staticmethod
    def win_sub_pop(domain):
        """
        :param domain: 域名
        :return: 返回True:80通，443通; 或80不通
                 返回False:80通，443不通
        """
        tc_ping = 'tools/tcping.exe'
        ret = subprocess.Popen([tc_ping, domain, '80'], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, encoding='utf8')
        ret_ssl = subprocess.Popen([tc_ping, domain, '443'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, encoding='utf8')
        if "Port is open" in ret.stdout.read():
            if "Port is open" in ret_ssl.stdout.read():
                return True
            else:
                return False
        else:
            return True

    @staticmethod
    def linux_sub_pop(domain):
        tc_ping = 'tools/tcping'
        ret = subprocess.Popen([tc_ping, '-t 5', domain, '80'], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, encoding='utf8')
        ret_ssl = subprocess.Popen([tc_ping, '-t 5', domain, '443'], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, encoding='utf8')
        if "port 80 open" in ret.stdout.read():
            if "port 443 open" in ret_ssl.stdout.read():
                return True
            else:
                return False
        else:
            return True

    def domain_status(self):
        """
        :return: 返回True和False计数
        """
        domain_list = DomainList().get_domain_list()
        sys = platform.system()
        count_true = 0
        count_false = 0
        res_message = ""
        print('开始检测...')
        # 采用tqdm方法迭代可以输出进度条
        # for domain in domain_list:
        for domain in tqdm(domain_list):
            if domain not in self.white_list:
                # print(domain)
                if sys == "Windows":
                    sp = DomainStatus.win_sub_pop(domain)
                    if sp:
                        count_true += 1
                    else:
                        message = '未配置https的域名：' + domain
                        res_message = res_message + message + '\n'
                        print(message)
                        count_false += 1

                if sys == "Linux":
                    sp = DomainStatus.linux_sub_pop(domain)
                    if sp:
                        count_true += 1
                    else:
                        message = '未配置https的域名：' + domain
                        res_message = res_message + message + '\n'
                        print(message)
                        count_false += 1
        time.sleep(2)
        print('白名单：' + ', '.join(self.white_list))
        print('正常数:' + str(count_true))
        print('异常数:' + str(count_false))
        print("检测完成")
        return {
            "count_false": count_false,
            "res_message": res_message
        }


if __name__ == '__main__':
    d = DomainStatus()
    d.domain_status()
