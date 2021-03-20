# MAC_adress

Program using API of web app https://macaddress.io.

## Requirements

I used Python language so the reqirement is Python3 installed.


## Before run

To run the program you need to login to https://macaddress.io/api and get your api key. Once you get the key, set it as an environment variable:

```
export MAC_ADRESS_API_KEY=”<your api key>”
```

You can also set it as a persisting variable in ~/.bash_profile by adding the export command for the environment variable. 

<br>
<br>

*If you use Windows you need to use command set instead of export.

## Run

Command line with a mac adress as a parameter:
```
$ python3 MACadress.py <mac adress>
```

for exmple: 
```
python3 MACadress.py 44:38:39:ff:ef:57
```

