"""
['_sta',
 '_eta',
 '_std',
 '_etd',
 '_platform',
 '_operator_name',
 '_operator_code',
 '_is_cancelled',
 '_disruption_reason',
 '_overdue_message',
 '_ata',
 '_atd',
 '_location_name',
 '_crs',
 '_previous_calling_point_lists',
 '_subsequent_calling_point_lists',
 '__module__',
 '__doc__',
 'field_mapping',
 '__init__',
 '_calling_point_lists',
 'is_cancelled',
 'disruption_reason',
 'overdue_message',
 'ata',
 'atd',
 'location_name',
 'crs',
 'previous_calling_point_lists',
 'subsequent_calling_point_lists',
 'previous_calling_points',
 'subsequent_calling_points',
 'scheduled_arrival',
 'estimated_arrival',
 'scheduled_departure',
 'estimated_departure',
 'sta',
 'eta',
 'std',
 'etd',
 'platform',
 'operator_name',
 'operator_code',
 '__dict__',
 '__weakref__',
 '__new__',
 '__repr__',
 '__hash__',
 '__str__',
 '__getattribute__',
 '__setattr__',
 '__delattr__',
 '__lt__',
 '__le__',
 '__eq__',
 '__ne__',
 '__gt__',
 '__ge__',
 '__reduce_ex__',
 '__reduce__',
 '__subclasshook__',
 '__init_subclass__',
 '__format__',
 '__sizeof__',
 '__dir__',
 '__class__']
"""


from nredarwin.webservice import DarwinLdbSession
from pprint import pprint

darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="abeedf25-c7ae-4b10-bc2e-0c3b0b1c38df")

board = darwin_sesh.get_station_board('STP')

for service in board.train_services:
    # print(service)
    service = darwin_sesh.get_service_details(service.service_id)
    # print(service.std, service.etd, service.destination.location_name)
    # print(service.subsequent_calling_points)
    print("\n\n ---- \n\n")
    for point in service.subsequent_calling_points:
        print(point.location_name, point.et, point.at, point.st)
