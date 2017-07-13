import xml.etree.cElementTree as ET

tree = ET.parse("D:/export_other_to_crew_bid_MHCC_20170626_080918_latchr.xml")

#return comma separated values for trip data with region and crew vacancies
def get_tripId_region_vacancies():
    for node in tree.iterfind(".//trip"):
        tripKeyIter_ = node.findall('tripKey')
        regions= node.find('regions')
        tripID = node.attrib['bidTripIdentifier']

        for node2 in tripKeyIter_:
              print(tripID + ',' + node2.attrib['name'] + ',' + node2.attrib['dor'] + ',' + regions.text + ',' +
              node.find("tripOpenPositions[@rank='CP']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='FO']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='SO']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='E1']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='E2']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='F1']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='F2']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='F3']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='F4']").attrib['slots'] + ',' +
              node.find("tripOpenPositions[@rank='F5']").attrib['slots'] )


# return comma separated values location data
def get_locationData():
    for node in tree.iterfind(".//locationdata"):
        locationData=node.findall('location')
        for node2 in locationData:
              print(node2.attrib['airport']+","+node2.attrib['city']+","+node2.attrib['country']+","+node2.attrib['name']+","+node2.attrib['timeZone'])

def get_destinationData():
    for node in tree.iterfind(".//destinationdata/destinations"):
        destinationData = node.findall('destination')
        for node2 in destinationData:
            print(node2.attrib['airport'] + "," + node2.attrib['layover'] + "," + node2.attrib['name'] + "," +node2.attrib['stop'])

def get_regionData():
    for node in tree.iterfind(".//regiondata/regions"):
        region_data = node.findall('regionInfo')
        for node2 in region_data:
            print(node2.text)


# return comma separated values trip data
def get_tripId_details():
    for node in tree.iterfind(".//trip"):
        tripKey = node.find("tripKey")
        duties = node.iterfind("duty")
        activities = node.iterfind("duty/activity")

        for legs in activities:
            if legs.find("flightLeg"):
                if legs.find('flightLeg[@connectionTimeMinutes]'):
                    print(tripKey.attrib['name'] + ',' +
                    legs.find("flightLeg").attrib['startStation'] + ',' +
                    legs.find("flightLeg").attrib['endStation'] + ',' +
                    legs.find("flightLeg").attrib['udor'] + ',' +
                    legs.find("flightLeg").attrib['startTime'] + ',' +
                    legs.find("flightLeg").attrib['endTime'] + ',' +
                    legs.find("flightLeg").attrib['carrier'] + ',' + '00' +
                    legs.find("flightLeg").attrib['flightNumber'] + ',' +
                    legs.find("flightLeg").attrib['aircraftType'] + ','+
                    legs.find("flightLeg").attrib['connectionTimeMinutes'])
                else:
                    print(tripKey.attrib['name'] + ',' +
                    legs.find("flightLeg").attrib['startStation'] + ',' +
                    legs.find("flightLeg").attrib['endStation'] + ',' +
                    legs.find("flightLeg").attrib['udor'] + ',' +
                    legs.find("flightLeg").attrib['startTime'] + ',' +
                    legs.find("flightLeg").attrib['endTime'] + ',' +
                    legs.find("flightLeg").attrib['carrier'] + ',' + '00' +
                    legs.find("flightLeg").attrib['flightNumber'] + ',' +
                    legs.find("flightLeg").attrib['aircraftType'])
            elif legs.find("groundTask"):
                print(tripKey.attrib['name'] + ',' +
                legs.find("groundTask").attrib['startStation'] + ',' +
                legs.find("groundTask").attrib['endStation']+','+
                legs.find("groundTask").attrib['startTime'] + ',' +
                legs.find("groundTask").attrib['endTime'] + ',' +
                legs.find("groundTask").attrib['activityType']+','+
                legs.find("groundTask").attrib['groupCode'])


get_tripId_details()

