# -*- coding: utf-8 -*-
import argparse
parser = argparse.ArgumentParser(description='此代码用于求两个整数之和')
parser.add_argument("a",type=int, help="第一个整数")
parser.add_argument("b",type=int, help="第二个整数")
args = parser.parse_args()

sum=args.a+args.b
print(sum)
