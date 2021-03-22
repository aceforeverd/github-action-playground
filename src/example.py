#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class HelloWorld(object):
    def __init__(self, id, name):
        self.idx = id
        self.namex = name
    def play(self):
        print('idx: {}, namex: {}', self.idx, self.namex)
if __name__ == '__main__':
    HelloWorld(1, '12')
    print('hello world')
