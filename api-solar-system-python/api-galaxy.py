import os
import requests

def get_data(body_type):
    fields = ['englishName', 'gravity', 'inclination', 'bodyType']
    try:
        response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
        response.raise_for_status()

        data = response.json()
        if isinstance(data, dict) and 'bodies' in data:
            bodies = data['bodies']
            print("Body Type:", body_type)  # Print the body type
            for body in bodies:
                if body['bodyType'] == body_type:  # Filter by body type
                    print("#########################")
                    for field in fields:
                        print(f"{field}: {body.get(field)}")
        else:
            print("No valid data found.")
            print("API Response:", data)  # Print the complete API response
        return data
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main
while True:
    print("#### MAIN MENU ####")
    print("[1]. Planets")
    print("[2]. Moons")
    print("[3]. Stars")
    print("[4]. Asteroids")
    print("[5]. Comets")
    print("[6]. Exit")
    print("[7]. Clear Screen")
    option = input("Press an option: ")

    if option == '6':
        print("Exiting...")
        break
    elif option == '7':
        clear_screen()
        continue
    
    body_types = {
       '1': "Planet",
       '2': "Moon",
       '3': "Star",
       '4': "Asteroid",
       '5': "Comet"
    }

    if option not in body_types:
        print("Invalid option")
        continue

    body_type = body_types[option]
    info = get_data(body_type)
