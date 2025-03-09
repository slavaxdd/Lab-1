END = '\u001b[0m'

GREEN = '\u001b[48;5;29m'
RED = '\u001b[48;5;161m'

with open('sequence.txt') as f:
    l = [abs(float(x)) for x in f]

half1 = sum(l[:125])
half2 = sum(l[125:])
summ = sum(l)

perc_1 = int(half1/summ * 100 + 0.5) 
perc_2 = int(half2/summ * 100 + 0.5)
print()

print('Процент суммы модулей первых 125 чисел:', f'{GREEN} {END}' * perc_1, sep='\n')
print('Процент суммы модулей вторых 125 чисел:', f'{RED} {END}' * perc_2, sep='\n')







