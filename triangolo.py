# scrivere una funzione disegna_triangolo che prende in input un intero n e disegna un triangolo in n righe con asterischi. esempio:
# disegna_triangolo(5)
#     *
#    ***
#   *****
#  ******* 
# *********

def triangolo(n):
    # num_asterischi = -1
    num_asterisco = 1
    num_space = n - 1
    for i in range(n):
        slice = ''
        asterisco = '*'
        space = ' '
        space *= num_space
        asterisco *= num_asterisco
        slice = space + asterisco
        print(slice)
        # num_space = n//2
        # num_asterischi -= 2 * (n - 1)
        # space *= abs(num_asterischi)
        # slice = asterisco * (n + n - num_asterischi)
        # num_asterischi += 2
        # print(slice)
        num_space -= 1
        num_asterisco += 2
    return None

def triangolo_andrea_corto(n):
    for i in range(n):
        print((n - i - 1) * ' ' + '*' * (2 * i + 1))

def triangolo_andrea(n):
    for i in range(n):
        num_spazi = n - i - 1
        spazi = num_spazi * ' '
        num_asterischi = i * 2 + 1
        asterischi = num_asterischi * '*'
        print(spazi + asterischi)

triangolo(5)
triangolo_andrea(5)

