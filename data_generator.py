#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:53:46 2020

@author: sergio
"""

import random

def create_generators(n=2, length = 1000):
    output = []
    for _ in range(n):
        it_list = [random.random() for x in range(length)]
        gen = (x for x in it_list)
        output.append(gen)
    return output
    