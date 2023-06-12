import requests
import json

def get_planet(val):
    planet = requests.get(val)
    planet_dict = json.loads(planet.text)
    for key, value in planet_dict.items():
        if key == 'name':
            return value

def get_pilot(json_dict):
    pilot_lst = list()
    i = 0
    for k, v in json_dict.items():
        if k == 'pilots':
            for _ in range(len(v)):
                pilot = {}
                a = requests.get(v[i])
                a_dict = json.loads(a.text)
                for key, val in a_dict.items():
                    if key == 'name' or key == 'height' or key == 'mass':
                        pilot[key] = val
                    elif key == 'homeworld':
                        pilot['homeworld_url'] = val
                        pilot['homeworld'] = get_planet(val)
                i += 1
                pilot_lst.append(pilot)
    return pilot_lst

def get_starship():
    ship = {}
    result = requests.get("https://swapi.dev/api/starships/10/")
    if result.status_code == 200:
        json_dict = json.loads(result.text)
        for key, val in json_dict.items():
            if key == 'name' or key == 'max_atmosphering_speed' or key == 'starship_class':
                ship[key] = val
            elif key == 'pilots':
                ship[key] = get_pilot(json_dict)
        print(json.dumps(ship, indent=4, sort_keys=True))
        with open("swap.json", "w") as file:
            json_text = json.dump(ship, file, indent=4)

get_starship()