# Convertir un numero en base decimal a su equivalente en cualquier base 
# Base tieen que estar entre 2 y 16 

## Realizar una funcion que valide que la base se encuentra entre 2 y 16 
# Recibe un argumento que es la base de tipo entero 
# Debe retornar TRUE si la base se encuentra entre ese rango 
# Caso contrario debe retornar FALSE


import os
def limpiarPantalla():
    os.system("cls")

def validaBaseNumerica (baseNumerica):
    esBaseValida = False
    if(baseNumerica >= 2 and baseNumerica <= 16):
        esBaseValida = True
    return esBaseValida


def devuelveLetra (numero): 
    letra = ""
    if (numero == 10):
        letra = "A"
    elif (numero ==11):
         letra = "B"
    elif (numero ==12):
        letra= "C"
    elif (numero==13):
        letra="D"
    elif (numero == 14):
        letra = "E"
    elif (numero==15):
        letra ="F"    
    else:
        letra = str(numero)  
    return letra    
                          
def convierteNumero (numero,base):    
    valor = ""
    if (base ==2): 
        valor=convierteBase2(numero,base)
        
    elif (base ==3):
        valor=convierteBase3 (numero, base)
        
    elif (base==4):
        valor =convierteBase4 (numero, base)
        
    elif (base == 5):
        valor= convierteBase5 (numero, base)

    elif (base ==6): 
        valor = convierteBase6 (numero,base)
    
    elif (base==7):
        valor= convierteBase7 (numero, base)
    
    elif (base==8): 
        valor= convierteBase8 (numero, base)
        
    elif (base==9):
        valor=convierteBase9 (numero, base)  
    elif (base==10):
        valor= numero     
    elif (base == 11):
        valor =convierteBase11 (numero, base) 
    elif (base ==12):
        valor = convierteBase12 (numero, base)
    elif (base == 13):
        valor = convierteBase13 (numero, base)
    elif (base == 14):
        valor = convierteBase14 (numero, base)
    elif (base == 15): 
        valor = convierteBase15(numero, base)
    elif (base == 16): 
        valor = convierteBase16(numero, base)
    
    return  valor                  
    
def convierteBase2 (num, base):
    binario = ""
    numBase2 = 0 
    resto =num
    while (resto > 1):
        numBase2 = resto % base 
        binario = str(numBase2) + binario 
        resto = resto // base  
    binario = str (resto) + binario 
    return binario

def convierteBase3 (num, base): 
    
    terciaria = ""
    numBase3= 0
    resto =num 
    while (resto>2):
        numBase3 = resto % base
        terciaria = str(numBase3)+ terciaria
        resto = resto // base
    terciaria = str(resto)+ terciaria 
    return terciaria    

def convierteBase4 (num,base):
    cuartenario = ""
    numBase4= 0
    resto = num
    while (resto >3):
        numBase4= resto % base
        cuartenario = str(numBase4) + cuartenario
        resto = resto // base 
    cuartenario = str(resto) + cuartenario
    return cuartenario
        
def convierteBase5 (numero,base):
    quinario = ""
    numeroBase5 = 0
    resto = numero 
    while (resto >4):
        numeroBase5 = resto % base 
        quinario = resto % base 
        resto  = resto // base 
    quinario = str(resto)  + quinario    
    return quinario  

def convierteBase6 (num,base): 
    senario = ""
    numBase6 = 0
    resto = num
    while (resto >5):
        numBase6 = resto % base
        senario = str(numBase6) + senario  
        resto = resto // base 
    senario = str(resto) + senario     
    return senario

def convierteBase7 (num, base):
    heptal = ""
    numBase7 = 0
    resto = num
    while (resto >6):
        numBase7 = resto % base
        heptal = str(numBase7) + heptal 
        resto = resto // base 
    heptal = str(resto) + heptal     
    return heptal 
    
def convierteBase8 (num,base): 
    octal= ""
    numBase8 = 0
    resto = num
    while (resto >7):
        numBase8 = resto % base
        octal = str(numBase8) + octal 
        resto = resto // base 
    octal = str(resto) + octal     
    return octal 

def convierteBase9 (num, base):
    nonario= ""
    numBase9 = 0
    resto = num
    while (resto >8):
        numBase9 = resto % base
        nonario= str(numBase9) + nonario
        resto = resto // base 
    nonario= str(resto) + nonario     
    return nonario 

def convierteBase11 (num, base):
    undecimal = ""
    numBase11 = 0
    resto = num 
    while (resto >10): 
        numBase11= resto % base
        if (numBase11 >9):
           undecimal = devuelveLetra (numBase11)+ undecimal
        else:
            undecimal = str(numBase11) + undecimal
        resto = resto // base 
    undecimal = devuelveLetra (resto)+ undecimal
    return undecimal   

def convierteBase12 (num, base):
    duodecimal = ""
    numBase12 = 0
    resto = num 
    while (resto >12): 
        numBase12= resto % base
        if (numBase12 >9):
           duodecimal = devuelveLetra (numBase12)+ duodecimal
        else:
            duodecimal = str(numBase12) + duodecimal
        resto = resto // base 
    duodecimal = devuelveLetra (resto)+ duodecimal
    return duodecimal   

def convierteBase13 (num, base):
    tridecimal = ""
    numBase13 = 0
    resto = num 
    while (resto >12): 
        numBase13= resto % base
        if (numBase13 >9):
           tridecimal = devuelveLetra (numBase13)+ tridecimal
        else:
            tridecimal = str(numBase13) + tridecimal
        resto = resto // base 
    tridecimal = devuelveLetra (resto)+ tridecimal
    return tridecimal   

def convierteBase14 (num, base):
    tetradecimal = ""
    numBase14 = 0
    resto = num 
    while (resto >13): 
        numBase14= resto % base
        if (numBase14 >9):
           tetradecimal = devuelveLetra (numBase14)+ tetradecimal
        else:
            tetradecimal = str(numBase14) + tetradecimal
        resto = resto // base 
    tetradecimal = devuelveLetra (resto)+ tetradecimal
    return tetradecimal   

def convierteBase15 (num, base):
    pentadecimal = ""
    numBase15 = 0
    resto = num 
    while (resto >14): 
        numBase15= resto % base
        if (numBase15 >9):
            pentadecimal = devuelveLetra (numBase15)+ pentadecimal
        else:
            pentadecimal = str(numBase15) + pentadecimal
        resto = resto // base 
    pentadecimal = devuelveLetra (resto)+ pentadecimal
    return pentadecimal               

def convierteBase16 (num, base ):
    hexadecimal = ""
    numBase16 = 0 
    resto = num 
    while (resto >15):
        numBase16 = resto % base 
        if (numBase16 >9):
            hexadecimal = devuelveLetra(numBase16) + hexadecimal
        else: 
            hexadecimal = str(numBase16) + hexadecimal
        resto = resto // base 
    hexadecimal = devuelveLetra(resto)+ hexadecimal            
    return hexadecimal    
    
    

if (__name__ == "__main__"):
    limpiarPantalla()
    base = int(input("Ingrese la Base: "))
    numero= int(input("Ingrese el numero en base decimal: "))
    
    baseValida= validaBaseNumerica (base)
    
    if (baseValida): 
        print (convierteNumero(numero, base))
    else: 
        print("No se puede convertir el numero")