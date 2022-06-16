import modulo
import os

while True:
    modulo.kminicio()
    modulo.kmfinal()
    modulo.abastecimento()
    
    reset = input('Deseja reiniciar (S / N)?\n')
    os.system('cls')
    
    if not reset in ('S', 's'):
        break
