import apikey
import requests
import json
import random

my_token=apikey.my_token
my_key=apikey.my_key
board_id=""
table_id=""

src_by_board_name="Moziverzum"
src_by_table_name="Ajánlások (Nyetflix) aka. randomizer"

def get_board_ids():
    global board_id
    url = 'https://api.trello.com/1/members/me/boards?key='+my_key+'&token='+my_token
    json_data=run_get(url)
    for y in range(0,len(json_data)):
        if json_data[y]["name"]==src_by_board_name:
            board_id = json_data[y]["id"]
    return 0

def get_list_ids():
    global table_id
    url = 'https://api.trello.com/1/boards/'+ board_id +'/lists?key='+my_key+'&token='+my_token
    json_data=run_get(url)
    for y in range(0,len(json_data)):
        if json_data[y]["name"]==src_by_table_name:
            table_id = json_data[y]["id"]
    return 0

def get_card_names():
    url = 'https://api.trello.com/1/lists/'+table_id+'/cards?key='+my_key+'&token='+my_token
    cards=run_get(url)
    names=[]
    for y in range(0, len(cards)):
        names.append(cards[y]["name"])
    randomize_names(names)

def randomize_names(names):
    rnd_num=random.randrange(0, len(names))
    print(names[rnd_num])

def run_get(url):
    headers = {"Accept": "application/json"}
    response = requests.request("GET",url,headers=headers)
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    return json.loads(response.text)
    
def get_random_film():
    get_board_ids()
    get_list_ids()
    get_card_names()
    
get_random_film()