import os
import requests
# from nredarwin.webservice import DarwinLdbSession
from zeep import Client, Settings, xsd, helpers
from zeep.plugins import HistoryPlugin

def loadDeparturesForStation(journeyConfig, apiKey):
    settings = Settings(strict=False)
    history = HistoryPlugin()
    WSDL = 'https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx'
    client = Client(wsdl=WSDL, settings=settings, plugins=[history])

    header = xsd.Element(
        '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}AccessToken',
        xsd.ComplexType([
            xsd.Element(
                '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}TokenValue',
                xsd.String()),
        ]))
    header_value = header(TokenValue=apiKey)

    res = client.service.GetDepBoardWithDetails(numRows=10,
                                                crs=journeyConfig["departureStation"],
                                                _soapheaders=[header_value])

    serialised_result = helpers.serialize_object(res, dict)

    return serialised_result["trainServices"]["service"], serialised_result["locationName"]

# def loadDeparturesForStation(journeyConfig, apiKey):
#     if journeyConfig["departureStation"] == "":
#         raise ValueError(
#             "Please set the journey.departureStation property in config.json")

#     if apiKey == "":
#         raise ValueError(
#             "Please complete the nreAPI section of your config.json file")

#     departureStation = journeyConfig["departureStation"]

#     # URL = f"http://transportapi.com/v3/uk/train/station/{departureStation}/live.json"

#     # PARAMS = {'app_id': appId,
#     #           'app_key': apiKey,
#     #           'calling_at': journeyConfig["destinationStation"]}

#     # r = requests.get(url=URL, params=PARAMS)

#     # data = r.json()

#     # if "error" in data:
#     #     raise ValueError(data["error"])

#     darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key=apiKey)

#     board = darwin_sesh.get_station_board(departureStation)

#     # for service in board.train_services:
#     #     print(service.std, service.etd, service.destination.location_name)

#     return board.train_services, board.location_name


def loadDestinationsForDeparture(trainService):
    nextStops = []

    for point in trainService["subsequentCallingPoints"]["callingPointList"]:
        # print(point.location_name, point.et, point.at, point.st)
        nextStops.append(point["callingPoint"]["locationName"])

    return nextStops
