# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    # filename='myapp.log',
    # filemode='w'
    )
