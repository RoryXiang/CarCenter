#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-27 14:36:20
# @Author  : RoryXiang (pingping19901121@gmail.com)
# @Link    : ${link}
# @Version : $Id$

from logging import handlers, getLogger
import os
import yaml
import logging.config
from conf import LOG_DIR, DIR_PATH

LOG_CONF_PATH = os.path.join(DIR_PATH, "logging.yaml")


def setup_logging():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    with open(LOG_CONF_PATH, "rt") as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    logging.config.dictConfig(config)


def add_logger_handler(logger, file_name):
    level = logging.INFO
    new_formatter = logging.Formatter(
        '%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s: %(message)s')
    file_name = file_name + ".log"
    file_name = LOG_DIR + file_name
    th = handlers.TimedRotatingFileHandler(filename=file_name,
                                           when='D',
                                           backupCount=14,
                                           interval=1,
                                           encoding='utf-8')
    # 防止给同一个logger添加重复的handler
    for handler in logger.handlers:
        if getattr(handler, "baseFilename", None) == th.baseFilename:
            return
    th.setFormatter(new_formatter)
    th.setLevel(logging.INFO)
    logger.addHandler(th)
    logger.setLevel(level)
