import os
import re
import collections
import itertools
for file in os.listdir(os.getcwd()):
  with open(file)as f:
    ip = []
    ip_of_attacking = []
    d = {}
    t = []
    ipregex = re.compile(r'''
    ((0?0|0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9]).([0-9]+)
    \s
    \IP
    \s
    [0-9]+ \. [0-9]+ \. [0-9]+ \.[0-9]+ \.  [0-9]+
    \s
    \>
    \s
    [0-9]+ \. [0-9]+ \. [0-9]+ \.[0-9]+ \. ([0-9]+ | [a-z0-9]+ | [a-z]+ | [a-z]+\-[a-z]+) \:
    \s
    (?!.*(UDP))
    ([A-Za-z]+ | [0-9]+)
    \s
    \[S]\,
    )
    ''', re.VERBOSE)

    ip = ipregex.findall(s)
    print(ip)

    a = ip[0][0]
    time = a[0:15]
    print('a is {}'.format(a))
    print('time is {}'.format(time))

    d = re.compile(r'''
    [0-9]+ \. [0-9]+ \. [0-9]+ \.[0-9]+
    ''',re.VERBOSE)
    second_ip = d.findall(a)

    ipregex = re.compile(r'''
    \IP \s
    ([0-9]+ \. [0-9]+ \. [0-9]+ \. [0-9]+)
    ''',re.VERBOSE)
    ip_of_attacking = ipregex.findall(str(ip))

    timeregex = re.compile(r'''
    ((0?0|0[0-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9]).([0-9]+))
    ''',re.VERBOSE)
    second_time = timeregex.findall(str(ip))
    for times in second_time:
         t.append(times[0])
    print (t)

    dictionary = collections.OrderedDict(itertools.izip(ip_of_attacking,t))
    print(dictionary)

    print('ip_of_attacking is {}'.format(ip_of_attacking))

    b = set(ip_of_attacking)
    print(b)

    if len(b) > 1:
        for key,value in dictionary.items():
            print("{} -->").format(f)
            print("scanned from {} at {}").format(key,value)

    if len(b) == 1:
       print("{} -->").format(f)
       print("scanned from {} at {}").format(second_ip[0],time)
