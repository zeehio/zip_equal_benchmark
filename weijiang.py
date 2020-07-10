#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:44:48 2020

@author: sergio
"""

import itertools

class _SentinelException(Exception):
    def __iter__(self):
        raise _SentinelException


def zip_equal(iterable1, iterable2):
    i1 = iter(itertools.chain(iterable1, _SentinelException()))
    i2 = iter(iterable2)
    try:
        while True:
            yield (next(i1), next(i2))
    except _SentinelException:  # i1 reaches end
        try:
            next(i2)  # check whether i2 reaches end
        except StopIteration:
            pass
        else:
            raise ValueError('the second iterable is longer than the first one')
    except StopIteration: # i2 reaches end, as next(i1) has already been called, i1's length is bigger than i2
        raise ValueError('the first iterable is longer the second one.')
    