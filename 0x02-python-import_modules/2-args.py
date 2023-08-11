#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div 
    import sys

    print("{} argument".format(len(sys.argv))
    for i in range(1, len(sys.argv)):
      print("{}: {}".format(str(sys.argv[i]))
