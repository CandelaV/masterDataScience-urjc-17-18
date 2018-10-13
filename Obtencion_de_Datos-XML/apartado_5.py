import xml.etree.ElementTree as ET


def save_xml_to_file(filename, ElementT):

    file = open(filename + ".xml", "wb")
    ElementT.write(file, encoding="UTF-8", xml_declaration=True, method = "xml")
    file.close()


def join_xml():

    tree_facilities = ET.parse('StationFacilitiesNOH.xml')
    root_facilities = tree_facilities.getroot()

    tree_stopfree = ET.parse('StepFreeTubeNNone.xml')
    root_stopfree = tree_stopfree.getroot()

    for item1 in root_facilities.iter('station'):
        station_name_1 = item1.find("name").text

        for item2 in root_stopfree.iter('Station'):
            station_name_2 = item2.find("StationName").text

            if station_name_1 == station_name_2:

                for i in range(7, 7 + len(item2)):

                    item1.insert(i, item2[(i - 7)])

                item1.remove(item1.find("StationName"))

    tree = ET.ElementTree(root_facilities)

    save_xml_to_file('TFLfacilities', tree)


if __name__ == '__main__':
    join_xml()
