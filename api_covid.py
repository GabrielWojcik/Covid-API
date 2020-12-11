!pip install matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import requests
import json
import sys
import csv
!pip install pandas
import pandas as pd

ENDPOINT = 'https://api.covid19api.com'
COUNTRY = 'brazil'
start_dt = '2020-03-01'
end_dt = '2020-04-01'

api_brasil = f'{ENDPOINT}/country/{COUNTRY}?from={start_dt}&to={end_dt}'
# print(api_brasil)
# print("\n\n")
response = requests.get(api_brasil)
# print(response.status_code)
if response.status_code == 200:
    print("Ok! Endpoint Funcionando!")
else:
    print("Erro no endpoint")

resp_dict = response.json()
import pprint

print(len(resp_dict))
pprint.pprint(resp_dict)

df = pd.DataFrame(resp_dict)

print(df)
df.to_csv('C:\\Users\\Gabriel\\xxx.csv', index=False)