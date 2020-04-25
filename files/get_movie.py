import apikey
import requests
import json
import random

my_token=apikey.my_token
my_key=apikey.my_key
src_by_board_name=apikey.src_by_board_name
src_by_table_name=apikey.src_by_table_name
board_id=""
table_id=""

def get_board_ids():
    url = 'https://api.trello.com/1/members/me/boards?key='+my_key+'&token='+my_token
    json_data=run_get(url)
    return search_name(json_data,src_by_board_name)

def get_list_ids():
    url = 'https://api.trello.com/1/boards/'+ board_id +'/lists?key='+my_key+'&token='+my_token
    json_data=run_get(url)
    return search_name(json_data,src_by_table_name)

def search_name(data,name):
    for y in range(0,len(data)):
        if data[y]["name"]==name:
            return data[y]["id"]
    return 0

def get_card_names():
    url = 'https://api.trello.com/1/lists/'+table_id+'/cards?key='+my_key+'&token='+my_token
    cards=run_get(url)
    names=[]
    for y in range(0, len(cards)):
        names.append(cards[y]["name"])
    random.shuffle(names)
    print(names[0])

def run_get(url):
    headers = {"Accept": "application/json"}
    response = requests.request("GET",url,headers=headers)
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    return json.loads(response.text)

def get_random_film():
    global board_id
    global table_id

    board_id = get_board_ids()
    table_id = get_list_ids()
    get_card_names()
    
get_random_film()