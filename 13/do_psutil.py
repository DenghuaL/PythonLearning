#!usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil

print(psutil.cpu_count())

print(psutil.cpu_count(logical=False))