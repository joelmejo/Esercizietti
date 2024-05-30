# 1404
# Number of Steps to Reduce a Number in Binary Representation to One

def numSteps(s: str) -> int:
        lista: list = list(s)
        steps: int = 0
        for char in lista:
            char = int(char)
        lista = lista.reverse()
        for i in len(lista) -1:
            lista[i] = lista[i] * (2**i)
        
        decimal: int= sum(lista)

        while decimal != 1:
            if decimal % 2 != 0:
                decimal += 1
                steps += 1
            else:
                decimal //= 2
                steps += 1
        return steps

numSteps("1101")