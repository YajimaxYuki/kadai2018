import sys
f1 = open (sys.argv[1])
f2 = open (sys.argv[2], 'w')
r1 = f1.read ()
f1.close ()
w2 = f2.write (r1)
f2.close ()
