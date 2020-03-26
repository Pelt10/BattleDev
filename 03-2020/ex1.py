import sys
import operator


def sortSecond(val): 
    return val[1]  

lines = []
color = {}
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
lines = lines[1:]
for line in lines:
    if line in color:
        color[line] = color[line] + 1;
    else:
        color[line] = 1
       
color = sorted(color.items(), key=operator.itemgetter(1), reverse = True)

print(color[0][0] + " " + color[1][0])

