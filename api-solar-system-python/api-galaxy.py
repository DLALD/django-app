import requests
import os

def get_data():
    os.system("clear") #clear scream
    print(":::: SOLAR SYSTEM INFORMATION :::")
    api_url ="https://api.le-systeme-solaire.net/rest/bodies/?filter%5B%5D=isComet"


    try:
        #request to api
        response =requests.get(api_url)
        response.raise_for_status() # Read error
        

        data = response.json()

        print("#### Main Menu ####")
        print("[1]. Planets")
        print("[2]. Dwarf Planets")
        print("[3]. Moons")
        print("[4]. Stars")
        print("[5]. Asteroid")
        print("[6]. Comets")
        print("[7]. Exit")
        opt = input(":::: Press any options") 

        
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error{e}")


    



#Main
info = get_data()
print(info)
