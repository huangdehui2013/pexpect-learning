#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
author:hdh
description: execute remote commands by pexpect
date:2015-04-29
"""
import sys 
import pexpect
password = 'password'
expect_list = ['(yes/no)', 'password:']

p = pexpect.spawn('ssh username@localhost ls')
try:
    while True:
        idx = p.expect(expect_list)
        print p.before + expect_list[idx],
        if idx == 0:
            print "yes"
            p.sendline('yes')
        elif idx == 1:
            print password
            p.sendline(password)
except pexpect.TIMEOUT:
    print >>sys.stderr, 'timeout'
except pexpect.EOF:
    print p.before
    print >>sys.stderr, '<the end>'
