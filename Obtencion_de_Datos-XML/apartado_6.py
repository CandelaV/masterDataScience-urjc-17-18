from rdflib import Graph, URIRef, Literal, Namespace
import xml.etree.ElementTree as ET


def grafo_rdf():

    tfl = Namespace("http://tfl.gov.uk/tfl#")

    g = Graph()

    tree = ET.parse('TFLfacilities.xml')
    root = tree.getroot()

    for item in root.iter('station'):

        station = item[0].text.replace(" ", "")

        uri_station = URIRef("http://urjc.es/estaciones/" + station)

        g.add((uri_station, tfl.name, Literal(item[0].tag)))
        g.add((uri_station, tfl.contact, Literal(item[1].tag)))
        g.add((uri_station, tfl.serving, Literal(item[2].tag)))
        g.add((uri_station, tfl.pertenece, Literal(item[3].tag)))
        g.add((uri_station, tfl.contains, Literal(item[4].tag)))
        g.add((uri_station, tfl.entrance, Literal(item[5].tag)))
        if len(item) > 6:
            g.add((uri_station, tfl.located, Literal(item[6].tag)))
            if len(item) > 7:
                g.add((uri_station, tfl.contain, Literal(item[7].tag)))
                g.add((uri_station, tfl.provide, Literal(item[8].tag)))
                g.add((uri_station, tfl.interchange, Literal(item[9].tag)))
                g.add((uri_station, tfl.include, Literal(item[10].tag)))
                g.add((uri_station, tfl.identified, Literal(item[11].tag)))

    g.serialize(destination="grafoRDF.xml", format="xml")


if __name__ == '__main__':
    grafo_rdf()