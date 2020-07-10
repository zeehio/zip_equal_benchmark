#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:43:41 2020

@author: sergio
"""

import timeit
from statistics import median
from random import sample

def run_benchmark(n, length, to_benchmark):
    print("n = {}, length = {}".format(n, length))
    output = {}
    for b in sample(to_benchmark, len(to_benchmark)):
        setup = """
from data_generator import create_generators
from """ + b + """ import zip_equal
n = """ + str(n) + """
length = """ + str(length) + """
generators = create_generators(n, length)
"""
        out = timeit.repeat('list(zip_equal(*generators))', setup = setup, number = 1, repeat = 50)
        output[b] = out
    print("{:15s}: {:>8s}, {:>8s}, {:>8s}".format("method", "min", "median", "max"))
    for b in to_benchmark:
        print("{:15s}: {:8.4f}, {:8.4f}, {:8.4f}".format(b, min(output[b]), median(output[b]), max(output[b])))
    return output

TO_BENCH_FULL = ['pieters', 'cjerdonek', 'weijiang', 'pylang']
TO_BENCH = ['pieters', 'cjerdonek', 'pylang']

min_measurements = []
n = 2
for length in (10000, 100000, 1000000):
    out = run_benchmark(n = n, length = length, to_benchmark = TO_BENCH_FULL)
    for b in out:
        min_measurements.append((b, n, length, min(out[b])))

n = 10
for length in (10000, 100000, 1000000):
    out = run_benchmark(n = n, length = length, to_benchmark = TO_BENCH)
    for b in out:
        min_measurements.append((b, n, length, min(out[b])))

#import pickle
#min_measurements = pickle.loads(b"\x80\x03]q\x00((X\x08\x00\x00\x00weijiangq\x01K\x02M\x10'G?j\xb9\xa4H\x80\x00\x00tq\x02(X\x07\x00\x00\x00pietersq\x03K\x02M\x10'G?aS\xd5\xc8\xa0\x00\x00tq\x04(X\x06\x00\x00\x00pylangq\x05K\x02M\x10'G?d\x94\xfd\xdc\x00\x00\x00tq\x06(X\t\x00\x00\x00cjerdonekq\x07K\x02M\x10'G?Wn$\xe5\x80\x00\x00tq\x08(h\x07K\x02J\xa0\x86\x01\x00G?\x92\x86[\xd7\xc8\x00\x00tq\t(h\x03K\x02J\xa0\x86\x01\x00G?\x99\x9d\x80r\xc8\x00\x00tq\n(h\x01K\x02J\xa0\x86\x01\x00G?\xa2\xe8h\x9a\xdc\x00\x00tq\x0b(h\x05K\x02J\xa0\x86\x01\x00G?\x9d\xc22X\xdc\x00\x00tq\x0c(h\x03K\x02J@B\x0f\x00G?\xd0\xd2\xa9\x87\xc5\x80\x00tq\r(h\x07K\x02J@B\x0f\x00G?\xc8v'\xe0\xab\x00\x00tq\x0e(h\x05K\x02J@B\x0f\x00G?\xd3K-b0@\x00tq\x0f(h\x01K\x02J@B\x0f\x00G?\xd8\x08\xd9\xf7\xf2@\x00tq\x10(h\x07K\nM\x10'G?w\xbb\xd5G\x80\x00\x00tq\x11(h\x05K\nM\x10'G?\x81\xa5$g8\x00\x00tq\x12(h\x03K\nM\x10'G?~\xdah8@\x00\x00tq\x13(h\x05K\nJ\xa0\x86\x01\x00G?\xbc\x1c?\x84X\x00\x00tq\x14(h\x07K\nJ\xa0\x86\x01\x00G?\xb3\xf6\x18\x82z\x00\x00tq\x15(h\x03K\nJ\xa0\x86\x01\x00G?\xb8\x93\xfd\xd2\x98\x00\x00tq\x16(h\x03K\nJ@B\x0f\x00G?\xed\xe1\x84\xf7\x0f\x00\x00tq\x17(h\x07K\nJ@B\x0f\x00G?\xe8s\x82\n\xdc\xa0\x00tq\x18(h\x05K\nJ@B\x0f\x00G?\xf15\xfd\x04\xa3\x00\x00tq\x19e.")

(methods, ns, lengths, times) = list(zip(*min_measurements))

import pandas as pd
data = pd.DataFrame(min_measurements, columns=['method', 'n', 'length', 'time'])
import matplotlib.pyplot as plt
plt.plot(lengths,  times, 'bo')

data.plot(x = 'length', y = 'time', kind = 'scatter', c = 'method', logx = True, colormap = 'viridis')