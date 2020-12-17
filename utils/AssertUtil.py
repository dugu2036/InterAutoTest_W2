# -*- coding: utf-8 -*-
# @Time : 2020/11/18 19:56
# @File : AssertUtil.py
# @Author : Yvon_₯㎕ζ๓

import json
from utils.LogUtil import my_log


#1、定义封装类
class AssertUtil:
#2、初始化数据、日志
    def __init__(self):
        self.log = my_log("AssertUtil")
#3、code相等
    def assert_code(self,code,expected_code):
        """
        验证返回状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is %s,expected_code is %s"%(code,expected_code))
            raise

#4、body相等
    def assert_body(self, body, expected_body):
        """
        验证返回结果内容相等
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body error,body is %s,expected_body is %s" % (body, expected_body))
            raise

#5、body包含
    def assert_in_body(self, body, expected_body):
        """
        验证返回结果包含期望结果
        :param body:
        :param expected_in_body:
        :return:
        """
        try:
            body = json.dumps(body)
            print(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者body是错误,body is %s,expected_body is %s" % (body, expected_body))
            raise