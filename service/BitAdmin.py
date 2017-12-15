#/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = '8192bit'

class BitConfig(object):
    def __init__(self, model_class):
        self.model_class = model_class

class BitSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, model_class, bit_config_class=None):
        if not bit_config_class:
            bit_config_class = BitConfig
        self._registry[model_class] = bit_config_class(model_class)

