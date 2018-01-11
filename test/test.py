#!/usr/bin/env python
#encoding: utf-8      #日本語を使う場合はこれを書く

class A():
    def  __init__(self):
        self.b = '愛'

    def c(self):
        return self.b

if __name__ == '__main__':
    obj = A()
    print obj.c()

