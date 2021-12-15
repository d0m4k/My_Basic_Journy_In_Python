/#!/usr/bin/etc/python3

#file read -> 10 

f = open("c.txt", 'a')
i=6
while i<18:
    f.write(str(i))
    i+=1
f.close()
