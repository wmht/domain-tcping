#!/usr/bin/env python
# coding=utf-8

import json
import requests


class SendWeChat(object):
    """
    发送信息到企业微信
    """

    def __init__(self):
        with open('config/config.json', 'r') as f:
            config = json.loads(f.read())
        self.corp_id = config.get("CorpId", '')
        self.agent_id = config.get("AgentId", '')
        self.agent_secret = config.get("AgentSecret", '')
        self.to_user = config.get("ToUser", '')

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.corp_id,
                  'corpsecret': self.agent_secret,
                  }
        req = requests.post(url, params=values)
        return req

    def get_access_token(self):
        get_req = self._get_access_token()
        if get_req.status_code != 200:
            print('连接服务器失败')
        else:
            get_req_json = json.loads(get_req.text)
            if get_req_json['errcode'] != 0:
                print('响应结果不正确')
            else:
                access_token = get_req_json['access_token']
                return access_token

    def send_data(self, message):
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        send_values = {
            "touser": self.to_user,
            "msgtype": "text",
            "agentid": self.agent_id,
            "text": {
                "content": message
            },
            "safe": "0"
        }
        send_msges = (bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()
        return respone["errmsg"]


if __name__ == "__main__":
    wx = SendWeChat()
    wx.send_data("测试")


