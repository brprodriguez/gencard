# Generador de tarjetas de crédito o débito ficticias validadas por el algoritmo de Luhn

### Overview 

- **GenCard.py** es un herramienta basada en python que permite generar tarjetas de pruebas 
**ficticias** y validadas con el algoritmo de Luhn.


### Installations

Para iniciar, siga los siguientes pasos:

1. **Clone el repositorio de GitHub :** use el siguiente comando:
   ```
   git clone https://github.com/brprodriguez/gencard.git
   ```
1. **Simple comando :**: Generar 100 tarjetas aleatorias
   ```
   gencard.py -m AT -c 100 
	```

### Options

```
Usage: gencard.py [-m|--modo] [-c|--cant] [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit

  Mandatory:
    -m           (Obligatorio) MODO : AT -> Aleatorio Full Mutiples BIN, S -> Secuencial, A1 -> Aleatorio Simple 1 BIN 
    -c           (Obligatorio) CANT : Cantidad de tarjetas a generar 
    -b           (Opcional)    BIN : Identificador del Banco 
    -f           (Opcional)    FILE-BANK : Nombre del archivo con información 
	                        pública de Bancos. Por defecto se usa 
				el archivo binpe.csv
```

### Simple usage

1. gencard.py obtiene un bin aleatorio del archivo binpe.csv y genera (100) tarjetas ficticias (A)leatorias validadas con el algoritmo de Luhn
```
python3 gencard.py -c 100 -m A 
```
2. gencard.py recibe el bin (110110) y genera (30) tarjetas ficticias (A)leatorias validadas con el algoritmo de Luhn
```
python3 gencard.py -c 30 -m A -b 110110 
```
3. gencard.py obtiene un bin aleatorio del archivo binpe.csv y genera (2000) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn 
```
python3 gencard.py -c 2000 -m S 
```
4. gencard.py recibe el bin (110110) y genera (1500) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn 
```
python gencard.py -c 1500 -m S -b 110110 
```
5. gencard.py recibe el bin (110110) y genera (1500) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn con file bank de Argentina (binar.csv)
```
python gencard.py -c 1500 -m S -b 110110 -f binar.csv
```
References
---------------
- [Comprehensive Guide on Gencard.py](https://www.notfound/) by brp-rodriguez

### Updates

* 2 de setiembre del 2023: gencard.py v1.0

#### Pull requests y nuevas funcionalidades son bienvenidas

License
---------------
Copyright (C) brp-rodriguez 

License: GNU General Public License, version 2
