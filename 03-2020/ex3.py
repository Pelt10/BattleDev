import sys

def two(t):
    if t < 10:
        return "0" + str(t)
    return str(t)


lines = []
calendar = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
calendar = ((([1] * (8*60)) + ([0] * (60 * 10)) + ([1] * (60 * 6))) * 5)

for line in lines[1:]:
    day, dates= line.split(" ")
    start_date, end_date = dates.split("-")
    start = 60 * int(start_date.split(":")[0]) + int(start_date.split(":")[1]) + (int(day) - 1) * (60*24)
    end = 60 * int(end_date.split(":")[0]) + int(end_date.split(":")[1]) + (int(day) - 1) * (60*24)
    for i in range(start, end + 1):
        calendar[i] = 1

start = 0
min = 0
for i in range(0, 7201):
    if calendar[i] == 0 and min == 0:
        start = i
        min = 1
    elif calendar[i] == 0 and min != 0:
        min = min + 1
        if min == 59:
            break;
    else:
        min = 0

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


