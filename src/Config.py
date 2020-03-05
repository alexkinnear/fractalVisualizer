import sys



mydict = {}
if len(sys.argv) < 2:
    f = open('data/branches.frac', 'r')
    mydict = {}

    for line in f:
        line = line.split(':')
        if not line[0].startswith('#'):
            if line[0] == 'type':
                mydict[line[0]] = line[1].strip()
            elif line[0] == 'iterations':
                mydict[line[0]] = int(line[1].strip())
            else:
                mydict[line[0]] = float(line[1].strip())


else:
    sys.argv[1] = sys.argv[1].lower()
    f = open(sys.argv[1], 'r')
    mydict = {}

    for line in f:
        line = line.split(':')
        if not line[0].startswith('#'):
            if line[0] == 'type':
                mydict[line[0]] = line[1].strip()
            elif line[0] == 'iterations':
                mydict[line[0]] = int(line[1].strip())
            else:
                mydict[line[0]] = float(line[1].strip())

