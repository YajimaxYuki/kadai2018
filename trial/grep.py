import sys
f = open (sys.argv[1])
t = sys.argv[2]
for line in f:
    if line.find (t) >= 0 :
        print (line,end='')
f.close ()
