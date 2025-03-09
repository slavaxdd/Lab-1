GREEN = '\u001b[38;5;29m'
WHITE = '\u001b[37m'
END = '\u001b[0m'

def func_gen():
    fun = []
    for x in range(-10, 10+1):
        y = 2*x + 3
        fun.append([x, y])

    #print(fun)

    for i in range(max(fun, key=lambda x: x[0])[0], min(fun, key=lambda x: x[0])[0] - 1, -1):
        for j in range(-10, 11):
            if [j, i] in fun:
                print(f'{GREEN}•{END}', end=' ')
            elif i == 0 or j == 0: 
                print(f'{WHITE}•{END}', end=' ')
            else:
                print(' ', end=' ')
        print()

func_gen()
