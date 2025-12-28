#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 21:10:25 2025

@author: dibyanshu
"""

import one

print("Top level in two.py")

one.func()

if __name__ == '__main__':
    print("two.py is being run directly")
else:
    print('one.py has been imported ')