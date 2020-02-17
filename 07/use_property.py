#!usr/bin/env python3
#--*-- coding: utf-8 --*--

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('width must be a value > 0')
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if value > 0:
            self._height = value
        else:
            raise ValueError('heigt must be a value > 0')

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()

s.width = 1024
s.height = 768
print('resolution = ', s.resolution)

    