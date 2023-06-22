import os
import requests
import base64

def toBase64(value):
    value_bytes = value.encode('ascii')
    base64_bytes = base64.b64encode(value_bytes)
    return base64_bytes.decode('ascii')

def makeAuthorizedRequest(url, apiConfig):
    username = apiConfig["username"]
    password = apiConfig["password"]

    if username == "" or password == "":
        raise ValueError(
            "Please complete the realtimeTrainsApi section of your config.json file")
    
    authorizationHeader = f"{username}:{password}"
    HEADERS = {"Authorization": f"Basic {toBase64(authorizationHeader)}"}

    r = requests.get(url=url, headers=HEADERS)

    data = r.json()
    
    if "error" in data:
        raise ValueError(data["error"])

    return data

def loadDeparturesForStation(journeyConfig, apiConfig):
    if journeyConfig["departureStation"] == "":
        raise ValueError(
            "Please set the journey.departureStation property in config.json")

    departureStation = journeyConfig["departureStation"]
    destinationStation = journeyConfig["destinationStation"]

    if destinationStation == "":
        URL = f"https://api.rtt.io/api/v1/json/search/{departureStation}"
    else:
        URL = f"https://api.rtt.io/api/v1/json/search/{departureStation}/to/{destinationStation}"

    data = makeAuthorizedRequest(URL, apiConfig)

    if "error" in data:
        raise ValueError(data["error"])

    return data["services"], data["location"]["name"]


def loadDestinationsForDeparture(serviceUid, runDate, apiConfig):
    year, month, day = runDate.split("-")
    URL = f"https://api.rtt.io/api/v1/json/service/{serviceUid}/{year}/{month}/{day}"

    data = makeAuthorizedRequest(URL, apiConfig)

    if "error" in data:
        raise ValueError(data["error"])

    return list(map(lambda x: x["description"], data["locations"]))[1:]
