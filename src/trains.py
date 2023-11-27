import os
import requests
from nredarwin.webservice import DarwinLdbSession


def loadDeparturesForStation(journeyConfig, apiKey):
    if journeyConfig["departureStation"] == "":
        raise ValueError(
            "Please set the journey.departureStation property in config.json")

    if apiKey == "":
        raise ValueError(
            "Please complete the nreAPI section of your config.json file")

    departureStation = journeyConfig["departureStation"]

    # URL = f"http://transportapi.com/v3/uk/train/station/{departureStation}/live.json"

    # PARAMS = {'app_id': appId,
    #           'app_key': apiKey,
    #           'calling_at': journeyConfig["destinationStation"]}

    # r = requests.get(url=URL, params=PARAMS)

    # data = r.json()

    # if "error" in data:
    #     raise ValueError(data["error"])

    darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key=apiKey)

    board = darwin_sesh.get_station_board(departureStation)

    # for service in board.train_services:
    #     print(service.std, service.etd, service.destination.location_name)

    return board.train_services, board.location_name


def loadDestinationsForDeparture(trainService, apiKey):
    nextStops = []

    darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key=apiKey)

    service = darwin_sesh.get_service_details(trainService.service_id)

    for point in service.subsequent_calling_points:
        # print(point.location_name, point.et, point.at, point.st)
        nextStops.append(point.location_name)

    return nextStops
