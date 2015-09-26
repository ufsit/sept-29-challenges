import sys, hashlib

def hash(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

rainbowtable = dict()

infile = sys.argv[1]
with open(infile, 'r') as f:
    for l in f.readlines():
        rainbowtable[hash(l.strip())] = l.strip()

while True:
    h = raw_input('> ')
    if h in rainbowtable.keys():
        print h  + ":" + rainbowtable[h]
