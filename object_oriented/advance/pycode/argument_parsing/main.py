import sys
from getopt import getopt

arg : list[str]= sys.argv[1:]

for i in arg:
  print(i)