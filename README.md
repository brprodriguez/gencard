# Generador de tarjetas de crédito o débito ficticias

## 📖 Resumen 

- **GenCard.py** es un herramienta basada en python permite que generar tarjetas de pruebas 
**ficticias** y validadas con el algoritmo de Luhn. 

## 📰 Actualizacipones 

* Setiembre 9, 2023: gencard.py v1.0 


## ⚡️ Intalación y uso

Para iniciar, siga los siguientes pasos:

1. **Clone el repositorio de GitHub :** use el siguiente comando the command:
   ```
   git clone https://github.com/brp-rodriguez/gencard.git
   ```
2. **Configure su entorno :** Asegurese de tener 3.10.6 o superior:
   ```
   ```

## ✨️ Opciones 
-------

```
Usage: gencard.py [-m|--modo] [-c|--cant] [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit

  Mandatory:
    -m, --modo          
    -c, --cant 
  Optional
    -b, --bin 
	-f, --filebin    
```

### Simple usage
```
python3 gencard.py -c 100 -m A \ngencard.py obtiene un bin aleatorio del archivo binpe.csv y genera (100) tarjetas ficticias (A)leatorias validadas con el algoritmo de Luhn
```

```
python3 gencard.py -c 30 -m A -b 110110 \ngencard.py recibe el bin (110110) y genera (30) tarjetas ficticias (A)leatorias validadas con el algoritmo de Luhn
```

```
python3 gencard.py -c 2000 -m S \ngencard.py obtiene un bin aleatorio del archivo binpe.csv y genera (2000) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn
```

```
python gencard.py -c 1500 -m A -b 110110 \ngencard.py recibe el bin (110110) y genera (1500) tarjetas ficticias (S)ecuenciales validadas con el algoritmo de Luhn
```
References
---------------
- [Comprehensive Guide on Gencard.py](https://www.notfound/) by BRP


#### Pull requests y nuevas funcionalidades son bienvenidas

License
---------------
Copyright (C) brp-rodriguez 

License: GNU General Public License, version 2
