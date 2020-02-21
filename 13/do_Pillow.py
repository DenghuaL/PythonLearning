#!usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('test.jpg')

w, h = im.size
print('Origin image size: %s x %s' % (w,h))
print(im)

im.thumbnail((w//2, h//2))      #int divide, use // to get in result
print('Resize image to size: %s x %s' % (w//2, h//2))
print(im)
im.save('thumbnail.jpg', 'jpeg')
