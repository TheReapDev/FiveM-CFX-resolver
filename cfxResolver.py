from enum import auto
from turtle import color
import requests
import colorama

colorama.init(autoreset=True)
cfxID = input("CFX ID: ")
headers = {
    "User-Agent":"CFX resolver - Spyosecure, Reaper"
}

if "/join/" in cfxID:
    cfxID = cfxID.split("in/")
    cfxID = cfxID[1]

def findIP(cfxID):
    response = requests.get("https://servers-frontend.fivem.net/api/servers/single/{}".format(cfxID), headers=headers).json()

    for IP in response["Data"]["connectEndPoints"]:
        print(f"{colorama.Fore.GREEN}Server endpoint found: {colorama.Fore.YELLOW}{IP}")

if __name__ == "__main__":
    findIP(cfxID)