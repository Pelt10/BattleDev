import sys

dict = {
    'fe': 'e',
    'ef': 'e',
    
    'fp': 'f',
    'pf': 'f',
    
    'fg': 'f',
    'gf': 'f',
    
    'ep': 'p',
    'pe': 'p',
    
    'es': 's',
    'se': 's',
    
    'pt': 'p',
    'tp': 'p',
    
    'ps': 's',
    'sp': 's',
    
    'pv': 'p',
    'sv': 'p',
}

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


friend = lines[1].split(" ")
me = lines[2].split(" ")


me = ["t" if p == "poison" else p[0] for p in me]
friend = ["t" if p == "poison" else p[0] for p in friend]


print(me, friend)
