import requests
import sys
import os
import json

API_KEY = os.environ.get('MAC_ADRESS_API_KEY')
OUTPUT = 'json' #possible other formats: xml, csv, vendor (more info: https://macaddress.io/api/documentation/making-requests)

def get_data():
    headers = {'Content-Type': 'application/json'}
    mac_address = str(sys.argv[1]) #user's argument in cmd
    url = r'https://api.macaddress.io/v1?apiKey={}&output={}&search={}'.format(API_KEY, OUTPUT, mac_address)
    print("URL: ", url)
    try:
        response = requests.get(url=url, headers=headers)
        json_data = response.json()
        company_name = json_data["vendorDetails"]["companyName"]
        if company_name == '':
            print("No company name assigned to this MAC adress.") #taking the value of the key: company name
        else:
            print("COMPANY NAME: ", company_name)
    except:
        print("Couldn't get data. Check if the format of MAC address is correct.")


if __name__ == "__main__":
    get_data()
