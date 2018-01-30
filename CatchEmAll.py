#!/usr/bin/python
# -*-  coding: utf-8 -*-

from pwn import *
import base64

with open("given-easy.txt","r") as f:
    lines = f.readlines()
index = 1
j = ""
for i in lines:
    if index % 8 is 0:
	temp = base64.b64decode(i)
        if (temp[4:8].isupper()):
		j += temp[4:8]
    index+=1
print(j)
