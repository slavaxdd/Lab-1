RED = '\u001b[31;5;29m'
END = '\u001b[0m'


'''
pattern B

#  #  #  #
#        #
#     #  #
#     #
#     #  #  #  #
'''

def draw_pattern(n):
    seq = ['•  •  •  •     ', '•        •     ', '•     •  •     ', '•     •        ', '•     •  •  •  ']
    for i in seq: print(i * n)



print(RED)
draw_pattern(8)
print(END)


    

    
