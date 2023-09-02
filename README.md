# Generador de tarjetas de crédito o débito ficticias validadas por el algoritmo de Luhn

## 📖 Resumen 

- **GenCard.py** es un herramienta basada en python que permite generar tarjetas de pruebas 
**ficticias** y validadas con el algoritmo de Luhn. 

## 📰 Actualizacipones 

* 2 de setiembre , 2023: gencard.py v1.0 


## ⚡️ Intalación y uso

Para iniciar, siga los siguientes pasos:

1. **Clone el repositorio de GitHub :** use el siguiente comando the command:
   ```
   git clone https://github.com/brp-rodriguez/gencard.git
   ```

## ✨️ Opciones 
-------

```
Usage: gencard.py [-m|--modo] [-c|--cant] [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit

  Mandatory:
    -m,           (Obligatorio) MODO : A -> Aleatorio, S -> Secuencial          
    -c,           (Obligatorio) CANT : Cantidad de tarjetas a generar 
  Optional
    -b,           (Opcional)    BIN : Identificador del Banco 
    -f,           (Opcional)    FILE-BANK : Nombre del archivo con información 
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
References
---------------
- [Comprehensive Guide on Gencard.py](https://www.notfound/) by brp-rodriguez


#### Pull requests y nuevas funcionalidades son bienvenidas

License
---------------
Copyright (C) brp-rodriguez 

License: GNU General Public License, version 2
