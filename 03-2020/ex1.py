import sys
import operator


def sortSecond(val): 
    return val[1]  

lines = []
color = {}

# Lecture du stdin
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

# On supprime la première ligne(celle contenant le nombre de ligne)
lines = lines[1:]

for line in lines:
    if line in color: # Si la couleur existe déjà, on incremente 
        color[line] = color[line] + 1;
    else:
        color[line] = 1 # Sinon on la créée avec comme valeur 1

# On trie en fonction des valeurs
color = sorted(color.items(), key=operator.itemgetter(1), reverse = True)

# On affiche le nom des 2 plus gros
print(color[0][0] + " " + color[1][0])

