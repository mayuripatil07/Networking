# -*- coding: utf-8 -*-
import collections
import itertools
import datetime as dt
import re
with open('/Users/mayuripatil/Desktop/dnslog.txt', 'r') as f:
    s = f.read()
    domain = []
    domainRegex = re.compile(r'''
    ([0-9a-z-]+
    \.
    [a-z-]+
    \.?
    [a-z-]+
    \.?
    [a-z-]+
    \.?
    \s
    [A-Z]+)



    ''', re.VERBOSE)
    domain = domainRegex.findall(s)


line_regex = re.compile(r'''
(([0-9][0-9][0-9][0-9])-([0-9]?[0-9])-([0-9]?[0-9]) \s (0?0|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9]).(([0-9][0-9])?[0-9]))
''', re.VERBOSE)
time = []

with open("/Users/mayuripatil/Desktop/dnslog.txt", "r") as in_file:
    s = in_file.read()

    Ex = line_regex.findall(s)

    for ex in Ex:
        time.append(ex[0])


dictionary = collections.OrderedDict(itertools.izip(time, domain))
v_list = []
t_list = []

t = dictionary.keys()

v = dictionary.values()

i = 0

while i < len(t):
    a = len(v_list)
    b = len(t_list)
    start = t[0]
    end = t[i]
    start_dt = dt.datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
    end_dt = dt.datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
    diff = (end_dt - start_dt)

    if diff.seconds < 60:

        v_list.append(v[i])
        t_list.append(t[i])

    elif diff.seconds >= 60:

        with open('/Users/mayuripatil/Desktop/report.txt', "a+") as report:
            report.write("\n" + '{}: {} Time:{}'.format(v[0], a, t[0]))

            for i, each in enumerate(v_list, start=1):
                report.write("\n" + "{}.{}".format(str(i), str(each)))

        del v[0:a + 1]

        del t[0:b + 1]

        del v_list[:]

        del t_list[:]

        i = 0

    i = i + 1

a = len(v_list)
b = len(t_list)


with open('/Users/mayuripatil/Desktop/report.txt', "a+") as report:
    report.write("\n" + '{}: {} Time:{}'.format(v[0], a, t[0]))

    for i, each in enumerate(v_list, start=1):
        report.write("\n" + "{}.{}".format(str(i), str(each)))
