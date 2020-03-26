import sys

def two(t):
    if t < 10:
        return "0" + str(t)
    return str(t)


lines = []
calendar = []
# Lecture du stdin
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
# On initialise le calendrier => avec le paterne suivant (1 emplacement = 1 minutes):
# 1 = indisponible
# 0 = disponible
# 0h -> 8h(8h): indiponible (8*60)
# 8h -> 18h(10h): disponible (10*60)
# 18h-> 0h(6h): indisponible (6*60)
calendar = ((([1] * (8*60)) + ([0] * (60 * 10)) + ([1] * (60 * 6))) * 5)

# On parcours toute les lignes sauf la premier
for line in lines[1:]:
    day, dates= line.split(" ") # On sépare le jours des heures
    start_date, end_date = dates.split("-") # On sépare les heures
    start = 60 * int(start_date.split(":")[0]) + int(start_date.split(":")[1]) + (int(day) - 1) * (60*24) # On calcule le début en minutes depuis le lundi 0h
    end = 60 * int(end_date.split(":")[0]) + int(end_date.split(":")[1]) + (int(day) - 1) * (60*24) # On calcule la fin en minutes depuis le lundi 0h
    for i in range(start, end + 1): # Et on les rends indisponible
        calendar[i] = 1

# On recherche 1h de dispo dans calendR
start = 0 
min = 0
for i in range(0, 7201): # 7200 -> taille du tableau
    if calendar[i] == 0 and min == 0: # Début d'une plage de disponibilité
        start = i
        min = 1
    elif calendar[i] == 0 and min != 0: # On est entrain de vérifier l'ensemble de la plage
        min = min + 1
        if min == 59:# On à 1h !
            break;
    else:
        min = 0


# La suite c'est juste de la transformation pour l'affichage
day = int(start / (60*24)) + 1

start = start - ((day-1) * 60*24)

end = start + 59

h_s = int(start/60)
start = start - (h_s*60)
m_s = start


h_e = int(end/60)
end = end - (h_e*60)
m_e = end



print(str(day) + " " + two(h_s) + ":" + two(m_s) + "-" + two(h_e) + ":" + two(m_e))


