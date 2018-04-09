import sys
f = open (sys.argv[1])
r = f.read ()
v = r.split ()
for x in v:
    print (x)
f.close
