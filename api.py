import requests
import json
import pymongo

if __name__ == '__main__':
    # URL: https://api.data.gov/ed/collegescorecard/v1/schools?api_key=hKDHFsoSDyhdWkQKBDAKq81ewzbh4Pb5ccSzlFjD
    url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=hKDHFsoSDyhdWkQKBDAKq81ewzbh4Pb5ccSzlFjD"
    response = requests.get(url)
    data = response.text
    parse_json = json.loads(data)
    print(type(parse_json))
    #client = pymongo.MongoClient("mongodb+srv://Kody:Mordor11@cluster0.uqxgp.mongodb.net/MonstersU?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
    #client['MonstersU']['School Data'].insert_one(parse_json)
