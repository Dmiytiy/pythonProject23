import json
from pprint import pprint

def load_candidate():
    with open('candidate.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        #Создадим словарь и переберём всех кондитатов
        candidate = {}
        for i in data:
            candidate[i['id']] = i
        #pprint(condidate)
        return candidate
load_candidate()