#!/usr/bin/env python
# coding=utf-8

from method.domainStatus import DomainStatus
from method.sendWechat import SendWeChat


def main():
    """
    当存在异常的域名，则发送企业微信通知
    """

    domain_status = DomainStatus().domain_status()
    count_false = domain_status.get("count_false")
    res_message = domain_status.get("res_message")
    if count_false > 0:
        swc = SendWeChat()
        print('发送结果到企业微信')
        if swc.send_data(res_message):
            print("发送成功")
        else:
            print("发送失败")
    else:
        print("没有异常域名")


if __name__ == '__main__':
    main()
