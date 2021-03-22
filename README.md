# MAC_adress

Pass mac address and get the company name.
Correct format mac addres: XX:XX:XX:XX:XX:XX <br>
where each X is a hexadecimal digit (0 to 9 or A to F).

Program using API of web app https://macaddress.io.

## Installation requirements

Install docker - https://www.docker.com/get-started 

Allow your user to run docker (linux only):  
>sudo usermod -G docker -a $USER


## Before run

To run the program you need to login to https://macaddress.io/api and get your api key. Once you get the key, you will pass it as an command parameter (see in Run section).
<br>
<br>



## Run using default API key (testing purposes only)

Command with a mac adress as a parameter:
```
$ docker run mac_company <mac adress>
```

for exmple: 
```
$ docker run mac_company 44:38:39:ff:ef:57
```


## Run using your API key
Command with a mac adress as a parameter:
```
$ docker run --env MAC_ADRESS_API_KEY=<your_api_key> mac_company <mac adress>
```


