import json
from tabulate import tabulate

with open('D:/pp2/TSIS/tsis 4/json/data.json', "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 73)

col_names = ["DN", "Description", "Speed", "MTU"]

json_data = []

for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            json_data.append([imdata[i][j]["dn"], " ", imdata[i][j]["speed"], imdata[i][j]["mtu"]])

print(tabulate(json_data, headers=col_names))