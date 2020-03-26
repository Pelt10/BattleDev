import sys

# Tentative de correspondance avec:
# f -> Feu
# e -> Eau
# p -> Plante
# g -> glace
# s -> Sol
# t -> Poison
# v -> Vol
# la clef étant les affrontement avec résultat et la valeur la resultant du combat
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
# Lecture de stdin
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

# Liste de Pogemon de mon ami
friend = lines[1].split(" ")
# Ma liste de pogemon
me = lines[2].split(" ")

# On transforme la liste pour remplacer poison en t et avoir seulment la première lettre pour le reste
me = ["t" if p == "poison" else p[0] for p in me]
friend = ["t" if p == "poison" else p[0] for p in friend]

print(me, friend)
