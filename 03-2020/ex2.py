import sys

lines = []
# Lectyre dy stdin
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
# On supprimne la première ligne(celle contenant le nombre de ligne)
lines = lines[1:]

# Valeur en cours de test
x=lines[0]
# Nombre de fois où on a vu x
nbr=1
# Le maximum actuel
max=1
# La première valeur à déjà été lu donc on ne la lis pas
for i in lines[1:]:
    if i == x: # La valeur actuel est identique à la valeur précédente
        nbr = nbr + 1 # On incremente
    else:
        if nbr > max: # Si notre dernière série de x est > à l'actuel max
            max = nbr # On le change
        nbr = 1 # On re-init les valeurs
        x = i 
# Identique à la ligne 21/22
if nbr > max:
    max = nbr

print(max)
