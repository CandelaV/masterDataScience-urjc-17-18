import requests
import xml.etree.ElementTree as ET


user = '44c0c1ae'
passwd = '926ed95f0d1702e030759ccd836db8b3'

url_facilities = 'https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml'
url_stepfree = 'https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml'


def london_transport_request(url):

    response = requests.get(url,
                            data={"app_id": user,
                                  "app_key": passwd},
                            verify=True)
    return response


def save_xml_to_file(filename, ElementT):

    file = open(filename + ".xml", "wb")
    ElementT.write(file, encoding="UTF-8", xml_declaration=True, method = "xml")
    file.close()


def remove_namespace(root, namespace):

    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in root.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]


def obtain_xml():

    ##############
    # Facilities
    ##############

    url_facilities = 'https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml'

    response_facilities = london_transport_request(url_facilities)
    root_facilities = ET.fromstring(response_facilities.content)

    for item in root_facilities.iter('station'):

        tag_oh = item.find("openingHours")
        item.remove(tag_oh)

    tree_facilities = ET.ElementTree(root_facilities[7])
    save_xml_to_file("StationFacilitiesNOH", tree_facilities)

    ##############
    # StepFree
    ##############

    url_stepfree = 'https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml'

    response_stepfree = london_transport_request(url_stepfree)
    root_stepfree = ET.fromstring(response_stepfree.content)

    ns_stepfree = root_stepfree.tag.split('}')[0].strip('{')

    remove_namespace(root_stepfree, ns_stepfree)

    for item in root_stepfree.iter('Accessibility'):
        tag_a = item.find("AccessibilityType")

        if str(tag_a.text) == "None":
            item.remove(tag_a)

    root_stepfree.remove(root_stepfree.find("Header"))
    tree_stepfree = ET.ElementTree(root_stepfree)
    save_xml_to_file("StepFreeTubeNNone", tree_stepfree)


if __name__ == '__main__':
    obtain_xml()