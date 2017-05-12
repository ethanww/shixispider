#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy import cmdline

name = 'shixi'  # spider的name
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
