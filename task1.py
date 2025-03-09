def draw_flag():

    END = '\u001b[0m'

    GREEN = '\u001b[48;5;29m'
    RED = '\u001b[48;5;161m'


    for i in range(-5, 5+1):
         for j in range(-8, 12):
             if (i**2 + j**2) <= 10: print(f'{RED}  {END}', end='')
             else: print(f'{GREEN}  {END}', end='')
         print()
    
draw_flag()