#!/usr/bin/python
#-*- coding:utf-8 -*-
# by MO

import redis

Host='127.0.0.1'
Port=6379

connect = redis.Redis(host=Host,port=Port)

print(type(connect.info()))
# print(connect.info())

for key in connect.info():
    print(key,connect.info(key))



