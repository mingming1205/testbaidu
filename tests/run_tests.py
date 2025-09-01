#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
import time
import unittest
import yagmail
from XTestRunner import HTMLTestRunner

GLOBAL_CASEBASEPATH = 'D:/zheng/testcode/test_baidu_ui'
GLOBAL_CURRENT = time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))

start_dir = GLOBAL_CASEBASEPATH + '/tests/'
suite = unittest.defaultTestLoader.discover(start_dir,pattern='test_*.py',top_level_dir=None)

if __name__ == "__main__":
    html_report = GLOBAL_CASEBASEPATH +'/tests/test_report/' + GLOBAL_CURRENT + '_report.html'

    # unittest.TextTestRunner(verbosity=2).run(suite)

    with open(html_report, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='自动化测试报告',
                                description='融合服务平台-自动化测试结果',
                                Tester='枫叶',
                                language="zh-CN",
                                rerun=1
                                )
        runner.run(suite)

    # send_email(html_report)

