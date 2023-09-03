import random
import argparse
import locale
import csv
import datetime
import re

MODO_ALEATORIO_FULL = 'AT'
MODO_ALEATORIO_1BIN = 'A1'
MODO_SECUENCIAL = 'S'

fecha_actual = datetime.datetime.now()
mes_actual = fecha_actual.month
ano_actual = fecha_actual.year

def fecha_expiracion_aleatorio(mes_actual,ano_actual):

    ano_aleatorio = random.randint(ano_actual, ano_actual + 10)
    if ano_aleatorio == ano_actual:
        mes_aleatorio = random.randint(mes_actual , 12)  
    else:
        mes_aleatorio = random.randint(1, 12)
    mes_aleatorio_string = f"{mes_aleatorio:02d}"
    return mes_aleatorio_string + ","+ str(ano_aleatorio % 100)
    
def cvv_aleatorio():
    codigo_aleatorio = random.randint(0, 999)
    codigo_aleatorio = f"{codigo_aleatorio:03d}"
    return codigo_aleatorio

def validar_bincode(bincode):    
    patron = r'^\d{6}$' #Caso general de 6 digitos   
    return True if re.match(patron, bincode) else False    

def validar_cantidad(valor):
    return valor.isdigit() and int(valor) > 0 
   
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

parser = argparse.ArgumentParser(description="Generador de número de tarjetas ficticias y validadas con el algoritmo de Luhn")
parser.add_argument('-m', metavar="Modo" ,type=str, help='MODO : AT -> Tarj. aleatorias con multiples BANK CODEs, A1 -> Tarj. aleatoria con 1 BANK CODE fijo, pero aleatorio, S -> Secuencial (Obligatorio)')
parser.add_argument('-c', metavar="Cant" ,type=int,  help='CANT : Cantidad de tarjetas a generar (Obligatorio)')
parser.add_argument( '-b' , metavar="Bin" ,type=str,  help='BIN : Identificador del Banco (Opcional)')
parser.add_argument( '-nd' , metavar="NunDig" ,type=str, default='16', help='Numero de digitos : 16 caso generico para VISA u otros o 15 para casos como AMEX (Opcional)')
parser.add_argument( '-f', metavar="File" ,type=str, default='./binfiles/binpe.csv', help='FILE PATH BANK INFO : Nombre del archivo con información pública de Bancos (Opcional). Por defecto se usa el archivo binpe.csv')

args = parser.parse_args()
    
if (args.m is None) or (args.c is None):
    print("\nError!!! -> Los siguentes parametros son obligatorios: -m modo, -c cant\n")
    print("Ejemplos:\n")
    print("python gencard.py -c 100 -m A \ngencard.py obtiene un bin aleatorio del archivo /binfile/binpe.csv y genera (100) tarjetas ficticias (A)leatorias validadas con el algoritmo de Luhn \n" )
    print("python gencard.py -c 30 -m A -b 110110 \ngencard.py recibe el bin (110110) y genera (30) tarjetas ficticias (A)leatorias validadas con el algoritmo de Luhn \n" )
    print("python gencard.py -c 2000 -m S \ngencard.py obtiene un bin aleatorio del archivo /binfiles/binpe.csv y genera (2000) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn \n" )
    print("python gencard.py -c 1500 -m S -b 110110 \ngencard.py recibe el bin (110110) y genera (1500) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn \n" )
    exit(1)

if (not args.b is None ) and (args.nd is None):
    print("\nError!!! -> El numero de digitos (-nd) es necesaria en caso se use el identificador del Banco (bin): VISA para 16 digitos y AMEX 15 digitos")
    exit(1)

if (not args.b is None ) and (not validar_bincode(args.b)):
    print("\nError!!! -> El identificador del Banco (bin) '" + str(args.b)+"' ingresado posee un formato invalido. Debe poseer 6 digitos")
    exit(1)

if (not (args.m == 'A1')) and (not (args.m == 'S')) and (not (args.m == 'AT')) :
    print("\nError!!! -> El modo permitido es '-m AT' (A)leatorio total o '-m S' (S)ecuencial o '-m A1' (A)leatorio 1 Bin\n")
    exit(1)

if (args.c <= 0 ):
    print("\nError!!! -> La cantidad de tarjetas debe ser un numero entero positivo\n")
    exit(1)
  

modo = args.m             # (Modo)              Obligatorio
cantidad = args.c         # (Cant)              Obligatorio
bincode = args.b          # (Bin)               Opcional
num_digitos = args.nd     # (Numero de digitos) Opcional, por defecto 16 
file_bank = args.f        # (File Bank)         Opcional 


def lectura_bin_from_file(filename):
    with open(filename, 'r', newline='') as archivo:    
        lineas = archivo.readlines()        
        for h,linea in enumerate(lineas):
            if(h==0):
                continue 
            bank_info = linea.strip().split(',')
            bincode = bank_info[0]
            brand = bank_info[1]
            tipo = bank_info[2]
            categoria = bank_info[3]
            emisor = bank_info[4]
            alpha_2 = bank_info[5]
            alpha_3 = bank_info[6]
            latitud = bank_info[8]
            longitud = bank_info[9]
            telefono = bank_info[10]
            url = bank_info[11]
            array_bank_info.append(bank_info)
            #print(bank_info)
    return array_bank_info    

# Verificación de números en el PAN
def isNumberString(s):    
    for char in s:
        if not char.isdigit():
            return False
    return True

def validator(ccNumber):
    # Código "Validator" adaptado a Python del respositorio de Karancode'
    # https://github.com/karancodes/credit-card-validator/blob/master/credit-card-validator.cpp
    if not isNumberString(ccNumber):
        print("Bad input!")        

    len_cc = len(ccNumber)
    doubleEvenSum = 0

    for i in range(len_cc - 2, -1, -2):
        dbl = int(ccNumber[i]) * 2
        if dbl > 9:
            dbl = (dbl // 10) + (dbl % 10)
        doubleEvenSum += dbl

    for i in range(len_cc - 1, -1, -2):
        doubleEvenSum += int(ccNumber[i])

    result = "OK" if doubleEvenSum % 10 == 0 else "NOTOK"    
    return result

array_bank_info = []

if __name__ == "__main__":
    cant_dig_retante=10 #defecto
    limite_nueves = 9999999999 #defecto
    if bincode==None:
        # Leyendo el archivo por defecto binpe.csv ...
        array_bin_code = lectura_bin_from_file(file_bank)
        random_bin_code = random.randint(0,len(array_bin_code)-1)                
        parte1 = str(array_bin_code[random_bin_code][0]) # <- Generar un codigo bin  
        brand =  str(array_bin_code[random_bin_code][1])
        #AMERICAN EXPRESS
        if brand == "AMERICAN EXPRESS":        
            cant_dig_retante = 9
            limite_nueves = 999999999
        else:
            cant_dig_retante = 10
            limite_nueves = 9999999999
        if (modo==MODO_SECUENCIAL):
            z = 0
            for i in range(0,limite_nueves):                
                parte2 = str(i).zfill(cant_dig_retante)
                tarjeta = parte1 + parte2                
                if validator(tarjeta) == "OK":
                    z+=1 
                    print( str(z) + ") "+  tarjeta + ","  + fecha_expiracion_aleatorio(mes_actual,ano_actual) + "," + cvv_aleatorio())
                    if (z==cantidad):
                        break        
        if (modo ==MODO_ALEATORIO_1BIN):            
            z = 0
            for i in range(0,limite_nueves):
                j = random.randint(0, limite_nueves) # Caso aleatorio se escoge un numero random de 10 diigitos
                parte2 = str(j).zfill(cant_dig_retante)
                tarjeta = parte1 + parte2                
                if validator(tarjeta) == "OK":
                    z+=1 
                    print( str(z) + ") "+  tarjeta + ","  + fecha_expiracion_aleatorio(mes_actual,ano_actual) + "," + cvv_aleatorio())
                    if (z==cantidad):
                        break
        w=0
        if (modo == MODO_ALEATORIO_FULL):
            len_array = len(array_bin_code)
            while w < cantidad: 
                random_bin_code_incide = random.randint(0,len_array-1)                
                #print(str(random_bin_code_incide))
                #print(array_bin_code[random_bin_code])
                #print("---")
                #print("Total " + str(len_array))
                #print("Incide +" + str(random_bin_code_incide))
                #print("Total " + str(len(array_bin_code)))
                #print("Bin aleatorio" + str(array_bin_code[random_bin_code_incide]))
                #print("" + str(random_bin_code_incide))
                parte1 = str(array_bin_code[random_bin_code_incide][0]) # <- Generar un codigo bin  
                #if (array_bin_code[random_bin_code][1] is None):
                #    print("no hay")
                brand =  str(array_bin_code[random_bin_code_incide][1])
                
                if brand == "AMERICAN EXPRESS":        
                    cant_dig_retante = 9
                    limite_nueves = 999999999
                else:
                    cant_dig_retante = 10
                    limite_nueves = 9999999999            
                j = random.randint(0, limite_nueves)
                parte2 = str(j).zfill(cant_dig_retante)
                tarjeta = parte1 + parte2                
                if validator(tarjeta) == "OK":
                    w+=1 
                    print( str(w) + ") "+  tarjeta + ","  + fecha_expiracion_aleatorio(mes_actual,ano_actual) + "," + cvv_aleatorio())
                    #print(brand)
                    if (w==cantidad):
                        break
        
    else:
        parte1 = bincode
        if num_digitos == '15': #America Express               
            cant_dig_retante = 9
            limite_nueves = 999999999
        else:
            cant_dig_retante = 10
            limite_nueves = 9999999999
        if (modo ==MODO_SECUENCIAL):
            z = 0
            for i in range(0,limite_nueves):                
                parte2 = str(i).zfill(cant_dig_retante)
                tarjeta = parte1 + parte2                
                if validator(tarjeta) == "OK":
                    z+=1 
                    print( str(z) + ") "+  tarjeta + ","  + fecha_expiracion_aleatorio(mes_actual,ano_actual) + "," + cvv_aleatorio())
                    if (z==cantidad):
                        break
        if (modo == MODO_ALEATORIO_1BIN):            
            z = 0
            for i in range(0,limite_nueves):
                j = random.randint(0, limite_nueves) # Caso aleatorio se escoge un numero de 10 diigitos
                parte2 = str(j).zfill(cant_dig_retante)
                tarjeta = parte1 + parte2                
                if validator(tarjeta) == "OK":
                    z+=1 
                    print( str(z) + ") "+  tarjeta + ","  + fecha_expiracion_aleatorio(mes_actual,ano_actual) + "," + cvv_aleatorio())
                    if (z==cantidad):
                        break
        
            
        
            
    
    
