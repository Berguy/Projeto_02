import os

def kminicio():
    global kmi
    kmi = input('Informe a quilometragem inicial:\n')
    
    os.system('cls')
    
    if kmi.isdigit() and kmi.isnumeric():
        kmi = int(kmi)
        if kmi < 1:
            print('Digite um número maior que "0" zero!\n')
            kminicio()
    else:
        print('Digite apenas números!\n')
        kminicio()

def kmfinal():
    global kmf
    kmf = input('Informe a quilometragem final:\n')
    
    os.system('cls')
    
    if kmf.isdigit() and kmf.isnumeric():
       kmf = int(kmf)
       if kmf < 1:
           print('Digite um número maior que "0" zero!\n')
           kmfinal()
    else:
        print('Digite apenas números!\n')
        kmfinal()        

def kmtotal():
    global tkmr
    tkmr = (kmf - kmi)

def calc1():
        ab1 = input('Informe a quantidade de litros abastecidos:\n')
            
        os.system('cls')
        
        try:
            if not ab1.isalpha():
                ab1 = float(ab1)
                mv = (tkmr / ab1)
                print(f'A média da sua viagem foi de {mv:.2f} km/l\n')
            else:
                print('Digite apenas números!\n')
                calc1()
                
        except ZeroDivisionError:
            print('O programa encontrou um erro.\nNão é possível relizar cálculos sem abastecimento.\nInforme qualquer quantidade abastecida desde que esta\nseja maior que "0" zero.\n')
            calc1()
            
        except ValueError:
            print('Você deve digitar algum valor antes de precionar enter!\n')
            calc1()

def calc2():
    cont = 0
    acl = 0
    while cont < tab:
        ab = input('Informe a quantidade de litros abastecidos:\n')
        
        os.system('cls')
        
        try:
            if not ab.isalpha():
                ab = float(ab)
                acl = (acl + ab)
                cont += 1
                global mv
                mv = (tkmr / acl)
            
        except ZeroDivisionError:
            print('O programa encontrou um erro.\nNão é possível relizar cálculos sem abastecimento.\nInforme qualquer quantidade abastecida desde que esta\nseja maior que "0" zero.\n')
            calc2()
                   
        except ValueError:
            print('Você deve digitar algum valor antes de precionar enter!\n')
            calc2()
            
        except UnboundLocalError:
                print('Digite apenas números!\n')
                calc2()
                
    print(f'A média da sua viagem foi de {mv:.2f} km/l\n')

def abastecimento():
        global tab
        tab = input('Quantos abastecimentos foram feitos:\n')

        os.system('cls')
        
        if tab.isdigit() and tab.isnumeric():
            tab =int(tab)
            if tab <= 0:
                print('IMPOSSÍVEL CALCULAR! DIGITE UM NÚMERO MAIOR QUE "0" PARA CONTINUAR\n')
                abastecimento()
            elif tab == 1:
                kmtotal()
                calc1()
            elif tab > 1:
                kmtotal()
                calc2()
        else:
            print('Digite apenas números!\n')
            abastecimento()
