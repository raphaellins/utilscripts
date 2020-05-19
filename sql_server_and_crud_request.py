import json
import requests
import pyodbc 
import time

def get_criterios_by_offer_id(offer_id):
    server = 'localhost' 
    database = 'mydb' 
    username = 'pass' 
    password = 'pwd' 

    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    cursor = conn.cursor()

    query = """my select query"""

    cursor.execute(query)

#  SPECIFIC MANIPULATION
    index = 0
    criterios = []
    for row in cursor:
        index = index + 1

        found_value = False
        for d in criterios:
            if d["tipo"] == row[1]:
                d["valores"].append(row[2])
                found_value = True

        if not found_value:
            criterios.append({
                "tipo": row[1],
                "valores": [row[2]]
            })

    return criterios

# //WARNINGGG
def update_offer(offer_id, payload):
    url = 'MY_URL'+ str(offer_id)
    headers = { 'accept' : 'application/json', "Content-Type": "application/json-patch+json" }

    requests.put(url, data=payload, headers=headers)


response = requests.get('MY_URL')

for offer in response.json()["dados"]:
    offer_id = str(offer["id"])

    if len(offer["criterios"]) > 0:
        continue

    print(offer_id, "WITHOUT CRITERIA")

    offer_detail_response = requests.get('MY_URL'+ offer_id)

    offer_detail = offer_detail_response.json()["dados"]

    criterios = get_criterios_by_offer_id(offer_id)

    offer_detail["criterios"] = criterios

    update_offer(offer_id, offer_detail)

    with open(offer_id + "-offer_update.json", "w") as write_file:
        json.dump(offer_detail, write_file)

    time.sleep(1)
