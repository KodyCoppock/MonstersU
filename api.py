import requests
import json
import pymongo

if __name__ == '__main__':
    # URL: https://api.data.gov/ed/collegescorecard/v1/schools?api_key=hKDHFsoSDyhdWkQKBDAKq81ewzbh4Pb5ccSzlFjD
    i=0
    client = pymongo.MongoClient("mongodb+srv://Kody:Mordor11@cluster0.uqxgp.mongodb.net/MonstersU?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
    while True:
        url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=hKDHFsoSDyhdWkQKBDAKq81ewzbh4Pb5ccSzlFjD&_per_page=100&_page={}".format(i)
        response = requests.get(url)
        data = response.text
        parse_json = json.loads(data)
        if response.status_code != 200:
            break
        else:
            client['MonstersU']['School Data'].insert_many(parse_json["results"])
            i = i + 1
