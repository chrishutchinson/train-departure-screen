from zeep import Client, Settings, xsd, helpers
from zeep.plugins import HistoryPlugin

def send(LDB_TOKEN, choosecrs, WSDL):
    settings = Settings(strict=False)
    history = HistoryPlugin()
    WSDL = 'https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx' + WSDL
    client = Client(wsdl=WSDL, settings=settings, plugins=[history])

    header = xsd.Element(
        '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}AccessToken',
        xsd.ComplexType([
            xsd.Element(
                '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}TokenValue',
                xsd.String()),
        ]))
    header_value = header(TokenValue=LDB_TOKEN)

    res = client.service.GetDepBoardWithDetails(numRows=10,
                                                crs=choosecrs,
                                                _soapheaders=[header_value])

    serialised_result = helpers.serialize_object(res, dict)

    return serialised_result

print(send("abeedf25-c7ae-4b10-bc2e-0c3b0b1c38df", "AFK", ""))