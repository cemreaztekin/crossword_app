from environ import*
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

def get_clues():
    response = requests.get(URL_JSON)
    soup = BeautifulSoup(response.content, "html.parser")
    content = (json.loads(soup.text))['body']

    group1 = content[0]['clueLists'][0]['name']
    group2 = content[0]['clueLists'][1]['name']

    list = {}
    across_list = []
    down_list = []
    across_clues = content[0]['clues'][0:5]
    down_clues = content[0]['clues'][5:]
    day = datetime.now().strftime("%d/%m/%Y")

    list["day"] = day

    for clue in across_clues:
        no = clue['label']
        text = clue['text'][0]['plain']
        string = (f"{no}. {text}")
        across_list.append(string)

    list[group1] = across_list

    for clue in down_clues:
        no = clue['label']
        text = clue['text'][0]['plain']
        string = (f"{no}. {text}")
        down_list.append(string)

    list[group2] = down_list

    return list
