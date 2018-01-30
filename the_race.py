
from pwn import *
host = '127.0.0.1'
port = 19999
r = remote(host, port)
for i in range(0,10):
    d = r.recv(2048)
    print d
    s = d.split("'")[-2]
    print s
    c = chr(int(s,2))
    print c
    r.send(c+'\n')
