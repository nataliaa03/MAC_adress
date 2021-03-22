FROM ubuntu
ADD MACadress.py /
RUN apt-get update && apt-get install -y python
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install requests
ENV MAC_ADRESS_API_KEY=at_VYT37bIoKyDp7Vs8xweRaw5gn1SNI
ENTRYPOINT [ "python3", "./MACadress.py" ]
#44:38:39:ff:af:57
