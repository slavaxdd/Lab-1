# s, k = [], 0
# for i in range(-4, 5):
#     s.append([])
#     for j in range(-4, 14):
#         if ((i-2)**2 + (j-2)**2 <= 16): s[k].append(' 0 ')
#         else: s[k].append(' . ')
#     s[k] = ''.join(s[k])
#     k += 1

# [print(s[i]) for i in range(9)]

for i in range(-5, 5+1):
    for j in range(-8, 12):
        if (i**2 + j**2) <= 9: print('  0  ', end='')
        else: print('  .  ', end='')
    print('\n')
