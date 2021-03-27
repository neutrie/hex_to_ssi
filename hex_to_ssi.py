VERT = '|'
HOR = '_'
SPACE = ' '

print("Number (0-15): ")
INPUT = int(input()) % 16

INPUT = list( map( int, format(INPUT, '#06b')[2:] ) )


a = (not INPUT[0] and not INPUT[1] and not INPUT[2] and INPUT[3]) or (not INPUT[0] and INPUT[1] and not INPUT[2] and not INPUT[3]) or (INPUT[0] and INPUT[1] and not INPUT[2] and INPUT[3]) or (INPUT[0] and not INPUT[1] and INPUT[2] and INPUT[3])
b = (not INPUT[0] and INPUT[1] and not INPUT[2] and INPUT[3]) or (INPUT[1] and INPUT[2] and not INPUT[3]) or (INPUT[0] and INPUT[2] and INPUT[3]) or (INPUT[0] and INPUT[1] and not INPUT[3])
c = (not INPUT[0] and not INPUT[1] and INPUT[2] and not INPUT[3]) or (INPUT[0] and INPUT[1] and not INPUT[3]) or (INPUT[0] and INPUT[1] and INPUT[2])
d = (not INPUT[0] and not INPUT[1] and not INPUT[2] and INPUT[3]) or (not INPUT[0] and INPUT[1] and not INPUT[2] and not INPUT[3]) or (INPUT[1] and INPUT[2] and INPUT[3]) or (INPUT[0] and not INPUT[1] and INPUT[2] and not INPUT[3])
e = (not INPUT[0] and INPUT[3]) or (not INPUT[0] and INPUT[1] and not INPUT[2]) or (not INPUT[1] and not INPUT[2] and INPUT[3])
f = (not INPUT[0] and not INPUT[1] and INPUT[3]) or (not INPUT[0] and not INPUT[1] and INPUT[2]) or (not INPUT[0] and INPUT[2] and INPUT[3]) or (INPUT[0] and INPUT[1] and not INPUT[2] and INPUT[3])
g = (not INPUT[0] and not INPUT[1] and not INPUT[2]) or (not INPUT[0] and INPUT[1] and INPUT[2] and INPUT[3]) or (INPUT[0] and INPUT[1] and not INPUT[2] and not INPUT[3])


print(SPACE + (HOR if not a else SPACE) + SPACE)
print((VERT if not f else SPACE) + (HOR if not g else SPACE) + (VERT if not b else SPACE))
print((VERT if not e else SPACE) + (HOR if not d else SPACE) + (VERT if not c else SPACE))
