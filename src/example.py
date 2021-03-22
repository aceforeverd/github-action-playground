#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class PlayGround(object):

    """Docstring for PlayGround. """

    def __init__(self, id, name):
        """TODO: to be defined.

        :Docstring for PlayGround.: TODO

        """

        self.id = id
        self.name = name

    def play(self):
        print('id: {}, name: {}', self.id, self.name)


if __name__ == '__main__':
    print('hello world')
