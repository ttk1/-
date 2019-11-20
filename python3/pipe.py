#!/usr/bin/env python

from subprocess import Popen, PIPE

p1 = Popen(['echo', 'abcd'], stdout=PIPE)
p2 = Popen(['tr', 'ad', 'da'], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()
output = p2.communicate()[0]

print(output.decode('utf-8'))
