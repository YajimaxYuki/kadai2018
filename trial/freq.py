import sys
f1 = open (sys.argv[1])
f2 = open (sys.argv[2], "r+")
r1 = f1.read()
v1 = r1.split()
d  = {}
i  = 0
for key in set (v1):
    d [key] = v1.count (key)
for k, m in sorted(d.items(), key = lambda x: -x[1]):
    if i < 10:
        print ("     " + str (m) + ": " + str (k))
        f2.write ("     " + str (m) + " " + str (k) + "\n")
        i += 1
    else:
        break
f1.close ()
f2.close ()
