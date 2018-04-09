import sys
f = open (sys.argv[1])
r = f.read ()
v = r.split ()
d = {}
i = 0
for x in v:
    result = v.count (x)
    d[x] = result
for k, m in sorted (d.items (), key = lambda x: -x[1]):
    if i < 10:
        print ("     " + str (m) + " " + str (k))
        i = i + 1
    else:
        break
f.close ()
