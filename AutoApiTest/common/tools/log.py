#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging

def get_log():

    format_log = "%(asctime)s-%(levelname)s-%(message)s"
    logging.basicConfig(filename="my.log", level=logging.INFO, format=format_log)
    return logging


