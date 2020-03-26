import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

lines = lines[1:]

x=lines[0]
nbr=1
max=1
for i in lines[1:]:
    if i == x:
        nbr = nbr + 1
    else:
        if nbr > max:
            max = nbr
        nbr = 1
        x = i

if nbr > max:
    max = nbr

print(max)
